You are building ONE direction of a prototype as a single self-contained HTML file (inline CSS and JS, no network, no external fonts or libraries).

App brief: {{BRIEF}}
Your direction (follow it; do not drift toward another direction): {{DIRECTION}}
Output file (write only here): {{OUT_PATH}}

Read first, in this order:
1. {{SKILLS}}/design-lean/SKILL.md. Follow its Craft rules, Tokens and Component gate sections (skip the Review and Polish modes). Ignore any instruction to wait for the user: nobody is here. State your direction assumptions in an HTML comment at the top of the file.
2. For a calibration of what a passing file looks like, you may skim {{REFERENCE}} (a finished design for a different app). Do NOT copy its layout, data, names or copy.

Hard requirements (a script checks these):
- Mark every component with data-component and data-name as the skill describes (button, tabs, input, select, table, list, card, status, nav, image, link, control). Data views that change get data-dynamic, data-states and an empty-state element.
- Colors only through CSS custom properties; no hex or rgb literals in component rules or inline styles. 4px spacing grid. Radius scale 4, 6, 8, 10, 12, 14, 16, 20. Transitions only on color, background-color, border-color, opacity, transform, box-shadow with cubic-bezier(0.22, 1, 0.36, 1) at 100 to 500ms. Interactive targets at least 32px tall on desktop and 44px at 390px wide.
- Placeholder data only. No people's names, customers, policy or claims data, credentials. Use teams, roles and rooms.
- Real working behavior in plain JS: filtering, selecting, the primary action, and the empty and error states. Native elements first (button, a, input, select, dialog).
- Keyboard: a visible focus ring; after any action that re-renders the DOM, move focus to a sensible element (never let it fall to body); dialogs close on Escape and return focus to what opened them; tab lists use arrow keys, and if you use role=tab also add role=tabpanel with aria-controls.
- Status changes announce through one aria-live=polite region. Meaning is never carried by color alone. Respect prefers-reduced-motion.
- No horizontal page scroll at 320, 390 or 720px.

Process (stop after at most 3 rounds):
1. Write the file.
2. Run: NODE_PATH={{NODE_PATH}} node {{RUN}}/gate.js {{OUT_PATH}}
3. Fix every FAIL row (the output names the failing check) and re-run until it prints no FAIL, or you have used 3 rounds.
4. Run: NODE_PATH={{NODE_PATH}} node {{RUN}}/probe.js {{OUT_PATH}} and fix every FAIL line the same way.

Reply with exactly: the file path, the last gate summary line, the last probe summary line, and any check you could not make pass with its cause. Do not describe the design.
