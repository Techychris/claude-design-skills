# Per-library guideline verification and resources

Run 2026-11-12 by five Haiku subagents, one batch per library group. Each checked the rules in `kb/ui-core.md` and `kb/ui-components.md` against official docs, READMEs, package manifests and raw source, then collected resources. Pages were read through summarising fetches, so wording is paraphrased. Corrections that held up are applied in those two files (see their "Guideline check and resources" sections).

| File | Library | Rules checked | Resources | Main finding |
|---|---|---|---|---|
| `shadcn.md` | shadcn/ui | 48 | 12 | Two rule examples contradict the docs (InputGroupButton, Button as link); most style rules are skill policy, not docs. |
| `base-ui.md` | Base UI | 33 | 14 | Direction does have a counterpart (DirectionProvider); public docs list 37 components, not 39. |
| `radix.md` | Radix Primitives | 25 | 13 | asChild basics and data-state confirmed; Slot merge details and the philosophy page unverifiable. |
| `sonner.md` | Sonner | 23 | 10 | Mostly confirmed; adds 4000 ms default, aria-live region, Alt+T hotkey, shared listRef caveat. |
| `vaul.md` | Vaul | 25 | 10 | `snapPoints` does not require `fadeFromIndex` (rechecked in source); docs site blocks fetching. |
| `cmdk.md` | cmdk | 20 | 12 | vimBindings need Ctrl (rechecked in source); README FAQ conflicts with the React peer range. |
| `number-flow.md` | NumberFlow | 19 | 12 | Props and reduced-motion default confirmed; many styling, CSP and formatting limits were missing. |
| `magic-ui.md` | Magic UI | 15 | 12 | Keyframes rule is not universal; install flow and MIT confirmed. |
| `21st-dev.md` | 21st.dev | 14 | 11 | Publishing states and CSS-variable guidance are out of date; CLI and publishing rules were missing. |
| `rareui.md` | RareUI | 23 | 11 | "Requires React 19 and Next 16" overstated; CLI flags and contributor rules were missing. |
| `ui-sdk.md` | UI SDK (Vercel, beta) | n/a (new overview, not a rule check) | 4 | Agent-oriented behavior library, Apache-2.0, React 19+, beta; accessibility claimed but not audited; canonical repo path unconfirmed. Written by the main session, not a Haiku run. |

## How to read these files

- Verdicts: CONFIRMED, CONTRADICTED, STALE, UNVERIFIABLE. UNVERIFIABLE usually means the docs are silent, not that the rule is wrong.
- Resource entries marked "seen in search, not read" were not opened; treat them as leads. Third-party mirrors (mintlify, deepwiki, context7, tessl) are labelled and are not authoritative.
- Two claims were rechecked by the main session against the cloned source and held: Vaul's `snapPoints`/`fadeFromIndex` types and cmdk's Ctrl-gated vim bindings.
- `ui-sdk.md` has no verdict table: the library was not in `kb/ui-core.md` or `kb/ui-components.md`, so there were no existing rules to check.

## Not verified

- Repo last-commit dates and archived status (GitHub API blocked).
- vaul.emilkowal.ski and 21st.dev `/r/` registry URLs (robots-blocked for the fetch tool).
- shadcn dark-mode setup (docs page is a stub) and Slot merge order in Radix.
- Svelte and Vue wrapper versions for NumberFlow; RareUI's `.test` entries, lazy variants and registry JSON.
- UI SDK: adapter versions, last-commit date, accessibility behavior, bundle size.
