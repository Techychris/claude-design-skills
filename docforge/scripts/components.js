// docforge components.js — reusable document components (docx-js). All take a theme `t`.
const {
  Paragraph, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
  AlignmentType, TableOfContents, Header, Footer, PageNumber, TabStopType, PageBreak,
  VerticalAlign, ImageRun,
} = require("docx");
const fs = require("fs");
const path = require("path");
const { hp, tw } = require("./themes");

const PAGE_W = 12240, MARGIN = 1440, CONTENT_W = PAGE_W - 2 * MARGIN; // US Letter, 1" margins
const NONE = { style: BorderStyle.NONE, size: 0, color: "auto" };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE,
  insideHorizontal: NONE, insideVertical: NONE };

// minimal inline markup: **bold** and *italic*
function runs(text, base = {}) {
  const out = [];
  String(text).split(/(\*\*[^*]+\*\*|\*[^*]+\*)/g).forEach((part) => {
    if (!part) return;
    if (part.startsWith("**")) out.push(new TextRun({ ...base, text: part.slice(2, -2), bold: true }));
    else if (part.startsWith("*")) out.push(new TextRun({ ...base, text: part.slice(1, -1), italics: true }));
    else out.push(new TextRun({ ...base, text: part }));
  });
  return out;
}

const p = (t, text, opts = {}) => new Paragraph({ children: runs(text), ...opts });

function spacer(pt = 8) { return new Paragraph({ spacing: { after: tw(pt) }, children: [] }); }

function rule(t, color, size = 6) {
  return new Paragraph({ spacing: { before: tw(2), after: tw(10) },
    border: { bottom: { style: BorderStyle.SINGLE, size, color: color || t.hairline } }, children: [] });
}

function cover(t, meta) {
  const kids = [];
  if (meta.org) kids.push(new Paragraph({
    shading: { type: ShadingType.CLEAR, fill: t.primary },
    spacing: { before: 0, after: tw(160) },
    children: [new TextRun({ text: `  ${meta.org.toUpperCase()}`, font: t.headingFont,
      size: hp(10), bold: true, color: "FFFFFF" })] }));
  kids.push(new Paragraph({ style: "Title", children: runs(meta.title || "Untitled") }));
  if (meta.subtitle) kids.push(new Paragraph({ style: "Subtitle", children: runs(meta.subtitle) }));
  kids.push(new Paragraph({ spacing: { before: tw(2), after: tw(18) },
    border: { bottom: { style: BorderStyle.SINGLE, size: 30, color: t.accent } }, children: [] }));
  const meta_rows = [["Author", meta.author], ["Date", meta.date], ["Version", meta.version],
    ["Prepared for", meta.for]].filter(([, v]) => v);
  meta_rows.forEach(([k, v]) => kids.push(new Paragraph({ spacing: { after: tw(3) }, children: [
    new TextRun({ text: `${k.toUpperCase()}  `, size: hp(8.5), color: t.muted, bold: true }),
    new TextRun({ text: String(v), size: hp(10.5), color: t.ink }),
  ] })));
  kids.push(new Paragraph({ children: [new PageBreak()] }));
  return kids;
}

function toc(t) {
  return [
    new Paragraph({ style: "TocHeading", children: [new TextRun("Contents")] }),
    new TableOfContents("Right-click → Update Field to populate", { hyperlink: true, headingStyleRange: "1-3" }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

const CALLOUT_COLORS = { note: null, warn: "B45309", success: "1E7B45" }; // note falls back to theme accent
function callout(t, { title, text, variant = "note" }) {
  const bar = CALLOUT_COLORS[variant] || t.accent;
  const kids = [];
  if (title) kids.push(new Paragraph({ spacing: { after: tw(2) }, children: [
    new TextRun({ text: title.toUpperCase(), bold: true, size: hp(9), color: bar, font: t.headingFont })] }));
  kids.push(new Paragraph({ spacing: { after: 0 }, children: runs(text) }));
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    margins: { top: 120, bottom: 120, left: 180, right: 160 },
    borders: { ...noBorders, left: { style: BorderStyle.SINGLE, size: 24, color: bar } },
    rows: [new TableRow({ children: [new TableCell({
      shading: { type: ShadingType.CLEAR, fill: t.faint },
      width: { size: CONTENT_W, type: WidthType.DXA }, children: kids })] })] });
}

function table(t, { headers, rows, widths }) {
  const cols = widths && widths.length === headers.length
    ? widths.map((w) => Math.round((w / widths.reduce((a, b) => a + b, 0)) * CONTENT_W))
    : headers.map(() => Math.round(CONTENT_W / headers.length));
  const cell = (txt, w, opts = {}) => new TableCell({
    width: { size: w, type: WidthType.DXA }, verticalAlign: VerticalAlign.CENTER,
    shading: opts.fill ? { type: ShadingType.CLEAR, fill: opts.fill } : undefined,
    children: [new Paragraph({ spacing: { after: 0 },
      children: runs(txt, opts.run || {}) })] });
  const head = new TableRow({ tableHeader: true, children: headers.map((h, i) =>
    cell(h, cols[i], { fill: t.primary, run: { bold: true, color: "FFFFFF", size: hp(t.body - 0.5), font: t.headingFont } })) });
  const body = rows.map((r, ri) => new TableRow({ children: r.map((c, i) =>
    cell(String(c), cols[i], ri % 2 ? { fill: t.faint } : {})) }));
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: cols,
    margins: { top: 90, bottom: 90, left: 140, right: 140 },
    borders: { ...noBorders,
      bottom: { style: BorderStyle.SINGLE, size: 8, color: t.hairline },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: t.hairline } },
    rows: [head, ...body] });
}

function metrics(t, items) {
  const w = Math.round(CONTENT_W / items.length);
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: items.map(() => w), borders: noBorders,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    rows: [new TableRow({ children: items.map((it) => new TableCell({
      width: { size: w, type: WidthType.DXA }, children: [
        new Paragraph({ spacing: { after: tw(1) }, children: [
          new TextRun({ text: String(it.value), bold: true, size: hp(22), color: t.primary, font: t.headingFont })] }),
        new Paragraph({ spacing: { after: 0 }, children: [
          new TextRun({ text: String(it.label).toUpperCase(), size: hp(8), color: t.muted })] }),
      ] })) })] });
}

function kv(t, pairs) {
  const KW = 2200, VW = CONTENT_W - KW;
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [KW, VW],
    borders: noBorders, margins: { top: 40, bottom: 40, left: 0, right: 100 },
    rows: pairs.map(([k, v]) => new TableRow({ children: [
      new TableCell({ width: { size: KW, type: WidthType.DXA }, children: [new Paragraph({
        spacing: { after: 0 }, children: [new TextRun({ text: String(k).toUpperCase(),
          bold: true, size: hp(8.5), color: t.muted })] })] }),
      new TableCell({ width: { size: VW, type: WidthType.DXA }, children: [new Paragraph({
        spacing: { after: 0 }, children: runs(v) })] }),
    ] })) });
}

function quote(t, { text, by }) {
  const kids = [new Paragraph({ style: "Quote", children: runs(text) })];
  if (by) kids.push(new Paragraph({ alignment: AlignmentType.LEFT, spacing: { before: 0, after: tw(8) },
    indent: { left: 480 }, children: [new TextRun({ text: `- ${by}`, size: hp(9.5), color: t.muted })] }));
  return kids;
}

function pngSize(buf) {
  if (buf.length < 24 || buf.toString("ascii", 12, 16) !== "IHDR") return null;
  return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
}

function jpgSize(buf) {
  let offset = 2; // skip SOI marker (0xFFD8)
  while (offset < buf.length - 8) {
    if (buf[offset] !== 0xff) { offset += 1; continue; }
    const marker = buf[offset + 1];
    if (marker >= 0xc0 && marker <= 0xc3) {
      return { height: buf.readUInt16BE(offset + 5), width: buf.readUInt16BE(offset + 7) };
    }
    offset += 2 + buf.readUInt16BE(offset + 2);
  }
  return null;
}

const IMG_DPI = 96;
const IMG_MAX_HEIGHT_IN = 8;

// Embeds a PNG or JPG (e.g. a diagram-forge PNG), scaled to fit the content
// width, with a height cap so an unusually tall diagram never overruns the
// page. Dimensions are read straight from the file bytes, so no image
// library is needed at build time beyond what docx-js already requires.
function image(t, { src, widthIn, caption }) {
  const abs = path.resolve(src);
  const buf = fs.readFileSync(abs);
  const ext = path.extname(abs).toLowerCase();
  const type = ext === ".png" ? "png" : (ext === ".jpg" || ext === ".jpeg") ? "jpg" : null;
  if (!type) throw new Error(`image block: unsupported file type "${ext}" for ${src} (use .png or .jpg)`);
  const dims = type === "png" ? pngSize(buf) : jpgSize(buf);
  if (!dims) throw new Error(`image block: could not read ${type} dimensions from ${src} (file may be corrupt)`);

  const contentIn = CONTENT_W / 1440;
  let wIn = Math.min(widthIn || contentIn, contentIn);
  let hIn = wIn * (dims.height / dims.width);
  if (hIn > IMG_MAX_HEIGHT_IN) { hIn = IMG_MAX_HEIGHT_IN; wIn = hIn * (dims.width / dims.height); }

  const altName = caption || path.basename(src);
  const kids = [new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: caption ? tw(2) : tw(8) },
    children: [new ImageRun({ type, data: buf,
      transformation: { width: Math.round(wIn * IMG_DPI), height: Math.round(hIn * IMG_DPI) },
      altText: { name: altName, description: altName, title: altName } })],
  })];
  if (caption) kids.push(new Paragraph({ style: "Caption", alignment: AlignmentType.CENTER, children: runs(caption) }));
  return kids;
}

function bullets(items, ref = "df-bullets") {
  return items.map((it) => new Paragraph({ numbering: { reference: ref, level: 0 },
    spacing: { after: tw(3) }, children: runs(it) }));
}

function memoHead(t, meta) {
  return [
    new Paragraph({ spacing: { after: tw(4) }, children: [new TextRun({
      text: "MEMORANDUM", font: t.headingFont, bold: true, size: hp(15), color: t.primary })] }),
    rule(t, t.accent, 18),
    kv(t, [["To", meta.to], ["From", meta.from], ["Date", meta.date], ["Re", meta.re]]
      .filter(([, v]) => v)),
    rule(t, t.hairline, 6),
  ];
}

function letterHead(t, meta) {
  const out = [];
  (meta.senderLines || []).forEach((l, i) => out.push(new Paragraph({
    spacing: { after: i === (meta.senderLines.length - 1) ? tw(14) : 0 },
    children: [new TextRun({ text: l, size: hp(t.body - 0.5), color: t.muted })] })));
  out.push(p(t, meta.date || "", { spacing: { after: tw(14) } }));
  (meta.recipientLines || []).forEach((l, i) => out.push(new Paragraph({
    spacing: { after: i === (meta.recipientLines.length - 1) ? tw(14) : 0 }, children: runs(l) })));
  return out;
}

function signoff(t, { closing = "Sincerely,", name, title }) {
  const out = [p(t, closing, { spacing: { before: tw(10), after: tw(28) } })];
  if (name) out.push(new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: name, bold: true })] }));
  if (title) out.push(new Paragraph({ spacing: { after: 0 }, children: [
    new TextRun({ text: title, size: hp(t.body - 0.5), color: t.muted })] }));
  return out;
}

function pageHeader(t, meta) {
  return new Header({ children: [new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: t.hairline } },
    spacing: { after: tw(2) },
    children: [new TextRun({ text: meta.title || "", size: hp(8.5), color: t.muted, font: t.headingFont })] })] });
}

function pageFooter(t, meta) {
  return new Footer({ children: [new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
    spacing: { before: tw(2) },
    children: [
      new TextRun({ text: meta.org || "", size: hp(8.5), color: t.muted }),
      new TextRun({ text: "\t", size: hp(8.5) }),
      new TextRun({ children: ["Page ", PageNumber.CURRENT, " of ", PageNumber.TOTAL_PAGES],
        size: hp(8.5), color: t.muted }),
    ] })] });
}

module.exports = { PAGE_W, MARGIN, CONTENT_W, runs, p, spacer, rule, cover, toc, callout,
  table, metrics, kv, quote, bullets, image, memoHead, letterHead, signoff, pageHeader, pageFooter };
