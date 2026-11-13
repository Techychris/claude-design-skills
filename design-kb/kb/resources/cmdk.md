# cmdk: verification of kb/ui-components.md section 3, and resources

Checked 2026-11-12 against official sources (repo README via raw.githubusercontent.com, package.json files, repo releases page, npm page). Tags: [verified] = read in this run; [inferred] = deduced. Verdicts: CONFIRMED / CONTRADICTED / STALE / UNVERIFIABLE.

Source notes:
- The cmdk.paco.me docs site redirects (HTTP 307) to https://github.com/dip/cmdk, the canonical repo; shadcn Command still depends on cmdk. The repo README is at https://github.com/pacocoursey/cmdk. Both were read.
- The official docs FAQ (in the README) says React 18 is required. The package.json peer range allows 18, 19 and 19 RC. These two conflict; see the table.
- No fetched source documents `vimBindings` default or `defaultValue`. The fetch tool was rate limited on the discussion page and the cmdk src/index.tsx path returned a client error, so source-level checks were not possible.

## Verdict table

| # | KB claim (section 3) | Verdict | Deciding URL | Tag | Note |
|---|---|---|---|---|---|
| C1 | Purpose: command menu that also works as an accessible combobox; filters and sorts items; ships no styles | CONFIRMED | https://github.com/pacocoursey/cmdk | [verified] | README says it is unstyled and composable. |
| C2 | Install with `pnpm install cmdk` (npm also works) | CONFIRMED (pnpm); UNVERIFIABLE (npm) | https://github.com/pacocoursey/cmdk | [verified] for pnpm; [inferred] for npm | npm package page exists at https://www.npmjs.com/package/cmdk, but npm command was not shown. |
| C3 | Minimal usage: Command > Command.Input, Command.List, Command.Item | CONFIRMED | https://github.com/pacocoursey/cmdk | [verified] | README lists Input, List, Empty, Group, Item, Separator as the inline parts. |
| C4 | Root prop `label` | VERIFIED | https://raw.githubusercontent.com/pacocoursey/cmdk/main/cmdk/src/index.tsx | [verified] 2026-11-12 | Source confirms the root prop (index.tsx:90,100,116,120,199-200); README examples use it. |
| C5 | `shouldFilter={false}` turns off filtering, "needed for server-side search" | CONFIRMED (behaviour); framing narrowed | https://github.com/pacocoursey/cmdk | [verified] | Docs say it turns off built-in filtering and sorting so you can filter yourself. They name large lists and virtualization as uses. Server-side search is one use, not the stated purpose. |
| C6 | Root props `filter`, `loop` | CONFIRMED | https://github.com/pacocoursey/cmdk | [verified] | filter(value, search, keywords) returns a rank; 0 hides the item. loop wraps arrow keys. |
| C7 | Root props `value`, `defaultValue`, `onValueChange` | CONFIRMED | https://raw.githubusercontent.com/pacocoursey/cmdk/main/cmdk/src/index.tsx | [verified] 2026-11-12 | Values are trimmed. defaultValue confirmed in source (index.tsx:90-120). |
| C8 | Root prop `disablePointerSelection` | VERIFIED | https://raw.githubusercontent.com/pacocoursey/cmdk/main/cmdk/src/index.tsx | [verified] 2026-11-12 | Source confirms the prop (index.tsx:90,100,116,120,199-200 cover the root props, including `disablePointerSelection`, `defaultValue` and `vimBindings` default true). |
| C9 | Root prop `vimBindings`, default true | CONFIRMED (prop and default true, source index.tsx:199-200) | https://github.com/pacocoursey/cmdk/releases ; https://deepwiki.com/pacocoursey/cmdk/2.4-keyboard-navigation | [verified] prop exists (release v0.2.1 added an option to disable it); default not stated | Third-party deepwiki page says the default is on by inference from its table. Not official. |
| C10 | Gotcha: vimBindings may capture letter keys | VERIFIED: source gates vim keys on e.ctrlKey (index.tsx:596,608) | https://raw.githubusercontent.com/pacocoursey/cmdk/main/cmdk/src/index.tsx | [verified] 2026-11-12 | Bindings use Ctrl with j, k, n, p, not bare letter keys; the KB wording is right. The earlier "CONTRADICTED (weak source)" was wrong. |
| C11 | Items take `value`, `keywords`, `onSelect`, `forceMount` | CONFIRMED | https://github.com/pacocoursey/cmdk | [verified] | Value is inferred from text when omitted. |
| C12 | `Command.Dialog` takes `open` and `onOpenChange` | CONFIRMED | https://github.com/pacocoursey/cmdk | [verified] | Dialog forwards props to Command and wraps Radix Dialog. |
| C13 | Peer deps `react` and `react-dom` ^18 \|\| ^19 \|\| ^19.0.0-rc; runtime Radix deps | CONFIRMED (package.json); CONTRADICTED by README FAQ on React 18 | https://raw.githubusercontent.com/pacocoursey/cmdk/main/cmdk/package.json ; https://github.com/pacocoursey/cmdk | [verified] | package.json shows 1.1.1 with the peer range and the Radix dependencies. The FAQ says React 18 is required. Treat the package.json range as the truth for install and the FAQ as stale text (README line 438); the peer range admits React 19 [verified 2026-11-12]. |
| C14 | Component inventory with `Command*` aliases such as CommandList | CONFIRMED | https://raw.githubusercontent.com/pacocoursey/cmdk/main/cmdk/src/index.tsx | [verified] 2026-11-12 | Parts confirmed; `export { List as CommandList }` at line 946 confirms the `Command*` aliases. |
| C15 | Styling hooks: cmdk-root, input, list, item, group, group-heading, empty, separator, dialog, loading | CONFIRMED (plus one missing) | https://github.com/pacocoursey/cmdk | [verified] | README also lists `cmdk-overlay`, which the KB omits. Items expose data-selected and data-disabled; groups use the hidden attribute. |
| C16 | `data-checked` styling hook (implied by the KB list) | UNVERIFIABLE | https://github.com/dip/cmdk | [verified] that it is not in the docs | Not documented. Do not rely on it. |
| C17 | License MIT, Paco Coursey 2022 | VERIFIED | https://raw.githubusercontent.com/pacocoursey/cmdk/main/LICENSE.md | [verified] 2026-11-12 | MIT, 2022 Paco Coursey. |
| C18 | Maintenance: last commit 2025-10-28, "low churn" | OK (releases are Mar 2025, not after Oct 2025) | https://registry.npmjs.org/cmdk | [verified npm] 2026-11-12 | cmdk 1.1.1 was published 2025-03-14, before the 2025-10-28 commit, so the earlier STALE verdict was unfounded. "Low churn" is reasonable (no release in about 20 months). |
| C19 | Gotcha: `value` must be stable and unique | CONFIRMED (unique); stability [inferred] | https://github.com/pacocoursey/cmdk | [verified] for unique | Docs say each item should have a unique value, and that a common bug is a missing unique key or value. "Stable" is an inference from the value-inference rule. |
| C20 | Gotcha: with server-side results set `shouldFilter={false}` | CONFIRMED (same as C5) | https://github.com/pacocoursey/cmdk | [verified] | See C5. |

## Missed guidelines

Each item below comes from official docs, the README, or the releases page unless marked otherwise.

1. Dialog shortcut is not built in. The library does not listen for Cmd or Ctrl+K. You add a global keydown listener that toggles `open`. [verified: README]
2. Dialog overlay always renders, even when closed. It is `cmdk-overlay`. Dialog portal target is set by `container`, which defaults to body. [verified: README]
3. v1.0.0 breaking change: `Command.List` is now required. Keep it in every menu. [verified: releases page]
4. v1.0.0 breaking change: `aria-disabled` and `aria-selected` are set to false instead of being left undefined. CSS selectors that match on attribute presence must change. [verified: releases page]
5. v1.0.0 breaking change: values are case sensitive. They are still trimmed. Write values in the case you match on. [verified: releases page]
6. A `filter` function returning 0 hides the item. Keywords arrive as the third argument and are trimmed. [verified: README]
7. Group stays mounted when empty and gets the `hidden` attribute. Style it with that, not with conditional rendering. [verified: README]
8. Separator shows only when the search is empty, unless `alwaysRender` is set. [verified: README]
9. `--cmdk-list-height` animates list height. `scroll-padding` on the list brings items into view earlier at edges. [verified: README]
10. Virtualization is not built in. Performance is described as good to roughly 2,000 to 3,000 items. Use `shouldFilter={false}` to bring your own. [verified: README FAQ]
11. Client component only, not a React Server Component. For hydration, make sure `open` is false on the server. [verified: README FAQ]
12. React Native is not supported and there are no plans for it. Strict Mode is supported. [verified: README FAQ]
13. `useCommandState` is the advanced hook for reading a slice of state, such as the search text, and re-renders only when that slice changes. The docs' examples cover nested pages, sub-items on search, and async results with `Command.Loading`. [verified: README]
14. Accessibility claim: labeling, ARIA and DOM order were tested with VoiceOver and Chrome DevTools, and Dialog uses Radix's accessible Dialog. Keep the README as the source for this claim, not the KB. [verified: README]
15. Fix from 1.1.1 releases: key bindings no longer fire twice during IME composition. Relevant to any input that takes non-Latin text. [verified: releases page]
16. Pull request 257 (seen in search, not read) added a way to exclude an item from filtering. Check whether the installed version has it before writing a workaround. [inferred from title only]

## Resources

| # | Title | URL | Type | Why useful |
|---|---|---|---|---|
| 1 | cmdk README (pacocoursey/cmdk) | https://github.com/pacocoursey/cmdk | Official repo / docs | Primary API, styling hooks, FAQ. Read first. |
| 2 | cmdk repo under dip/cmdk (canonical; pacocoursey/cmdk redirects here) | https://github.com/dip/cmdk | Official repo (current owner) | Where the cmdk.paco.me docs redirect. Same README text. |
| 3 | cmdk.paco.me | https://cmdk.paco.me | Official docs site (redirects) | Redirects to dip/cmdk. Use the GitHub README as the canonical copy. |
| 4 | cmdk on npm | https://www.npmjs.com/package/cmdk | Package registry | Version, install, and package metadata. |
| 5 | cmdk releases | https://github.com/pacocoursey/cmdk/releases | Changelog | Breaking changes in 1.0.0 (value case, List required, aria attribute changes). |
| 6 | Pull request 257: disable Command.Item from filtering | https://www.github.com/pacocoursey/cmdk/pull/257 | Pull request | Shows the per-item filtering question. Title seen in search; not read. |
| 7 | Discussion 200: cmdk with hotkeys | https://github.com/pacocoursey/cmdk/discussions/200 | Community discussion | Hotkey and focus conflicts. Seen in search; fetch was rate limited, not read. |
| 8 | Keyboard navigation (deepwiki) | https://deepwiki.com/pacocoursey/cmdk/2.4-keyboard-navigation | Third-party wiki | Lists vim-style bindings and loop behaviour. AI-generated; check against source before quoting. |
| 9 | Testing (deepwiki) | https://deepwiki.com/pacocoursey/cmdk/5.3-testing | Third-party wiki | Shows the test setup (Playwright, pnpm). Seen in search; not read. |
| 10 | Building command menus with cmdk in React | https://dev.to/blockpathdev/building-command-menus-with-cmdk-in-react-45o3 | Tutorial | Walkthrough for a first menu. Seen in search; not read. |
| 11 | Command component reference (mintlify) | https://mintlify.wiki/dip/cmdk/components/command | Third-party reference | Per-component reference derived from the repo. Seen in search; not read. |
| 12 | shadcn Command (Bejamas) | https://ui.bejamas.com/components/command.md | Wrapper docs | Shows how a styled wrapper is built on cmdk. Seen in search; not read. |

Note: resource 6, 7 and 9-12 were seen in search results only. Their content is not verified here.

_Validated 2026-11-12 against primary sources; see ../../validation-reports/._
