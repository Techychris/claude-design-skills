// probe.js: generic behavior probe for a single-file HTML app. Catches what gate.js cannot see.
// Usage: NODE_PATH=<dir with playwright> node probe.js <file.html> [--json out.json]
// Checks: document basics, tab order, reflow at 320/390/720, reduced motion, accessible names,
// focus loss after activating each control (repeated until it disables), dialog open/Escape/focus return,
// focus loss inside dialogs, empty state after a no-match search, console errors.
// Exit 1 if any FAIL. Every row is something the script observed, never inferred.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const target = process.argv[2];
if (!target) { console.error('Usage: node probe.js <file.html> [--json out.json]'); process.exit(2); }
const url = /^https?:|^file:/.test(target) ? target : 'file://' + path.resolve(target);
const jIdx = process.argv.indexOf('--json'); const jsonOut = jIdx > 0 ? process.argv[jIdx + 1] : null;
const rows = [];
const add = (area, check, status, detail = '') => rows.push({ area, check, status, detail });

const SEL = 'button, [role=tab], [role=button], a[href], summary';
const desc = (p) => p.evaluate(() => { const e = document.activeElement; return !e || e === document.body ? 'BODY' : e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + ' "' + (e.getAttribute('aria-label') || e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 24) + '"'; });
const label = (e) => (e.getAttribute('aria-label') || e.textContent || e.id || e.tagName).trim().replace(/\s+/g, ' ').slice(0, 28);

(async () => {
  const browser = await chromium.launch();
  const open = async (w = 1440, opts = {}) => { const p = await browser.newPage({ viewport: { width: w, height: 900 }, ...opts }); p.errs = []; p.on('pageerror', (e) => p.errs.push(e.message)); p.on('console', (m) => m.type() === 'error' && p.errs.push(m.text())); await p.goto(url); await p.waitForTimeout(250); return p; };

  // 1. Document basics
  let p = await open();
  const basics = await p.evaluate(() => ({ lang: !!document.documentElement.lang, title: !!document.title.trim(), h1: document.querySelectorAll('h1').length, main: !!document.querySelector('main,[role=main]'), vp: !!document.querySelector('meta[name=viewport]'), posTab: [...document.querySelectorAll('[tabindex]')].filter((e) => +e.getAttribute('tabindex') > 0).length }));
  add('document', 'lang, title, viewport meta', basics.lang && basics.title && basics.vp ? 'PASS' : 'FAIL', JSON.stringify({ lang: basics.lang, title: basics.title, viewport: basics.vp }));
  add('document', 'one h1 and a main landmark', basics.h1 === 1 && basics.main ? 'PASS' : 'FAIL', `h1=${basics.h1} main=${basics.main}`);
  add('document', 'no positive tabindex', basics.posTab === 0 ? 'PASS' : 'FAIL', String(basics.posTab));

  // 2. Names on interactive elements
  const unnamed = await p.evaluate(() => [...document.querySelectorAll('button,a[href],input,select,textarea,[role=tab],[role=button]')].filter((e) => e.offsetParent !== null && !(e.getAttribute('aria-label') || e.getAttribute('aria-labelledby') || (e.labels && e.labels.length) || (e.textContent || '').trim() || e.getAttribute('title'))).map((e) => e.outerHTML.slice(0, 60)));
  add('names', 'every visible control has an accessible name', unnamed.length ? 'FAIL' : 'PASS', unnamed.slice(0, 3).join(' | '));

  // 3. Tab order (first 12 stops) recorded; fail on a trap (same element 3x in a row)
  const stops = []; for (let i = 0; i < 12; i++) { await p.keyboard.press('Tab'); stops.push(await desc(p)); }
  const trap = stops.some((s, i) => i > 1 && s === stops[i - 1] && s === stops[i - 2]);
  add('keyboard', 'tab order (first 12 stops)', trap ? 'FAIL' : 'INFO', stops.join(' > '));
  await p.close();

  // 4. Reflow
  for (const w of [320, 390, 720, 1440]) { p = await open(w); const o = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); add('reflow', `no horizontal page scroll at ${w}px`, o > 1 ? 'FAIL' : 'PASS', o > 1 ? `overflows by ${o}px` : ''); await p.close(); }

  // 5. Reduced motion
  p = await open(1440, { reducedMotion: 'reduce' });
  const slow = await p.evaluate(() => [...document.querySelectorAll('button,a,input,select,[role=tab]')].filter((e) => e.offsetParent !== null && Math.max(...getComputedStyle(e).transitionDuration.split(',').map(parseFloat)) > 0.05).length);
  add('motion', 'transitions shortened under prefers-reduced-motion', slow ? 'FAIL' : 'PASS', slow ? `${slow} controls still >50ms` : '');
  await p.close();

  // 6. Focus loss: activate each control by keyboard, repeat while it stays enabled, watch for BODY
  p = await open();
  const n = await p.$$eval(SEL, (els) => els.filter((e) => e.offsetParent !== null && !e.closest('dialog:not([open])')).length);
  const lost = []; const opened = [];
  for (let k = 0; k < n; k++) {
    const fresh = await open(); const h = (await fresh.$$(SEL)).filter(Boolean);
    const vis = []; for (const el of h) if (await el.isVisible()) vis.push(el);
    const el = vis[k]; if (!el) { await fresh.close(); continue; }
    const name = await el.evaluate(label); const isLink = await el.evaluate((e) => e.tagName === 'A');
    if (isLink) { await fresh.close(); continue; }
    const tag = await el.evaluate((e) => { e.setAttribute('data-probe', 'x'); return e.id ? '#' + e.id : '[data-probe=x]'; });
    for (let r = 0; r < 6; r++) {
      const live = await fresh.$(tag); if (!live) break;
      await live.focus(); await fresh.keyboard.press('Enter'); await fresh.waitForTimeout(120);
      const dlgOpen = await fresh.evaluate(() => !!document.querySelector('dialog[open]'));
      if (dlgOpen) {
        opened.push(name);
        // inside the dialog: each button Enter, each select next option, watch for BODY
        const inner = await fresh.$$('dialog[open] select, dialog[open] button');
        for (const c of inner) { const t = await c.evaluate((e) => e.tagName); const cn = await c.evaluate(label); if (t === 'SELECT') { const nopt = await c.evaluate((e) => e.options.length); await c.focus(); await fresh.keyboard.press('ArrowDown'); await fresh.waitForTimeout(150); const f = await desc(fresh); if (nopt > 1 && f === 'BODY' && (await fresh.evaluate(() => !!document.querySelector('dialog[open]')))) lost.push(`inside dialog opened by "${name}": changing select "${cn}" -> focus on BODY`); break; } }
        await fresh.keyboard.press('Escape'); await fresh.waitForTimeout(150);
        const still = await fresh.evaluate(() => !!document.querySelector('dialog[open]'));
        const back = await desc(fresh);
        if (still) lost.push(`dialog opened by "${name}" did not close on Escape`); else if (back === 'BODY') lost.push(`dialog opened by "${name}" closed but focus did not return (BODY)`);
        break;
      }
      const a = await desc(fresh);
      if (a === 'BODY') { lost.push(`"${name}" pressed ${r + 1}x -> focus on BODY`); break; }
    }
    await fresh.close();
  }
  add('focus', 'focus never drops to BODY after activating a control', lost.length ? 'FAIL' : 'PASS', lost.slice(0, 6).join(' | '));
  add('focus', 'dialogs found and exercised', opened.length ? 'INFO' : 'INFO', opened.length ? [...new Set(opened)].join(', ') : 'none opened by a button');
  await p.close();

  // 7. Empty state after a no-match search
  p = await open(); const s = await p.$('input[type=search], input[placeholder*=earch i], input[aria-label*=earch i]');
  if (s) { await s.fill('zzzqqq'); await p.waitForTimeout(200); const txt = await p.evaluate(() => document.body.innerText); const ok = /\b(no |nothing|none|empty|0 )/i.test(txt); add('states', 'no-match search shows an empty message', ok ? 'PASS' : 'FAIL', ok ? '' : 'no "no/nothing/empty" text after a no-match search'); }
  else add('states', 'no-match search shows an empty message', 'SKIP', 'no search input found');
  add('console', 'no console or page errors on load', p.errs.length ? 'FAIL' : 'PASS', p.errs.slice(0, 2).join(' | '));
  await p.close(); await browser.close();

  for (const r of rows) console.log(`${r.status.padEnd(5)} ${r.area.padEnd(9)} ${r.check}${r.detail ? '  -> ' + r.detail : ''}`);
  const f = rows.filter((r) => r.status === 'FAIL').length;
  console.log(`\n${rows.filter((r) => r.status === 'PASS').length} passed, ${f} failed, ${rows.filter((r) => r.status === 'SKIP').length} skipped`);
  if (jsonOut) fs.writeFileSync(jsonOut, JSON.stringify({ url, rows }, null, 2));
  process.exit(f ? 1 : 0);
})().catch((e) => { console.error('probe error:', e.message); process.exit(2); });
