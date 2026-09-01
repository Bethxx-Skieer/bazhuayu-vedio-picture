# Page and Image-Set Recipes

Recipes control combinations. A page does not begin with “Which layout looks nice?” It begins with “What must this page make the reader understand?”

## Page recipes

### A. Main-value cover

Job: earn the next swipe by naming a specific problem and changed result.

Required:

- `page-shell`
- `brand-lockup`
- `eyebrow`
- `headline-block`
- one visual anchor: `process-mini`, `evidence-preview`, `before-after-mini`, or `atmosphere-image`
- `page-meta`

Limits:

- Headline normally 8–18 Chinese characters; split into 2–3 lines.
- One support line at most.
- Do not present a complete feature catalog.
- The visual anchor occupies about 28–44% of usable height.

### B. Pain-point comparison

Job: show why the current method creates a concrete cost and what changes.

Required:

- `headline-block`
- `before-after`
- one `metric-or-result-band` or short conclusion

Allowed:

- one small platform group;
- one connector;
- no large screenshot unless it directly compares the two states.

Limits:

- Compare the same task, owner, and point in time.
- Old side: 2–3 pain details. New side: 2–3 changed actions.
- New side must describe a workflow change, not only name the product.

### C. Process explanation

Job: make the operating sequence understandable.

Required:

- `headline-block`
- 3–5 `process-node` components
- `process-connector`
- one short result line

Allowed:

- one platform group at the input;
- one destination group at the output;
- one small human-review note.

Limits:

- Node copy begins with a verb.
- Show input → transformation → destination or action.
- Avoid a grid of unrelated features disguised as a flow.

### D. Screenshot evidence

Job: establish trust with a real interface state.

Required:

- `headline-block`
- one `evidence-frame` with `data-asset-state="ready"`, or one `media-placeholder` with `data-asset-state="missing"`
- one sentence explaining what the visual proves or still needs to prove

Allowed:

- one primary and one secondary `shot-callout`;
- one small context card.

Limits:

- The screenshot occupies 46–66% of usable page height.
- Do not claim proof when the asset state is missing.
- Do not add several floating decorations around a screenshot.

### E. Feature collection

Job: group several capabilities under one user task.

Required:

- `headline-block`
- 2–4 `feature-item` components
- one organizing dimension: sequence, owner, object, or result

Allowed:

- one platform group;
- one compact result band.

Limits:

- Every feature supports the same main task.
- If the items answer different user problems, split them into separate content units.

### F. Large-type atmosphere cover

Job: create emotion or a strong judgment before detailed explanation.

Required:

- `brand-lockup`
- large `headline-block`
- one quiet visual texture or `atmosphere-image`

Limits:

- 4–14 Chinese characters.
- No more than three headline lines.
- No feature cards, full process, or screenshot grid.
- Use only when the statement is specific enough to stand alone.

### G. Result / next step

Job: close the argument and make the next action clear.

Required:

- `headline-block`
- 2–3 result or fit statements
- `next-step`
- one `cta-button`

Limits:

- One CTA only.
- Say who the route is suitable for and what happens after action.
- Do not introduce a new major claim on the final page.

### H. Scenario explanation cover

Job: make a business automation scene understandable while preserving cover-level impact.

Required:

- `page-shell`
- `brand-lockup`
- two-line `headline-block`
- one support line
- one full-bleed `atmosphere-image`
- 2–4 `scene-callout` components attached to actual scene objects

Limits:

- Keep the content system to three modules: headline, support line, and visual scene.
- Generate the background at the final 3:4 ratio with a quiet title zone; add all Chinese copy in HTML.
- Use one highlighted headline phrase or result only.
- Callouts explain inputs, actions, results, or exceptions; they are annotations inside the visual, not a separate feature row.
- Reposition callouts for every new background and keep leader lines short.

## Image-set recipes

### Product introduction · 5 pages

1. Main-value cover — concrete pain + changed result.
2. Pain comparison — old workflow versus connected workflow.
3. Process explanation — how the product moves the task end to end.
4. Screenshot evidence — real product state or an explicit missing placeholder.
5. Result / next step — fit criteria and one trial action.

Use for a new product or solution that needs both explanation and trust.

### Workflow solution · 4 pages

1. Main-value cover.
2. Process explanation.
3. Screenshot evidence.
4. Result / next step.

Use when the audience already understands the pain and mainly needs the method.

### Screenshot-led proof · 3 pages

1. Main-value cover with evidence preview.
2. Screenshot evidence with a real crop.
3. Result / next step.

Use when the interface state is the strongest differentiator.

### Task feature collection · 3 pages

1. Main-value cover.
2. Feature collection grouped by one task.
3. Result / next step.

Use for an application bundle or several related actions, not a random feature list.

### Judgment-first series · 4 pages

1. Large-type atmosphere cover.
2. Pain-point comparison.
3. Process explanation or screenshot evidence.
4. Result / next step.

Use only when the judgment is clear, defensible, and relevant to the target account.

## Storyboard record

Before building HTML, write one row per page:

| Page | Job | One message | Headline | Evidence | Screenshot state | Reader takeaway |
|---|---|---|---|---|---|---|

If `One message` contains two independent outcomes, split or choose one. If `Evidence` is empty on a proof page, use a missing placeholder and report it instead of inventing support.
