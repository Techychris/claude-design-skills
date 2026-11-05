#!/usr/bin/env node
// docforge extract_text.js -- pull prose-bearing fields out of a spec, one per
// line, for scanning by remove-ai-tells' scan_tells.py. Deliberately excludes
// table cells, kv pairs, and metrics values: those are data fragments, not
// prose, and including them would add sentence-splitting noise without
// catching anything the mechanical checks are actually meant to catch.
//
// Usage: node extract_text.js <spec.json>
//        node extract_text.js myspec.json | python3 /mnt/skills/user/remove-ai-tells/scripts/scan_tells.py -
const fs = require("fs");

const specPath = process.argv[2];
if (!specPath) { console.error("Usage: node extract_text.js <spec.json>"); process.exit(1); }
const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));

const strip = (s) => String(s).replace(/\*\*([^*]+)\*\*/g, "$1").replace(/\*([^*]+)\*/g, "$1");
const out = [];

if (spec.meta) {
  ["title", "subtitle", "author", "for"].forEach((k) => { if (spec.meta[k]) out.push(strip(spec.meta[k])); });
}

(spec.blocks || []).forEach((b) => {
  switch (b.type) {
    case "h1": case "h2": case "h3": case "p": case "caption":
      if (b.text) out.push(strip(b.text));
      break;
    case "bullets": case "numbered":
      (b.items || []).forEach((it) => out.push(strip(it)));
      break;
    case "callout":
      if (b.title) out.push(strip(b.title));
      if (b.text) out.push(strip(b.text));
      break;
    case "quote":
      if (b.text) out.push(strip(b.text));
      break;
    default:
      break; // table/kv/metrics/image/etc.: data fragments, not prose -- skip
  }
});

console.log(out.filter(Boolean).join("\n\n"));
