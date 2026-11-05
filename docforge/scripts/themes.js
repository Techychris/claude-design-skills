// docforge themes.js — design tokens + Word style factory (docx-js)
// Tokens only use Word-safe fonts. Sizes in pt here; converted to half-points in styles().

const THEMES = {
  boardroom: { // authoritative corporate: navy + rust, sans headings / serif body
    headingFont: "Segoe UI", bodyFont: "Georgia", monoFont: "Consolas",
    ink: "1A1A1A", primary: "1F3864", accent: "C45911", muted: "595959",
    faint: "F2F5FA", hairline: "D9D9D9",
    body: 10.5, h1: 19, h2: 14, h3: 11.5, title: 30, subtitle: 13, line: 1.24,
  },
  editorial: { // literary: oxblood + brass, serif throughout
    headingFont: "Garamond", bodyFont: "Georgia", monoFont: "Consolas",
    ink: "21201E", primary: "5B2333", accent: "B08D57", muted: "6B645C",
    faint: "F7F3EE", hairline: "E0D8CC",
    body: 11, h1: 21, h2: 15, h3: 12, title: 32, subtitle: 13.5, line: 1.3,
  },
  slate: { // modern minimal: charcoal + teal, sans throughout
    headingFont: "Segoe UI", bodyFont: "Segoe UI", monoFont: "Consolas",
    ink: "202124", primary: "2F3437", accent: "0F766E", muted: "5F6368",
    faint: "F1F3F4", hairline: "DADCE0",
    body: 10.5, h1: 18, h2: 13.5, h3: 11, title: 28, subtitle: 12.5, line: 1.2,
  },
  meridian: { // classic Word pairing done right: steel blue + coral
    headingFont: "Cambria", bodyFont: "Calibri", monoFont: "Consolas",
    ink: "262626", primary: "205072", accent: "D1495B", muted: "595959",
    faint: "EEF4F8", hairline: "D6E1EA",
    body: 11, h1: 19, h2: 14, h3: 11.5, title: 30, subtitle: 13, line: 1.15,
  },
};

const hp = (pt) => Math.round(pt * 2);          // half-points
const tw = (pt) => Math.round(pt * 20);         // twips from points
const lineOf = (t) => Math.round(t.line * 240); // docx line units (240 = single)

function styles(t) {
  const heading = (id, name, size, color, before, after, outlineLevel) => ({
    id, name, basedOn: "Normal", next: "Normal", quickFormat: true,
    run: { font: t.headingFont, size: hp(size), bold: true, color },
    paragraph: { spacing: { before: tw(before), after: tw(after), line: lineOf(t) },
      keepNext: true, keepLines: true, outlineLevel },
  });
  return {
    default: { document: { run: { font: t.bodyFont, size: hp(t.body), color: t.ink },
      paragraph: { spacing: { after: tw(7), line: lineOf(t) } } } },
    paragraphStyles: [
      heading("Heading1", "Heading 1", t.h1, t.primary, 16, 6, 0),
      heading("Heading2", "Heading 2", t.h2, t.primary, 12, 4, 1),
      heading("Heading3", "Heading 3", t.h3, t.accent, 10, 3, 2),
      { id: "Title", name: "Title", basedOn: "Normal", next: "Normal",
        run: { font: t.headingFont, size: hp(t.title), bold: true, color: t.primary },
        paragraph: { spacing: { before: 0, after: tw(6), line: 240 } } },
      { id: "Subtitle", name: "Subtitle", basedOn: "Normal", next: "Normal",
        run: { font: t.bodyFont, size: hp(t.subtitle), color: t.muted, italics: true },
        paragraph: { spacing: { after: tw(12) } } },
      { id: "Quote", name: "Quote", basedOn: "Normal", next: "Normal",
        run: { italics: true, color: t.ink, size: hp(t.body + 0.5) },
        paragraph: { indent: { left: 480 }, spacing: { before: tw(8), after: tw(8) },
          border: { left: { style: "single", size: 18, color: t.accent, space: 12 } } } },
      { id: "Caption", name: "Caption", basedOn: "Normal", next: "Normal",
        run: { size: hp(9), color: t.muted, italics: true },
        paragraph: { spacing: { before: tw(3), after: tw(10) } } },
      { id: "TocHeading", name: "TOC Heading", basedOn: "Normal", next: "Normal",
        run: { font: t.headingFont, size: hp(t.h1), bold: true, color: t.primary },
        paragraph: { spacing: { before: tw(4), after: tw(8) } } }, // no outlineLevel: keeps itself out of the TOC
    ],
  };
}

function getTheme(name) {
  const t = THEMES[name];
  if (!t) throw new Error(`Unknown theme "${name}". Available: ${Object.keys(THEMES).join(", ")}`);
  return t;
}

module.exports = { THEMES, getTheme, styles, hp, tw };
