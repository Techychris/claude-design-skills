#!/usr/bin/env node
// docforge build.js — JSON spec -> polished .docx
// Usage: node build.js <spec.json> <out.docx>
const fs = require("fs");
const path = require("path");
const { Document, Packer, Paragraph, HeadingLevel, PageBreak, LevelFormat, AlignmentType,
  convertInchesToTwip, Header, Footer } = require("docx");
const { getTheme, styles, tw } = require("./themes");
const C = require("./components");

function block(t, b, meta) {
  switch (b.type) {
    case "cover":     return C.cover(t, { ...meta, ...b });
    case "toc":       return C.toc(t);
    case "h1":        return new Paragraph({ heading: HeadingLevel.HEADING_1, children: C.runs(b.text) });
    case "h2":        return new Paragraph({ heading: HeadingLevel.HEADING_2, children: C.runs(b.text) });
    case "h3":        return new Paragraph({ heading: HeadingLevel.HEADING_3, children: C.runs(b.text) });
    case "p":         return C.p(t, b.text);
    case "bullets":   return C.bullets(b.items);
    case "numbered":  return b.items.map((it) => new Paragraph({
                        numbering: { reference: "df-numbered", level: 0 },
                        spacing: { after: tw(3) }, children: C.runs(it) }));
    case "table":     return C.table(t, b);
    case "callout":   return C.callout(t, b);
    case "metrics":   return C.metrics(t, b.items);
    case "kv":        return C.kv(t, b.pairs);
    case "quote":     return C.quote(t, b);
    case "image":     return C.image(t, b);
    case "rule":      return C.rule(t, b.accent ? t.accent : undefined, b.accent ? 18 : 6);
    case "caption":   return new Paragraph({ style: "Caption", children: C.runs(b.text) });
    case "spacer":    return C.spacer(b.pt || 8);
    case "pagebreak": return new Paragraph({ children: [new PageBreak()] });
    case "memohead":  return C.memoHead(t, { ...meta, ...b });
    case "letterhead":return C.letterHead(t, { ...meta, ...b });
    case "signoff":   return C.signoff(t, b);
    default: throw new Error(`Unknown block type "${b.type}". Valid: cover, toc, h1-h3, p, bullets, numbered, table, callout, metrics, kv, quote, image, rule, caption, spacer, pagebreak, memohead, letterhead, signoff`);
  }
}

function build(spec) {
  const t = getTheme(spec.theme || "boardroom");
  const meta = { date: new Date().toLocaleDateString("en-US",
    { year: "numeric", month: "long", day: "numeric" }), ...(spec.meta || {}) };
  const children = [];
  (spec.blocks || []).forEach((b) => {
    const r = block(t, b, meta);
    Array.isArray(r) ? children.push(...r) : children.push(r);
  });
  const chrome = spec.chrome || {}; // { header: bool, footer: bool }
  const hasCover = (spec.blocks || []).some((b) => b.type === "cover");
  const blank = { header: new Header({ children: [] }), footer: new Footer({ children: [] }) };
  return new Document({
    features: { updateFields: true },
    styles: styles(t),
    numbering: { config: [
      { reference: "df-bullets", levels: [
        { level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 400, hanging: 220 } } } },
        { level: 1, format: LevelFormat.BULLET, text: "\u25E6", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 760, hanging: 220 } } } } ] },
      { reference: "df-numbered", levels: [
        { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 400, hanging: 260 } } } } ] },
    ] },
    sections: [{
      properties: { page: { size: { width: C.PAGE_W, height: 15840 },
        margin: { top: C.MARGIN, right: C.MARGIN, bottom: C.MARGIN, left: C.MARGIN } },
        titlePage: hasCover },
      headers: chrome.header ? { default: C.pageHeader(t, meta), ...(hasCover ? { first: blank.header } : {}) }
        : (hasCover ? { first: blank.header } : undefined),
      footers: chrome.footer === false ? (hasCover ? { first: blank.footer } : undefined)
        : { default: C.pageFooter(t, meta), ...(hasCover ? { first: blank.footer } : {}) },
      children,
    }],
  });
}

async function main() {
  const [specPath, outPath] = process.argv.slice(2);
  if (!specPath || !outPath) { console.error("Usage: node build.js <spec.json> <out.docx>"); process.exit(1); }
  const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
  const doc = build(spec);
  const buf = await Packer.toBuffer(doc);
  fs.mkdirSync(path.dirname(path.resolve(outPath)), { recursive: true });
  fs.writeFileSync(outPath, buf);
  console.log(`docforge: wrote ${outPath} (theme: ${spec.theme || "boardroom"}, blocks: ${(spec.blocks || []).length})`);
}
main().catch((e) => { console.error("docforge error:", e.message); process.exit(1); });
