#!/bin/bash
# docforge hard gates: syntax -> build -> render -> text check -> non-blank page check
#
# Two modes:
#   bash gates.sh                        -> self-test: rebuilds & checks all 5 bundled templates
#   bash gates.sh <spec.json> <out.docx> -> targeted: builds & checks that specific spec/output pair
#                                            (this is the mode SKILL.md's workflow step 4 documents)
set -u

# Resolve any caller-supplied paths to absolute BEFORE we cd into the skill root,
# since relative paths are meant to be relative to the caller's cwd, not this script's.
TARGET_SPEC=""
TARGET_OUT=""
if [ "$#" -ge 2 ]; then
  TARGET_SPEC="$(realpath -m "$1")"
  TARGET_OUT="$(realpath -m "$2")"
fi

cd "$(dirname "$0")/.."
SOFFICE="python3 /mnt/skills/public/docx/scripts/office/soffice.py"
OUT=out; mkdir -p $OUT; FAIL=0

for js in scripts/themes.js scripts/components.js scripts/build.js; do
  node --check "$js" >/dev/null 2>&1 && echo "GATE syntax $js: PASS" || { echo "GATE syntax $js: FAIL"; FAIL=1; }
done

node -e '
const {THEMES}=require("./scripts/themes");
const SAFE=new Set(["Georgia","Cambria","Garamond","Calibri","Segoe UI","Arial","Times New Roman","Consolas","Book Antiqua"]);
let bad=[]; const names=Object.keys(THEMES);
if(names.length<4) bad.push("fewer than 4 themes");
for(const [n,t] of Object.entries(THEMES)) for(const k of ["headingFont","bodyFont","monoFont"])
  if(!SAFE.has(t[k])) bad.push(`${n}.${k}=${t[k]} not Word-safe`);
if(bad.length){console.error("GATE themes: FAIL "+bad.join("; "));process.exit(1)}
console.log(`GATE themes: PASS (${names.length} themes, fonts safe)`);' || FAIL=1

# Pull a handful of short, distinctive text candidates out of a spec so we can
# confirm the rendered PDF actually contains content from THIS document.
expect_for() {
  node -e '
    const path=require("path");
    const specPath=path.resolve(process.argv[1]);
    const s=require(specPath);
    const cands=[s.meta&&s.meta.title, ...(s.blocks||[]).map(b=>b.type==="signoff"&&b.name),
      ...(s.blocks||[]).map(b=>(b.type==="h1"||b.type==="p")&&b.text)].filter(x=>x&&String(x).length>=8);
    console.log(cands.map(c=>String(c).replace(/[*]/g,"").split(/\s+/).slice(0,3).join(" ")).join("\t"));
  ' "$1"
}

# Build one spec -> docx, render it, and run the four hard gates (build/render/text/page)
# against that specific artifact. Used by both modes below.
check_one() {
  local spec="$1" outdoc="$2" label="$3"
  local outdir; outdir="$(dirname "$outdoc")"
  mkdir -p "$outdir"
  local expect; expect="$(expect_for "$spec")"

  if node scripts/build.js "$spec" "$outdoc" >/dev/null 2>&1; then
    echo "GATE build $label: PASS"
  else
    echo "GATE build $label: FAIL"; FAIL=1; return
  fi

  local pdf="${outdoc%.docx}.pdf"
  $SOFFICE --headless --convert-to pdf "$outdoc" --outdir "$outdir" >/dev/null 2>&1
  [ -f "$pdf" ] && echo "GATE render $label: PASS" || { echo "GATE render $label: FAIL"; FAIL=1; return; }

  local txt; txt="$(pdftotext "$pdf" - 2>/dev/null | tr '\n' ' ' | tr -s ' ')"
  local hit=0
  while IFS= read -r c; do [ -n "$c" ] && echo "$txt" | grep -qiF "$c" && hit=1 && break; done < <(echo "$expect" | tr '\t' '\n')
  [ $hit -eq 1 ] && echo "GATE text $label: PASS" || { echo "GATE text $label: FAIL (none of: $expect)"; FAIL=1; }

  local pageprefix="${pdf%.pdf}-page"
  pdftoppm -jpeg -r 80 -f 1 -l 1 "$pdf" "$pageprefix" >/dev/null 2>&1
  local img; img="$(ls "${pageprefix}-1.jpg" 2>/dev/null || ls "${pageprefix}-01.jpg" 2>/dev/null)"
  # Pixel-variance check, not byte size: a legitimately sparse page (e.g. a cover
  # with just a title and org band) can be a small, valid JPEG — byte size alone
  # false-flagged those. A truly blank/white page has near-zero variance regardless
  # of file size, so that's the actual property worth gating on.
  local variance; variance="$(identify -format "%[fx:standard_deviation*100]" "$img" 2>/dev/null || echo 0)"
  awk -v v="$variance" 'BEGIN{exit !(v > 4)}' \
    && echo "GATE page $label: PASS (variance ${variance})" \
    || { echo "GATE page $label: FAIL (variance ${variance} — blank?)"; FAIL=1; }
}

if [ -z "$TARGET_SPEC" ]; then
  # Coverage gate: every block type build.js's switch actually implements must be
  # exercised by at least one bundled template — otherwise the self-test below can
  # report 100% green while a whole block type (e.g. h3, once) silently bit-rots.
  node -e '
    const fs=require("fs");
    const supported=[...fs.readFileSync("scripts/build.js","utf8").matchAll(/case "([a-z0-9]+)":/g)].map(m=>m[1]);
    const tpls=["report","memo","letter","brief","minutes"];
    const used=new Set();
    for(const t of tpls) for(const b of (require(`./templates/${t}.json`).blocks||[])) used.add(b.type);
    const missing=supported.filter(t=>!used.has(t));
    if(missing.length){console.error("GATE coverage: FAIL — never exercised by any template: "+missing.join(", "));process.exit(1)}
    console.log(`GATE coverage: PASS (${supported.length} block types, all exercised)`);
  ' || FAIL=1
fi

if [ -n "$TARGET_SPEC" ]; then
  # Targeted mode: verify the exact document the caller is about to deliver.
  check_one "$TARGET_SPEC" "$TARGET_OUT" "$(basename "$TARGET_OUT" .docx)"
else
  # Self-test mode: regression-check the five bundled templates still build & render.
  for tpl in report memo letter brief minutes; do
    check_one "templates/$tpl.json" "$OUT/$tpl.docx" "$tpl"
  done
  grep -q "PAGE" <(unzip -p $OUT/report.docx word/footer1.xml 2>/dev/null) && echo "GATE fields report-footer: PASS" || { echo "GATE fields report-footer: FAIL"; FAIL=1; }
fi

exit $FAIL
