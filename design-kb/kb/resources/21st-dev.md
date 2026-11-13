# 21st.dev (serafimcloud/21st): verification and resources

Checked 2026-11-12 against official sources: 21st.dev, the GitHub repo (README, LICENSE, package.json), and the official help centre at help.21st.dev (publishing and CLI pages). Pages were read through WebFetch summaries, so statements are paraphrased. https://21st.dev/r/... registry URLs are disallowed by robots.txt for this client, so the registry JSON was not read. Tags: [verified] = read in this run; [inferred] = deduced.

Scope: KB `kb/ui-components.md`, section 6 (serafimcloud/21st).

## Verdict table

| # | KB rule (section) | Verdict | Deciding URL | Note |
|---|---|---|---|---|
| 1 | Install a component with the shadcn CLI using a 21st.dev `/r/<owner>/<component>` URL (6, Install) | CONFIRMED (form) | https://github.com/serafimcloud/21st (README) ; https://help.21st.dev/cli/find | README uses npx with a /r/shadcn/accordion URL. The `21st add <user>/<slug>` command runs `shadcn add` against the 21st registry [verified]. The KB's pnpm dlx form is equivalent. The registry endpoint itself was not read (robots) |
| 2 | 21st.dev is a community registry of React, Tailwind and Radix components installed through shadcn (6, Purpose) | OUTDATED | https://21st.dev ; https://github.com/serafimcloud/21st | Repo description: "largest marketplace of shadcn/ui-based React Tailwind components, blocks and hooks". Homepage (title "12,000+ Crafted UI"): components, 987 themes, 299 templates, 376 shaders, icons, video; paid items and a pricing page exist; "Radix" is not stated anywhere read. Current framing: marketplace of shadcn/ui-based React and Tailwind components, themes, templates and icons (free and paid), installable via `@21st-dev/cli` or by pasting prompts into an agent. Homepage now frames install as pasting a component's prompt into an AI agent (Claude Code, Codex, Lovable), with MCP and CLI routes. It does not mention Radix or Next. README still describes shadcn-style installs [verified] |
| 3 | Components use shadcn CSS variables such as `hsl(var(--background))` (6, Key API) | CONTRADICTED (for new publishes) | https://help.21st.dev/publishing/quick-start ; https://help.21st.dev/publishing/quality-guidelines | Publishing rules ask for semantic tokens and Tailwind v4 theme variables, and say not to use the raw oklch or hsl variable forms [verified] |
| 4 | Components support light and dark mode (6, Key API) | CONFIRMED | https://help.21st.dev/publishing/quality-guidelines | Guidelines require light and dark mode to work [verified] |
| 5 | Demo files pass content through props (6, Key API) | CONFIRMED | https://help.21st.dev/publishing/component-structure ; https://help.21st.dev/publishing/quality-guidelines | Logic lives in the component taking props; demos supply content [verified] |
| 6 | Repo root Node >= 18 and pnpm 8.15.6 (6, Dependencies) | CONFIRMED (repo only) | https://raw.githubusercontent.com/serafimcloud/21st/main/package.json | Repo tooling values. Not a consumer requirement [verified] |
| 7 | Web app uses Next ^15.2.1 (6, Dependencies) | CONFIRMED (package.json); README CONTRADICTS | https://raw.githubusercontent.com/serafimcloud/21st/main/package.json ; https://github.com/serafimcloud/21st | package.json says ^15.2.1. README architecture section says Next.js 14, so the README is out of date [verified] |
| 8 | Publishing states are on_review, posted and featured (6, Gotchas) | STALE (confirmed) | https://help.21st.dev/publishing/quick-start ; https://github.com/serafimcloud/21st | Current help centre lists Draft, Published, Private, In review, Featured and Needs changes. The three README states come from an older flow [verified] |
| 9 | Repo last commit 2025-05-28, about 17 months stale (6, Maintenance) | UNVERIFIABLE (unverified; last commit reportedly 2025-05-28) | https://github.com/serafimcloud/21st | GitHub returns 403 here. Repo has 1,055 commits, 5.5k stars. Product and CLI are active (npm @21st-dev/cli 2026-10-06), so "stale" applies only to the open-source repo [inferred] |
| 10 | License MIT, 2024, 21st.dev (6, Maintenance) | CONFIRMED | https://raw.githubusercontent.com/serafimcloud/21st/main/LICENSE | MIT, copyright holder 21st.dev, year 2024. README names "21st Labs Inc." and states no license. Publishing docs say new Studio components default to MIT [verified] |
| 11 | The full catalogue is probably database-backed (6, Gotchas) | UNVERIFIABLE (consistent) | https://help.21st.dev/publishing/quick-start | Docs describe a hosted catalogue with Studio publishing and a featured list. Storage is not documented [inferred] |
| 12 | Components expect shadcn init and its CSS variables (6, Gotchas) | CONFIRMED | https://github.com/serafimcloud/21st (README) ; https://help.21st.dev/publishing/quality-guidelines | README says the install command extends the Tailwind theme and sets up global styles [verified] |
| 13 | Snapshot list of 19 components and publisher names (6, Component inventory) | UNVERIFIABLE | none | Snapshot file not re-checked against the live catalogue |
| 14 | Publish flow and component naming were not covered by the KB | (missed) | https://help.21st.dev/publishing/quick-start | See Missed guidelines |

## Missed guidelines

1. The `21st` CLI (help.21st.dev/cli/find) has search, get, theme, logo and add. `21st add <user>/<slug>` runs `shadcn add` against 21st's registry. The `--print` flag only prints the command [verified]. Install the CLI with `npm i -g @21st-dev/cli` (v1.18.0, MIT, npm 2026-10-06, bin `21st`). Also: `21st login`, `publish`, `components`, `open`, `publish-theme`, `publish-template`. `add` shells out to `npx shadcn@latest add` against `/r/<user>/<slug>`. `get` is free on paid plans and metered on the free tier; `search` and `logo` are free; a `--paid` flag shows items that are sold [verified https://help.21st.dev/cli/find ; https://registry.npmjs.org/@21st-dev/cli]. Publishing and catalog review are separate; Published items are not in the public catalogue until Featured [verified https://help.21st.dev/publishing/quality-guidelines]. The exact `21st add <user>/<slug>` syntax is unsourced.
2. Publishing from the CLI: a new component or local revision must be one self-contained file with one demo. Extra local files, a 21st.json, and registry dependencies must go through Studio [verified].
3. Each component needs a `default` demo. It cannot be deleted, and each demo's filename becomes its permanent slug [verified].
4. Metadata limits: description 10 to 280 characters; 1 to 5 tags per demo; required PNG or JPEG cover image up to 4 MB; optional MP4 or MOV video up to 50 MB [verified].
5. Every imported npm package must be declared in the nearest package.json, and the build must pass. Shared helpers go in src/lib or src/hooks [verified].
6. Quality guidelines: consistent hover, focus and active states; ARIA attributes; keyboard navigation; sufficient contrast; TypeScript; minimal dependencies; props for configurable behaviour; each prop documented [verified].
7. Access and team rules: Public or Private access; team publishing needs owner or admin rights and an active Team plan; only the original author can check out source code [verified].
8. Review states include Needs changes (resubmit) and withdrawing an active review. Making a component Private removes it from review or the catalogue [verified].
9. Install by prompt: the homepage describes pasting a component's prompt into an AI agent, and the 21st registry is also published as an agent skill [verified: homepage; skills.sh listing seen in search results].
10. Contributor setup (README): fork, `pnpm install`, `pnpm dev`, and an `.env.local` in apps/web with Supabase, Clerk, Cloudflare R2 and Amplitude keys. Open PRs against main [verified].

## Resources

| # | Title | URL | Type | Why useful |
|---|---|---|---|---|
| 1 | 21st.dev | https://21st.dev | Marketplace site | Browse components and see the current install-by-prompt flow [fetched] |
| 2 | serafimcloud/21st README | https://github.com/serafimcloud/21st | Repository | Install form, publishing states (outdated), contributor setup [fetched] |
| 3 | Publishing quick start | https://help.21st.dev/publishing/quick-start | Official help | Current review states, CLI and Studio publish steps, requirements [fetched] |
| 4 | Quality guidelines | https://help.21st.dev/publishing/quality-guidelines | Official help | Accessibility, theming, dependency and props rules for publishing [fetched] |
| 5 | Component structure | https://help.21st.dev/publishing/component-structure | Official help | File layout, demo rules, package.json and src/lib usage [fetched] |
| 6 | 21st CLI: find and add | https://help.21st.dev/cli/find | Official CLI help | search, get, add and --print commands [fetched] |
| 7 | Community components (docs index) | https://help.21st.dev/community/components.md | Official help | Docs index for the community catalogue [seen in search results] |
| 8 | Publish page | https://21st.dev/publish | Product page | Entry point for publishing; the review and access rules are in item 3 [seen in search results] |
| 9 | 21st registry agent skill | https://skills.sh/21st-dev/registry/21st-registry | Agent skill | Lets an AI agent search and install from the registry [seen in search results] |
| 10 | LICENSE | https://raw.githubusercontent.com/serafimcloud/21st/main/LICENSE | License | MIT terms, copyright holder 21st.dev [fetched] |
| 11 | Component libraries blog | https://21st.dev/blog/component-libraries | Blog | Context on the component-library landscape [seen in search results] |

Notes: https://21st.dev/r/shadcn/accordion was blocked by robots.txt for this client, so it is not listed as a resource. The search-result mirror at cdn.jsdelivr.net for the README was not used.

_Validated 2026-11-12 against primary sources; see ../../validation-reports/._
