# UI component knowledge base

> Online validation 2026-11-12: corrections from `kb/validation.md` are applied below.

Built 2026-11-12 from local clones under /home/claude (read-only). Tags: [verified] = read in this run (README, manifest or source); [inferred] = deduced, not run.

## Summary

| Repo | Package / version | Last commit | License | Status |
|---|---|---|---|---|
| emilkowalski/sonner | sonner 2.0.8 | 2026-08-10 | MIT | Active |
| emilkowalski/vaul | vaul 1.1.2 | 2025-10-03 | MIT | Unmaintained (README says so) |
| pacocoursey/cmdk | cmdk 1.1.1 | 2025-10-28 | MIT | Low churn [inferred] |
| barvian/number-flow | number-flow 0.6.2, @number-flow/react 0.6.2 | 2026-09-20 | MIT | Active |
| magicuidesign/magicui | private site + registry (no version) | 2026-11-12 | MIT | Active |
| serafimcloud/21st | open-source platform, public repo (no version) | 2025-05-28 | MIT | Stale (about 17 months) [verified: upstream HEAD is that commit] |
| codewithswappy/rareui | rareui CLI 0.1.6; site 0.1.0 | 2026-04-07 | MIT | Moderate [inferred] |

## 1. emilkowalski/sonner

- **Purpose:** Opinionated React toast component. Mount `<Toaster />` once, then call `toast()` from anywhere. [verified README]
- **Install:** `npm install sonner` [verified README]
- **Minimal usage** (README, trimmed):
```jsx
import { Toaster, toast } from 'sonner';
<Toaster />
<button onClick={() => toast('My first toast')}>Give me a toast</button>
```
- **Key API:**
  - `<Toaster>` props: `position`, `theme` ('light' | 'dark' | 'system'), `richColors`, `expand`, `duration`, `closeButton`, `visibleToasts`, `toastOptions` [verified src/types.ts:128-150]
  - `toast(message, data?)`, plus `toast.success` and `toast.loading` [verified src/state.ts:180-193]
  - `toast.promise(promise, { loading, ... })` [verified src/state.ts:196-213]
  - Per-toast options typed as `ExternalToast` [verified src/types.ts:197]
- **Dependencies:** peer `react` and `react-dom` ^18 || ^19 || ^19.0.0-rc; `@types/react` optional [verified package.json]. Exports `./dist/styles.css`, copied from src/styles.css at build [verified package.json]. The source imports `./styles.css` at src/index.tsx:9 [verified]. Whether bundlers need an explicit CSS import is not stated in the README [inferred from exports].
- **Component inventory:** one component (`Toaster`) plus the `toast` API. Exports: `toast`, `Toaster`, `useSonner` [verified src/index.tsx:899].
- **Extras:** README points to an `ask-sonner` agent skill: `npx skills add https://github.com/emilkowalski/skills --skill ask-sonner` [verified README].
- **Gotchas:**
  - Loading toasts never auto-dismiss: the timer is skipped when `type` is loading or `duration` is Infinity [verified src/index.tsx:204].
  - Use `toast.promise` to swap a loading toast for success or error [verified src/state.ts:196-213].
  - Keep one `<Toaster />` per app [inferred; not tested].

## 2. emilkowalski/vaul

- **Purpose:** Drawer (bottom sheet, or a panel on any edge) for React, built on Radix Dialog, with snap points and drag-to-dismiss. The README is only an "unmaintained" notice, so purpose comes from package.json and src/index.tsx [verified].
- **Install:** `npm install vaul` [verified on the npm package page; vaul.emilkowal.ski is blocked by robots.txt].
- **Minimal usage** (inferred from the `Drawer` export object, src/index.tsx:1137-1147):
```jsx
import { Drawer } from 'vaul';
<Drawer.Root>
  <Drawer.Trigger>Open</Drawer.Trigger>
  <Drawer.Portal><Drawer.Overlay /><Drawer.Content>...</Drawer.Content></Drawer.Portal>
</Drawer.Root>
```
- **Key API:** `Drawer.Root` props (src/index.tsx:50-135):
  - `open` and `onOpenChange`
  - `direction`: 'top' | 'bottom' | 'left' | 'right'
  - `snapPoints` with `activeSnapPoint` and `setActiveSnapPoint`
  - `modal`, `nested` (and `NestedRoot`)
  - `dismissible`, `shouldScaleBackground`, `handleOnly`
- **Dependencies:** peer `react` and `react-dom` ^16.8 through ^19 [verified package.json]. Runtime dependency `@radix-ui/react-dialog` ^1.1.1 [verified package.json]. Ships `style.css` [verified package.json files].
- **Component inventory:** `Drawer.Root`, `NestedRoot`, `Trigger`, `Portal`, `Overlay`, `Content`, `Handle`, `Close`, `Title`, `Description` [verified src/index.tsx:1137-1147].
- **License:** MIT, 2023 Emil Kowalski [verified LICENSE.md].
- **Maintenance:** README says the repo is unmaintained and the author does not plan near-term work [verified README]. Pin the version if you depend on it [inferred].
- **Gotchas:**
  - Passing `snapPoints` does not require `fadeFromIndex`: the props type is a union, and the variant without it sets `fadeFromIndex` to `never` [verified src/index.tsx:27-47, rechecked 2026-11-12; earlier claim was wrong].
  - `handleOnly` limits dragging to the handle [verified prop exists; exact behaviour inferred].
  - Radix Dialog is a hard dependency, so Radix version drift can affect it [inferred].

## 3. pacocoursey/cmdk

- **Purpose:** Command-menu (Cmd+K) React component that doubles as an accessible combobox. It filters and sorts items for you and ships no styles [verified README, src/index.tsx].
- **Install:** `pnpm install cmdk` [verified README]. npm works too [inferred].
- **Minimal usage** (README, trimmed):
```tsx
import { Command } from 'cmdk'
<Command label="Command Menu">
  <Command.Input />
  <Command.List>
    <Command.Item>Apple</Command.Item>
  </Command.List>
</Command>
```
- **Key API:** root props (src/index.tsx:85-120):
  - `label`
  - `shouldFilter`: false turns off automatic filtering, needed for server-side search
  - `filter`, `loop`
  - `value`, `defaultValue`, `onValueChange`
  - `disablePointerSelection`, `vimBindings` (default true)
  - Items take `value`, `keywords`, `onSelect` and `forceMount` [verified src/index.tsx:45-62]
  - `Command.Dialog` takes `open` and `onOpenChange` [verified README]
- **Dependencies:** peer `react` and `react-dom` ^18 || ^19 || ^19.0.0-rc. Runtime: `@radix-ui/react-dialog` ^1.1.6, `@radix-ui/react-primitive`, `@radix-ui/react-id`, `@radix-ui/react-compose-refs` [verified cmdk/cmdk/package.json].
- **Component inventory:** Command (root), Input, List, Empty, Group, Item, Separator, Loading, Dialog. Each also exports under a `Command*` alias, such as `CommandList` [verified src/index.tsx:941-953].
- **Styling hooks:** `cmdk-root`, `cmdk-input`, `cmdk-list`, `cmdk-item`, `cmdk-group`, `cmdk-group-heading`, `cmdk-empty`, `cmdk-separator`, `cmdk-dialog`, `cmdk-loading` and others [verified, grep of src/index.tsx].
- **License:** MIT, 2022 Paco Coursey [verified LICENSE.md].
- **Maintenance:** last commit in the clone 2025-10-28 [verified]. The releases page lists 1.1.0 and 1.1.1 (undated year), so activity may be newer than this; not confirmed [online check 2026-11-12].
- **Gotchas:**
  - `value` must be stable and unique when item text changes [verified README].
  - With server-side results, set `shouldFilter={false}` [verified src/index.tsx:90].
  - `vimBindings` defaults to true and adds Ctrl+J/K/N/P navigation; the handlers check `ctrlKey`, so plain letter keys are not captured [verified src/index.tsx:200,594-608].

## 4. barvian/number-flow

- **Purpose:** Animated number component. Digits animate between values. The core is a framework-agnostic web component (`number-flow`). Wrappers exist for React (`@number-flow/react`), Svelte (`@number-flow/svelte` 0.4.2) and Vue (`@number-flow/vue` 0.5.2) [verified packages/*/package.json, README]. The 0.0.1 in site/package.json belongs to the docs app, not the published package [verified online].
- **Install:** `npm install @number-flow/react` [package exists on npm at 0.6.2; no install command in the docs site or README].
- **Minimal usage** (default export confirmed at packages/react/src/NumberFlow.tsx):
```jsx
import NumberFlow from '@number-flow/react'
<NumberFlow value={count} />
<NumberFlow value={0.42} format={{ style: 'percent' }} />
```
- **Key API** (packages/react/src/NumberFlow.tsx):
  - `value` (required), `format` (Intl.NumberFormatOptions), `locales`
  - `prefix`, `suffix`
  - `willChange`, `isolate`
  - `onAnimationsStart`, `onAnimationsFinish`
  - `respectMotionPreference` (default true, from the core Props) [verified packages/number-flow/src/lite.ts:44,79]
  - `NumberFlowGroup` to coordinate several numbers [verified NumberFlow.tsx:244]
- **Dependencies:** React ^18 || ^19 (react, react-dom peers). Svelte ^4 || ^5. Vue ^3 [verified package.json]. Runtime: `esm-env`, and `number-flow` for the React package [verified].
- **Component inventory:** `NumberFlow`, `NumberFlowGroup`, the web-component element, and a `continuous` plugin that makes transitions pass through intermediate digits [verified packages/number-flow/src/plugins/continuous.ts].
- **License:** MIT, 2024 Maxwell Barvian [verified LICENSE.md].
- **Maintenance:** active, last commit 2026-09-20; changesets for releases [verified].
- **Gotchas:**
  - Animation respects `prefers-reduced-motion` by default [verified lite.ts:186,228].
  - The React wrapper starts with `'use client'` [verified NumberFlow.tsx:1].
  - Docs live on the external site, number-flow.barvian.me [verified README].

## 5. magicuidesign/magicui

- **Purpose:** Magic UI, a copy-paste library of animated React and Tailwind components. Each component is a source file you own, installed through the shadcn registry as `@magicui/<slug>` [verified README, SKILL.md]. The repo is the docs site (apps/www) plus the registry source (apps/www/registry/magicui/*.tsx) [verified].
- **Install:**
```bash
npx shadcn@latest init
npx shadcn@latest add @magicui/magic-card
```
- **Minimal usage** (import path from the skill; JSX children inferred):
```tsx
import { MagicCard } from "@/components/ui/magic-card"
<MagicCard>Hello</MagicCard>
```
- **Key API:** no shared runtime. Each component has its own props type, for example `MagicCard(props: MagicCardProps)` [verified apps/www/registry/magicui/magic-card.tsx:56]. Registry entries declare their own npm dependencies, for example magic-card needs `motion` [verified registry.json].
- **Dependencies:** React/Next.js with Tailwind CSS and shadcn initialised [verified SKILL.md]. Repo dev needs Node >=22.14 and pnpm >=9 [verified package.json engines].
- **Component inventory:** 79 `registry:ui` items in registry.json (magicui.design/docs/components lists 78; client-tweet-card is the one not shown), plus 179 `registry:example` items [verified]:
  magic-card, android, warp-background, line-shadow-text, aurora-text, morphing-text, scroll-progress, lens, pointer, smooth-cursor, progressive-blur, neon-gradient-card, noise-texture, meteors, grid-pattern, hexagon-pattern, striped-pattern, interactive-grid-pattern, dot-pattern, flickering-grid, hero-video-dialog, code-comparison, marquee, globe, glyph-matrix, glare-hover, shimmer-button, tweet-card, client-tweet-card, bento-grid, particles, number-ticker, ripple, retro-grid, animated-list, animated-shiny-text, animated-grid-pattern, border-beam, animated-beam, text-reveal, dia-text-reveal, hyper-text, animated-gradient-text, orbiting-circles, dock, word-rotate, avatar-circles, typing-animation, sparkles-text, spinning-text, comic-text, icon-cloud, text-animate, scroll-based-velocity, shiny-button, shine-border, animated-circular-progress-bar, confetti, cool-mode, pulsating-button, ripple-button, file-tree, blur-fade, safari, iphone, rainbow-button, interactive-hover-button, terminal, video-text, pixel-image, highlighter, animated-theme-toggler, light-rays, dotted-map, backlight, kinetic-text, text-3d-flip, floating-3d-particles, dither-field
- **Skill:** see the next section.
- **License:** MIT, Magic UI [verified LICENSE.md].
- **Maintenance:** active, last commit 2026-11-12 (today) [verified].
- **Gotchas:**
  - Some components need global CSS keyframes or extra packages listed in their docs [verified SKILL.md].
  - Keep component APIs intact and customise through props or className [verified SKILL.md].

### Magic UI agent skill

File: /home/claude/magicuidesign/magicui/skills/magic-ui/SKILL.md (name `magic-ui`). Related files: references/components.md and references/recipes.md. Only the first 20 lines of components.md were read; recipes.md was not read.

- **Triggers:** adding, customising or troubleshooting Magic UI components in React or Next.js projects.
- **Workflow:** define the UI outcome, confirm prerequisites (React/Next.js, Tailwind, shadcn init), run `npx shadcn@latest add @magicui/<slug>`, import from `@/components/ui/<slug>`, then check accessibility, responsiveness, performance and maintainability.
- **Integration rule:** keep the component API intact and prefer prop or className changes over rewriting internals.
- **Motion budget:** start with one core component plus one supporting effect; do not stack many high-motion effects in one viewport.
- **Selection heuristics:** social proof (marquee, avatar-circles); hero (globe, warp-background, animated-grid-pattern); text (blur-fade, text-animate, word-rotate, sparkles-text); CTA (shiny-button, shimmer-button, rainbow-button); backgrounds (grid-pattern, dot-pattern, particles, flickering-grid, dither-field).
- **Troubleshooting:** `components.json` or init errors (run shadcn init), `@/` alias mismatch, missing global CSS, missing packages listed in the component's manual install steps.
- **Reference links:** magicui.design/docs, components, installation, MCP setup.

## 6. serafimcloud/21st

- **Purpose:** Source of 21st.dev, a community registry of React, Tailwind and Radix components installed through shadcn [verified README]. The repo is the platform itself, a Turborepo with apps/web (Next.js), apps/backend and packages/ui, not a component library [verified directory listing, package.json]. The GitHub repo is public and the README calls it an open-source registry [verified online].
- **Install (for a component, not the repo):**
```bash
pnpm dlx shadcn@latest add "https://21st.dev/r/serafimcloud/animated-hero"
```
  Pattern taken from a search-result record [verified search_results.json].
- **Key API:** no runtime API. The contract is the shadcn install URL `https://21st.dev/r/<owner>/<component>` [verified]. Components use shadcn CSS variables such as `hsl(var(--background))` (README form; the 21st help centre now asks new publishes to use semantic Tailwind v4 tokens, not raw hsl/oklch variable forms [verified online 2026-11-12]) and support light and dark mode. Demo files pass content through props [verified README].
- **Dependencies:** root Node >=18 and pnpm 8.15.6 [verified package.json]. The web app uses Next ^15.2.1, Radix radio group, TanStack Table, recharts, Monaco editor, Clerk and Prisma [verified package.json, apps/web/package.json].
- **Component inventory:**
  - packages/ui/src holds only button.tsx, card.tsx and code.tsx [verified].
  - The catalogue is not in the repo. search_results.json is a snapshot of one search, containing: Animated hero, Animated Testimonials, Container Scroll Animation, Expandable Card, Feature Section, Hero Badge, Hero Highlight, Hero Parallax, Hero Pill, Hero Section, Hero Section Dark, Hero Video Dialog, Hero with Mockup, Hero with text and two button, Hero with image, text and two buttons, Hero with group of images, text and two buttons, Shape Landing Hero [verified].
  - The snapshot also has publisher names (Aceternity UI, Origin UI, Prism UI, Serenity UI, Kokonut, Magic UI). These are sources, not components [inferred].
- **License:** MIT, 2024 21st.dev [verified LICENSE].
- **Maintenance:** last commit 2025-05-28 [verified: upstream HEAD equals clone HEAD, 2026-11-12]. No commits in about 17 months. Archived flag not verified (GitHub API blocked).
- **Gotchas:**
  - README publishing states are `on_review`, `posted` and `featured`; the help centre now lists Draft, Published, Private, In review, Featured and Needs changes, so the README is out of date [verified online 2026-11-12].
  - The full catalogue is probably database-backed, since supabase/ holds SQL and seed files only [inferred].
  - Components expect shadcn init and its CSS variables [verified README].

## 7. codewithswappy/rareui

- **Purpose:** "The most unique and premium library of animated React components", copy-paste or CLI install. Docs at rareui.in [verified README].
- **Install:**
```bash
npx rareui add liquid-metal
```
  Example from README [verified]. The CLI accepts kebab-case or PascalCase names [verified packages/cli/src/index.ts:58,68].
- **Key API:**
  - CLI: `npx rareui add [component-name]`, which creates components.json on init [verified packages/cli/src/index.ts:45,58].
  - Per-component props were not read.
  - Lazy variants exist for heavy components: LiquidMetalLazy, LiquidWaveLazy [verified file names].
  - Registry JSON per component under public/r/ [verified].
- **Dependencies (site app, from README and package.json):** React ^19.2, Next ^16.2.1, Tailwind CSS 4, Framer Motion ^12.23, three ^0.181, @number-flow/react ^0.5.10, many @radix-ui primitives [verified]. Site Node >=20.18.0 [verified]. CLI dependencies: @clack/prompts, commander, execa, fs-extra, chalk [verified].
- **Component inventory:** 41 files in public/r/ and component folders in components/rareui/ [verified]: 3D elements, AnimatedTab, AvatarGroup, Book3D, ClickSpark, FeatureBadge, FloatingNavigation, GlassSearchBar, GlassShimmerButton, LiquidButton (liquidButton), LiquidMetal (+Lazy), LiquidTooltip, LiquidWave (+Lazy), LoadingSpinner, MagneticScatterText, ParticleCard, PremiumButton, PremiumProfileCard, ProfileDropdown, RetroPixelButton, SoftButton, SoundText, Text Animation, ThreeDButton, ToastTabs, VaporSmokeText, WordMagnet, Neumorphism3DButton, ImageExpandTestimonial, interactive-background. Test entries also exist: LoadingSpinner.test, PremiumButton.test.
- **License:** MIT, 2025 Swapnil Kalambe [verified LICENSE].
- **Maintenance:** last commit 2026-04-07 [verified]. Changelog at data/changelog.json [verified]. Moderate activity [inferred].
- **Gotchas:**
  - The CLI accepts kebab-case or PascalCase names, so the README's `liquid-metal` is fine [verified online 2026-11-12].
  - Do not install the `.test` registry entries [inferred].
  - README lists React 19, Next 16, Tailwind 4 and Framer Motion 12 as the stack, not as strict requirements; React 18 compatibility is untested [verified online 2026-11-12].
  - Three.js-based components add weight [inferred from the three dependency and 3D names].

## Not read

- Magic UI references/recipes.md, and the rest of components.md.
- Per-component props for rareui and 21st.
- Sonner, cmdk and vaul test suites and website folders.
- Any repo's CHANGELOG (none checked).

## Guideline check and resources (2026-11-12)

Per-library verdict tables, missed guidelines and resource lists are in `kb/resources/` (start at `kb/resources/README.md`). Highest-value additions not covered above:

- **Sonner:** default duration 4000 ms; timers pause on expand, hover and hidden tab; the list is an `aria-live` polite region; Alt+T focuses it; several positions share one `listRef`, so keep one position unless you test keyboard focus; reduced motion disables toast transitions.
- **Vaul:** unstyled; Handle is `aria-hidden`; clicking the Handle cycles snap points; a Title is needed for accessibility (Radix behaviour); `NestedRoot` throws outside a parent drawer; docs site blocks automated fetching.
- **cmdk:** v1.0.0 made `Command.List` required and values case-sensitive; no built-in Cmd+K listener; no virtualization (about 2-3k items); client-only; set `open` false on the server; `cmdk-overlay` hook exists. The README FAQ says React 18 is required while the peer range allows 19, so trust package.json.
- **NumberFlow:** `digits` is not reactive; `isolate` does nothing inside `NumberFlowGroup`; `::part` styling needs Declarative Shadow DOM; CSP needs `nonce`; no scientific notation, RTL or non-Latin digits.
- **Magic UI:** the keyframes rule is not universal (border-beam needs none); border-beam's parent needs `relative overflow-hidden`; component class names use Tailwind v4 syntax [inferred].
- **21st.dev:** `21st add <user>/<slug>` CLI; published components need a `default` demo and a cover image; the registry URLs block automated fetching.
- **RareUI:** CLI flags `-y -o -c -p`, `diff`, `add .` installs everything; contributors must meet WCAG 2.1 AA.
