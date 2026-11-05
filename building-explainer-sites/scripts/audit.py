#!/usr/bin/env python3
"""Audit an explainer page against the skill's automatable rules.

Usage:
    python scripts/audit.py page.html            # local file
    python scripts/audit.py https://example.com  # URL
    python scripts/audit.py page.html --json report.json

Renders the page with headless Chromium at 320, 390 and 1280 px, plus JS-off,
dark color scheme and reduced-motion variants. Prints PASS / WARN / FAIL per
check. Exit code: 0 = no FAIL, 1 = at least one FAIL, 2 = setup problem.

Requires: pip install playwright && python -m playwright install chromium
"""
import argparse
import json
import os
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("SETUP: Playwright is not installed. Run:\n"
          "  pip install playwright && python -m playwright install chromium")
    sys.exit(2)

# Thresholds (see SKILL.md "Hard rules and soft defaults").
MIN_BODY_PX_MOBILE = 16        # hard rule: body text >= 16px
LONGFORM_WORDS = 1500          # pages longer than this count as long-form
LONGFORM_BODY_PX_DESKTOP = 18  # soft default: 18-20px on desktop long-form
CPL_RANGE = (45, 80)           # soft default ~55-75; warn outside 45-80
CONTRAST_NORMAL = 4.5          # WCAG 1.4.3
CONTRAST_LARGE = 3.0           # >= 24px, or >= 18.66px bold
TARGET_MIN = 24                # WCAG 2.5.8, CSS px
JS_OFF_FAIL_RATIO = 0.5        # JS-off text below 50% of JS-on text = FAIL
JS_OFF_WARN_RATIO = 0.8

PAGE_JS = r"""
() => {
  const parse = (c) => {
    const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number);
    return {r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1};
  };
  const blend = (top, bottom) => ({
    r: top.r * top.a + bottom.r * (1 - top.a),
    g: top.g * top.a + bottom.g * (1 - top.a),
    b: top.b * top.a + bottom.b * (1 - top.a), a: 1});
  const lum = (c) => {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b);
  };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
  const visible = (el) => {
    const s = getComputedStyle(el), r = el.getBoundingClientRect();
    return s.visibility !== 'hidden' && s.display !== 'none' && parseFloat(s.opacity) > 0 && r.width > 0 && r.height > 0;
  };
  const effectiveBg = (el) => {
    const layers = []; let hasImage = false;
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      const s = getComputedStyle(n);
      if (s.backgroundImage && s.backgroundImage.includes('url(')) hasImage = true;  // gradients use background-color
      const c = parse(s.backgroundColor);
      if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; }
    }
    let bg = {r: 255, g: 255, b: 255, a: 1};
    for (let i = layers.length - 1; i >= 0; i--) bg = blend(layers[i], bg);
    return {bg, hasImage};
  };
  const label = (el) => {
    const t = (el.innerText || el.getAttribute('aria-label') || el.value || '').trim().replace(/\s+/g, ' ');
    return el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (t ? ' "' + t.slice(0, 40) + '"' : '');
  };

  const out = {};
  const docEl = document.documentElement;
  out.overflow = docEl.scrollWidth > docEl.clientWidth + 1;
  out.scrollWidth = docEl.scrollWidth; out.clientWidth = docEl.clientWidth;
  out.bodyBg = getComputedStyle(document.body).backgroundColor;

  const root = document.querySelector('main') || document.body;
  out.words = (root.innerText || '').split(/\s+/).filter(Boolean).length;

  // Body text size and characters per line, from running-text paragraphs.
  const paras = [...root.querySelectorAll('p, li, dd, blockquote')]
    .filter((p) => visible(p) && (p.innerText || '').trim().length > 80 && !p.closest('nav, footer, figure, .chip'));
  const sizes = paras.map((p) => parseFloat(getComputedStyle(p).fontSize)).sort((a, b) => a - b);
  out.bodyPx = sizes.length ? sizes[Math.floor(sizes.length / 2)] : null;
  out.minParaPx = sizes.length ? sizes[0] : null;
  const cpl = [];
  for (const p of paras) {
    const s = getComputedStyle(p);
    if ((p.innerText || '').length < 200) continue;
    let lh = parseFloat(s.lineHeight); if (isNaN(lh)) lh = parseFloat(s.fontSize) * 1.2;
    const lines = Math.round(p.getBoundingClientRect().height / lh);
    if (lines >= 2) cpl.push(Math.round(p.innerText.length / lines));
  }
  cpl.sort((a, b) => a - b);
  out.cplMedian = cpl.length ? cpl[Math.floor(cpl.length / 2)] : null;

  // Text contrast: every visible element that owns a non-empty text node.
  const failures = []; let checked = 0; let overImage = 0;
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  while (walker.nextNode()) {
    const t = walker.currentNode; const el = t.parentElement;
    if (!el || seen.has(el) || !t.textContent.trim() || !visible(el)) continue;
    if (el.closest('svg, script, style, noscript, [aria-hidden="true"]')) continue;
    seen.add(el); checked++;
    const s = getComputedStyle(el);
    const fg = parse(s.color); if (!fg) continue;
    const {bg, hasImage} = effectiveBg(el);
    if (hasImage) { overImage++; continue; }
    const fgFlat = fg.a < 1 ? blend(fg, bg) : fg;
    const size = parseFloat(s.fontSize), bold = parseInt(s.fontWeight, 10) >= 700;
    const large = size >= 24 || (bold && size >= 18.66);
    const need = large ? 3.0 : 4.5;
    const r = ratio(fgFlat, bg);
    if (r + 1e-6 < need) failures.push({el: label(el), ratio: Math.round(r * 100) / 100, need});
  }
  out.contrastChecked = checked; out.contrastFailures = failures; out.textOverImage = overImage;

  // Target size: interactive elements smaller than 24x24 (inline links in text are exempt).
  const small = [];
  for (const el of document.querySelectorAll('a[href], button, input:not([type=hidden]), select, textarea, [role=button], [role=slider], [tabindex]:not([tabindex="-1"])')) {
    if (!visible(el)) continue;
    if (el.tagName === 'A' && el.closest('p, li, td, dd, blockquote')) continue;
    let r = el.getBoundingClientRect();
    if (el.tagName === 'INPUT' && (el.type === 'checkbox' || el.type === 'radio')) {
      const lab = el.id && document.querySelector('label[for="' + el.id + '"]') || el.closest('label');
      if (lab) r = lab.getBoundingClientRect();
    }
    if (el.tagName === 'INPUT' && el.closest('label') && getComputedStyle(el).opacity === '0') {
      r = el.closest('label').getBoundingClientRect();
    }
    if (r.width < 24 || r.height < 24) small.push({el: label(el), w: Math.round(r.width), h: Math.round(r.height)});
  }
  out.smallTargets = small;

  // Images and headings.
  out.imgNoAlt = [...document.querySelectorAll('img')].filter((i) => !i.hasAttribute('alt')).map((i) => i.src.slice(-60));
  out.svgImgNoName = [...document.querySelectorAll('svg[role="img"]')]
    .filter((s) => !s.getAttribute('aria-label') && !s.getAttribute('aria-labelledby') && !s.querySelector('title, desc')).length;
  const hs = [...document.querySelectorAll('h1, h2, h3, h4, h5, h6')].filter(visible).map((h) => +h.tagName[1]);
  out.h1Count = hs.filter((h) => h === 1).length;
  out.headingSkips = hs.filter((h, i) => i > 0 && h > hs[i - 1] + 1).length;
  out.headingCount = hs.length;
  return out;
}
"""

MOTION_JS = r"""
() => {
  const moving = [];
  for (const el of document.querySelectorAll('*')) {
    const s = getComputedStyle(el);
    const dur = (v) => Math.max(...v.split(',').map((x) => parseFloat(x) * (x.trim().endsWith('ms') ? 0.001 : 1)));
    const t = dur(s.transitionDuration), a = dur(s.animationDuration);
    if ((t > 0.01 && s.transitionProperty !== 'none') || (a > 0.01 && s.animationName !== 'none')) {
      moving.push({el: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : ''),
                   transition: s.transitionDuration, animation: s.animationName !== 'none' ? s.animationName + ' ' + s.animationDuration + ' x' + s.animationIterationCount : ''});
    }
  }
  return moving;
}
"""


def to_url(target):
    if target.startswith(('http://', 'https://', 'file://')):
        return target
    path = os.path.abspath(target)
    if not os.path.exists(path):
        print(f"SETUP: file not found: {target}")
        sys.exit(2)
    return 'file://' + path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('target', help='HTML file path or URL')
    ap.add_argument('--json', help='write the full report to this file')
    args = ap.parse_args()
    url = to_url(args.target)

    results = []   # (status, check, detail)
    raw = {}

    def add(status, check, detail):
        results.append((status, check, detail))

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()

            def render(width, js=True, scheme='light', motion='no-preference'):
                ctx = browser.new_context(viewport={'width': width, 'height': 900}, java_script_enabled=js,
                                          color_scheme=scheme, reduced_motion=motion)
                page = ctx.new_page()
                errors = []
                page.on('pageerror', lambda e: errors.append(str(e)))
                page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
                page.goto(url, wait_until='load')
                page.wait_for_timeout(600)
                return ctx, page, errors

            for width in (320, 390, 1280):
                ctx, page, errors = render(width)
                data = page.evaluate(PAGE_JS)
                data['errors'] = errors
                raw[f'light_{width}'] = data
                ctx.close()

            ctx, page, _ = render(390, js=False)
            raw['nojs_390'] = page.evaluate(PAGE_JS)
            ctx.close()

            ctx, page, _ = render(390, scheme='dark')
            raw['dark_390'] = page.evaluate(PAGE_JS)
            ctx.close()

            ctx, page, _ = render(390, motion='reduce')
            raw['reduced_motion'] = page.evaluate(MOTION_JS)
            ctx.close()
            browser.close()
    except Exception as e:  # browser missing, navigation failure, etc.
        print(f"SETUP: could not render the page: {e}\n"
              "If Chromium is missing, run: python -m playwright install chromium")
        sys.exit(2)

    m, d = raw['light_390'], raw['light_1280']

    # Overflow
    over = [w for w in (320, 390, 1280) if raw[f'light_{w}']['overflow']]
    add('FAIL' if over else 'PASS', 'Horizontal overflow',
        f"page scrolls sideways at {', '.join(map(str, over))} px" if over else 'none at 320, 390, 1280 px')

    # Font size
    if m['bodyPx'] is None:
        add('WARN', 'Body font size', 'no running-text paragraphs found to measure')
    else:
        status = 'FAIL' if m['bodyPx'] < MIN_BODY_PX_MOBILE else 'PASS'
        add(status, 'Body font size (mobile)', f"{m['bodyPx']}px at 390 px (floor {MIN_BODY_PX_MOBILE}px)")
        longform = d['words'] > LONGFORM_WORDS
        if longform and d['bodyPx'] and d['bodyPx'] < LONGFORM_BODY_PX_DESKTOP:
            add('WARN', 'Body font size (desktop long-form)',
                f"{d['bodyPx']}px for a {d['words']}-word page; default is 18-20px")
        else:
            add('PASS', 'Body font size (desktop)', f"{d['bodyPx']}px, {d['words']} words")

    # Line length
    if d['cplMedian']:
        lo, hi = CPL_RANGE
        ok = lo <= d['cplMedian'] <= hi
        add('PASS' if ok else 'WARN', 'Characters per line (desktop)',
            f"median ~{d['cplMedian']} (default 55-75; warn outside {lo}-{hi})")
    else:
        add('WARN', 'Characters per line (desktop)', 'no long paragraphs to measure')

    # Contrast (light and dark)
    for key, name in (('light_390', 'light'), ('dark_390', 'dark')):
        fails = raw[key]['contrastFailures']
        if fails:
            ex = '; '.join(f"{f['el']} {f['ratio']}:1 (needs {f['need']})" for f in fails[:5])
            add('FAIL', f'Text contrast ({name})', f"{len(fails)} of {raw[key]['contrastChecked']} text elements fail. e.g. {ex}")
        else:
            add('PASS', f'Text contrast ({name})', f"{raw[key]['contrastChecked']} text elements checked")
        if raw[key]['textOverImage']:
            add('WARN', f'Text over images ({name})', f"{raw[key]['textOverImage']} elements sit on background images; check by hand")
    if raw['dark_390']['bodyBg'] in ('rgba(0, 0, 0, 0)', 'transparent'):
        add('WARN', 'Body background', 'body background is transparent; set it explicitly so both themes render')

    # Target size
    small = m['smallTargets']
    if small:
        ex = '; '.join(f"{s['el']} {s['w']}x{s['h']}" for s in small[:5])
        add('FAIL', 'Target size >= 24px', f"{len(small)} targets too small (spacing exceptions need manual review). e.g. {ex}")
    else:
        add('PASS', 'Target size >= 24px', 'all interactive targets at least 24x24 CSS px (inline text links exempt)')

    # JS off
    on_words, off_words = m['words'], raw['nojs_390']['words']
    ratio = off_words / on_words if on_words else 1
    status = 'FAIL' if ratio < JS_OFF_FAIL_RATIO else 'WARN' if ratio < JS_OFF_WARN_RATIO else 'PASS'
    add(status, 'Content with JavaScript off', f"{off_words} of {on_words} words render ({ratio:.0%})")

    # Reduced motion
    moving = raw['reduced_motion']
    looping = [x for x in moving if 'infinite' in x['animation']]
    if looping:
        add('FAIL', 'Reduced motion', f"{len(looping)} looping animations still run, e.g. {looping[0]['el']}")
    elif moving:
        add('WARN', 'Reduced motion', f"{len(moving)} elements keep transitions under reduce, e.g. {moving[0]['el']} {moving[0]['transition']}")
    else:
        add('PASS', 'Reduced motion', 'no transitions or animations when reduced motion is requested')

    # Images
    if m['imgNoAlt']:
        add('FAIL', 'Image alt text', f"{len(m['imgNoAlt'])} <img> without alt")
    else:
        add('PASS', 'Image alt text', 'every <img> has alt (quality is manual)')
    if m['svgImgNoName']:
        add('WARN', 'SVG names', f"{m['svgImgNoName']} svg[role=img] without a title, desc or aria-label")

    # Headings
    hstat = 'PASS'
    notes = [f"{m['headingCount']} headings"]
    if m['h1Count'] != 1:
        hstat = 'WARN'; notes.append(f"{m['h1Count']} h1 (expected 1)")
    if m['headingSkips']:
        hstat = 'WARN'; notes.append(f"{m['headingSkips']} skipped levels")
    add(hstat, 'Heading structure', ', '.join(notes) + '. Whether headings state the point is manual')

    # Console errors
    errs = sorted({e for w in (320, 390, 1280) for e in raw[f'light_{w}']['errors']})
    add('FAIL' if errs else 'PASS', 'Script errors', '; '.join(errs[:3]) if errs else 'none')

    # Report
    width = max(len(c) for _, c, _ in results)
    for status, check, detail in results:
        print(f"{status:<4}  {check:<{width}}  {detail}")
    fails = sum(1 for s, _, _ in results if s == 'FAIL')
    warns = sum(1 for s, _, _ in results if s == 'WARN')
    print(f"\n{fails} FAIL, {warns} WARN, {len(results) - fails - warns} PASS")
    print("Manual: keyboard order, focus visibility, chart and UI contrast (3:1), text over images, "
          "alt-text quality, comprehension with a newcomer, real-phone check, link health.")

    if args.json:
        with open(args.json, 'w') as f:
            json.dump({'url': url, 'results': [dict(status=s, check=c, detail=x) for s, c, x in results], 'raw': raw}, f, indent=1)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
