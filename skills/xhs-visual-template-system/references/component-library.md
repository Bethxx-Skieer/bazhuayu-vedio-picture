# Semantic Component Library

Components are chosen by communication job. Their names describe what they do, not what they look like. Use the classes and data attributes in the active theme starter.

## Global components

### `page-shell`

The fixed 1080×1440 canvas, background, safe area, and footer zone.

- Required on every page.
- One page contains one shell.
- Do not override its dimensions or theme background ad hoc.

### `brand-lockup`

The official logo in the reserved top-right position.

- Exactly one per page.
- Prefer the blue horizontal logo on a light background.
- Never recreate the logo with text.

### `eyebrow`

A short category or context label above the headline.

- 4–12 Chinese characters.
- One per page at most.
- It may use a tiny semantic dot; it is not a slogan container.

### `headline-block`

The main headline and optional one-line explanation.

- Required on every page.
- One primary message only.
- Highlight no more than one phrase.
- Interior-page support line: usually 18–36 Chinese characters.

### `page-meta`

Page number, short source note, or series marker in the quiet footer zone.

- Keep visually subordinate.
- Do not use the footer as a second CTA.

## Information components

### `surface-card`

A neutral container for one related information unit.

- Prefer one dominant card plus one or two subordinate items.
- Avoid more than four sibling cards on one page.
- A card requires an information relationship; it is not a decoration layer.

### `metric-or-result-band`

A compact band expressing the changed state or a verified result.

- Use only with a factual, supported statement.
- Green may indicate completion; blue indicates system value.
- Do not invent a number to make the band look stronger.

### `feature-item`

One capability expressed as action + object + outcome.

- 2–4 per page.
- Do not repeat the headline in every item.
- Use small icons or sequence numbers only when they speed scanning.

### `platform-badge`

A platform or business-system identifier.

- Use real platform colors only inside the badge or logo.
- 3–6 badges per group; use “等” when the full list is longer.
- Never imply unsupported platform coverage.

## Process components

### `process-node`

A numbered or named step in a causal sequence.

- 3–5 nodes per process page.
- Each node begins with a verb.
- Use blue for structure, orange for a human action or judgment, and green for completion.

### `process-connector`

An arrow or line indicating direction.

- It must connect a real before/after or step relationship.
- Avoid crossing lines.
- A connector may not become the page’s loudest object.

### `before-after`

Two unequal panels showing a changed method or state.

- The old side is neutral and slightly muted.
- The new side receives brand-blue structure and one green result cue.
- Compare the same dimension on both sides.
- Do not compare a vague pain with an unrelated feature list.

## Screenshot and image components

### `evidence-frame`

A real screenshot that proves the adjacent claim.

Required structure:

```html
<figure class="evidence-frame" data-asset-state="ready">
  <div class="evidence-bar">真实产品界面 · 任务运行记录</div>
  <div class="evidence-media">
    <img src="assets/task-record.png" alt="任务运行成功记录">
    <span class="shot-callout is-success">最近一次运行成功</span>
  </div>
  <figcaption>它证明：任务能按计划运行并留下状态记录。</figcaption>
</figure>
```

Rules:

- One large screenshot per evidence page; two only when making a direct, necessary comparison.
- Show the smallest crop that proves the claim while preserving context.
- The frame label describes the interface, not a marketing promise.
- Use one primary callout and at most one secondary callout.
- Obscure personal names, account IDs, phone numbers, and confidential business values.

### `shot-callout`

A compact annotation attached to a screenshot target.

- 6–18 Chinese characters.
- Blue for structure, orange for a clicked action, green for success.
- Never cover the source value being explained.
- The pointer direction must be unambiguous.

### `media-placeholder`

A first-class production component used when a required screenshot or image has not yet been supplied.

Required structure:

```html
<figure class="media-placeholder" data-asset-state="missing" data-required-asset="任务运行成功截图">
  <div class="placeholder-icon" aria-hidden="true"></div>
  <strong>截图待补：任务运行成功界面</strong>
  <p>需要证明：任务按计划完成，并保留运行状态。</p>
  <small>建议比例 16:9 · 保留任务名称、状态和运行时间</small>
</figure>
```

Rules:

- Preserve the intended aspect ratio and footprint.
- State what asset is needed and what claim it must prove.
- Use the dashed border only for this missing state.
- Do not label a placeholder as evidence.
- The final validation report must list every remaining placeholder.

### `atmosphere-image`

An illustration or AI-generated mood visual that supports a cover concept.

- Never use it to prove a product capability.
- Keep all important Chinese text in HTML.
- It may be absent in information-led sets.

### `ip-speech-scene`

An approved Octopus IP asset paired with one speech bubble and one supporting business-scene prop.

- Default to `octopus-3d-work-neutral.png` for generic work scenes; it has no party hat, confetti, or celebration prop and uses a transparent background.
- Keep the bubble body and tail as one CSS/SVG shape.
- Put all visible copy and pills in HTML.
- Use at most one supporting prop group and three capability pills.
- Keep decorative rings behind the IP and prop; never let them cut through the subjects.
- Prefer the original IP over regeneration when brand identity matters.

### `ip-collaboration-scene`

Two approved mascot assets and one shared work object, or one approved fixed composite scene, expressing one clear collaboration relationship.

- Use at most two mascots and one shared work object or action point.
- Keep Octopus toward the left and the partner IP toward the right when that direction matches the approved composition.
- Use a visible interaction such as sharing one computer or completing a high-five; do not place two unrelated mascots side by side.
- Keep both characters on the same lighting, material, scale, floor, and shadow system.
- When the shared object is a computer, use a real supplied task screenshot in the screen. The shell may use an approved transparent computer asset or HTML/CSS, but must remain a separate layer from the screenshot; never generate a fake product interface.
- Put all titles, role descriptions, logos, and labels in HTML.
- Treat the composite scene or both mascots as fixed approved assets; do not regenerate them during routine template use.
- This component primarily communicates partnership and role division; a real embedded screenshot may additionally establish authentic product context.

### `partner-proof-scene`

One approved Octoparse identity, one partner identity, and one centered computer containing a real task screenshot.

- Use when the partnership and the product result matter, but mascot interaction does not.
- Keep the Octoparse logo, partner logo and name, computer shell, screenshot, headline, and value band as separate replaceable layers.
- Preserve the supplied partner logo as a complete mark; crop only transparent outer padding and never redraw or recolor it.
- Put the real screenshot inside the computer screen and retain enough interface context to establish authenticity.
- Do not add mascot layers, decorative partner characters, or a second evidence frame.
- Use one concise value band below the two-line headline; it may summarize up to three verified stages or outcomes.
- Center the computer on the canvas after mascot layers are removed; do not preserve asymmetrical offsets from the IP collaboration template.

### `scene-callout`

A compact HTML annotation attached to one visible object or state inside an atmosphere scene.

- Use 2–4 callouts per scenario cover.
- Write a short object/state name plus one action line: `订单数据 / 读取订单明细`.
- Place each callout beside its target and connect it with one short, unambiguous leader line.
- Use blue-gray for inputs, green for completed matching, and orange for exceptions.
- Do not arrange scene callouts as a detached horizontal pill row.
- Do not use atmosphere-scene callouts as product screenshot evidence.

## Conversion components

### `next-step`

A low-pressure action block at the end of a set.

- Use one action only: search, open an application, fill a form, or consult.
- State what happens next.
- Do not combine price, trial, QR code, and three links in one block.

### `cta-button`

The visual action inside `next-step`.

- One per page.
- Use official blue, not a new campaign color.
- Keep it visually below the main content claim.

## Component caps

- One headline block, one brand lockup, and one focal point per page.
- Prefer 3–5 component types on an interior page.
- Maximum 4 sibling surface cards.
- Maximum 5 process nodes.
- Maximum 2 screenshot annotations.
- Maximum 4 scene callouts.
- Maximum 1 CTA.
- Maximum 3 medium solid-color modules under `hr-light-tech`.
- If a page needs more, split the page rather than shrinking everything.
