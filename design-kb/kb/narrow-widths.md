# Narrow widths: phones and foldable cover screens

Added 2026-11-13 after a demo run. A billing settings screen built from the `interface-design` skill passed its checks at 1440 and 390 px, then showed uneven buttons on an iPhone Duo cover screen. This file records the device facts, the defects and the rules that came out of it.

Tags: `[verified]` = read on the cited page or measured this run. `[estimated]` = arithmetic or inference. `[standard]` = W3C spec. `[convention]` = practitioner rule with no research behind it.

## iPhone Duo display facts

| Display | Size | Pixels | Density | Points |
|---|---|---|---|---|
| Outer (cover) | 5.4 in | 1398 x 2034 | 460 ppi | Not published by Apple. 466 x 678 at 3x [estimated] |
| Inner | 7.6 in | 1878 x 2670 | 430 ppi | Not published by Apple. 626 x 890 by dividing the panel by 3, or 669 x 951 inferred from the App Store screenshot size (2007 x 2853); the two disagree [estimated] |

- Pixels, sizes and densities are from Apple's spec page [verified 2026-11-13: apple.com/sg/iphone-duo/specs].
- The point sizes come from one developer blog (blakecrosley.com, "iPhone Duo for Developers"), which says they are arithmetic, not a spec. A screen-size reference site lists both viewports as "not published" (data checked 31 October 2026) [verified that the pages say this].
- The same blog reports that the outer display is compact width and the inner display is regular in both dimensions, citing Apple's Tech Talks. The talks themselves were not opened [estimated].
- Design consequence: the cover screen is wider than a current iPhone (about 466 vs 402 points) but still sits under a 600 px phone breakpoint, so it gets the phone layout with more room per row. Test at 466 px as well as 320 and 390.

## What went wrong in the demo (measured in headless Chromium)

| Defect | Measured | Cause |
|---|---|---|
| Primary button narrower than its neighbours | 300 vs 308 px at 320-360 wide | One card had more padding than the others at the phone breakpoint |
| Destructive button content-sized, label off-centre | 114 px wide while others were full width | Never set to full width; a layout rule named `.danger` also applied to `.btn.danger` |
| Peer buttons with ragged widths | 95, 104, 106, 110 px, at 12 px text vs 14 px elsewhere | Content-sized buttons left to wrap |
| Page wider than the viewport | 372 px at 320 wide, Download link clipped | A table that cannot shrink, hidden by `overflow-x: hidden` on `body` |
| Focus lost | `document.activeElement` was `BODY` after confirming a dialog and after Retry | The focused control was removed and focus was not moved |
| Error not announced | Inline email error shown on blur only | No live-region announcement |
| Skeleton ignores reduced motion | 1.4 s infinite pulse outside the reduced-motion block | Loader left out of the block |

After the fix, at 390, 466 and 599 px every action button measured the same width per row role (326, 402 and 535 px) at 44 px high and 14 px text, and the four peer buttons were equal (159, 197 and 264 px) [verified by measurement]. Not tested on a physical iPhone Duo.

## Rules

- **Reflow** [standard]: WCAG 2.2 SC 1.4.10 (AA) requires no two-dimensional scrolling at 320 CSS px wide. Use `minmax(0, 1fr)` columns, give a table that cannot shrink its own `overflow-x: auto` region, and do not hide overflow on `body`.
- **Target size** [standard]: 24 x 24 CSS px is the AA minimum (SC 2.5.8); 44 x 44 is AAA (SC 2.5.5). Uniformity between buttons is not a WCAG requirement.
- **One button size per role** [convention]: stacked action buttons share width, height, text size and inset. Cards on one screen share one padding value at the phone breakpoint.
- **Peer buttons in equal columns** [convention]: use a grid, not content-sized buttons that wrap.
- **Destructive differs by colour, not size** [convention].
- **Scope layout classes** [convention]: a container and a component modifier must not share a class name.
- **Focus has a destination** [standard, SC 2.4.3 Focus Order]: after an action removes the focused control, move focus to a named element.
- **Announce errors** [standard, SC 4.1.3 Status Messages].
- **Looping loaders obey `prefers-reduced-motion`** [convention; SC 2.3.3 is AAA and covers interaction-triggered motion].
- **Measure, do not eyeball** [convention]: at 320, 390 and 466 px list every button's width, height and font size, and compare `scrollWidth` with the viewport.

## Slop that survived the build (found 2026-11-13, same screen)

The screen was built with `interface-design`, which had no rule against these, and `unslop` had not been run on it. An unslop polish pass removed them; the dialog, email error and four table states still worked afterwards, and buttons stayed uniform at 466 px [verified by measurement].

| Sign | Where | Fix |
|---|---|---|
| Status pills | "Paid" and "Refunded" as tinted, fully rounded badges | Plain text with a small status dot |
| Decorative tile | Blue italic 700-weight "VISA" tile beside "Visa ending 4417" | Removed; the text already says it |
| Uppercase tracked labels | Eyebrow, plan label, table headers (`letter-spacing: .06em`) | Sentence case, zero tracking |
| Heavy weights | 600 on headings, buttons and links; 700 on the tile | 500; hierarchy from size and colour |
| Trailing periods | One-sentence captions and the error message | Removed |
| Colour literals | `#fff` and three other hex values outside the token block | Tokens |
| Loader ignores reduced motion | Skeleton pulse | Stops under `prefers-reduced-motion` |

Rules, all `[convention]` (from the unslop skill by Damir Sokolovsky, @heydamir, github.com/heydamir/unslop, CC BY 4.0; no research base was checked for them):
- Status, counts and plan names are quiet text, not pills. A pill shape stays only where the control is one by nature, such as a switch.
- No uppercase tracked labels; sentence case everywhere.
- No tile, chip or tag that repeats the text beside it.
- Weights 400 and 500, 600 for rare emphasis; no italic for emphasis.
- Labels, buttons, captions and one-sentence messages end without a period.
- Every colour is a token.
- No looping motion on things that are not live.

Process lesson: a build skill and a de-slop skill are separate steps. Passing one says nothing about the other, so a build is not finished until the slop search has run (uppercase, tracked labels, pill radii, 700+ weights, italic, colour literals, infinite animations).

## Lesson about the checks

The screen scored 80.0 against a threshold of 80 in a rubric review, and passed its mechanical gates, before the uneven buttons were reported. Both the gates and the rubric tested minimum size and never compared buttons with each other, and neither tested 320 or 466 px. A check for a minimum does not catch inconsistency. The score was not re-run after the fix.

Sources: apple.com/sg/iphone-duo/specs/ ; blakecrosley.com/blog/iphone-duo-for-developers ; madegooddesigns.com/tools/screen-sizes/ ; w3.org/TR/WCAG22 (SC numbers as recorded in `kb/ux-mastery.md` section on viewports and in `validation-reports/`).
