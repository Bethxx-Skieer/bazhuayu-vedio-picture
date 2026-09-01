# Theme: HR 蓝白轻科技

## Design intent

This is the default official-brand theme. It comes from the strongest parts of the HR recruiting automation set: calm blue-white space, clear process structure, real screenshots, and small semantic accents. It should feel dependable and technical without becoming a blue software dashboard.

The background is mostly near-white. Blue establishes brand and structure. Orange marks an action or decision. Green marks a completed state or result. Every strong color must have a job.

## Tokens

| Role | Token | Value | Use |
|---|---|---:|---|
| official primary | `--brand-blue` | `#0055FF` | logo relationship, primary accent, CTA, key label |
| interface blue | `--ui-blue` | `#2267EB` | numbered nodes, screenshot annotations, legacy-HR continuity |
| ink | `--ink` | `#14213D` | headlines and primary copy |
| body text | `--text` | `#34415C` | body copy |
| muted text | `--muted` | `#68738A` | captions and secondary labels |
| action | `--action` | `#FF7A21` | action, judgment, attention |
| success | `--success` | `#14BF78` | completion, result, enabled state |
| canvas | `--canvas` | `#F5F7FF` | base background |
| surface | `--surface` | `#FFFFFF` | primary cards |
| soft blue | `--soft-blue` | `#EEF4FF` | process or result background |
| line | `--line` | `#DDE7FA` | borders and separators |

## Color balance

- Near-white, pale blue, and white surfaces: 72–82% of the page.
- Dark ink and body copy: 12–18%.
- Strong blue: 7–12%.
- Orange and green together: normally no more than 5%.
- A large solid-blue rectangle must never occupy a whole half-page.
- Use no more than three medium solid-color modules on one page. Small numbered nodes and tiny status dots do not count as modules, but should still remain sparse.
- Never use an evenly distributed rainbow palette. Semantic accents are not decoration.

## Background

Use a nearly white vertical wash with:

- a low-contrast 72px technical grid;
- one very faint warm glow near the upper-right;
- one very faint blue glow near the lower-left;
- no saturated purple, cyan, or neon gradient;
- no large blurred color cloud behind body text.

The grid should be felt before it is noticed. If it reads as graph paper at thumbnail size, reduce it.

## Surfaces

- Primary cards are white or slightly translucent white.
- Borders are pale blue-gray, usually 1–2px.
- Shadows are broad, low-opacity, and cool. Avoid dark drop shadows.
- Primary radius: 28–36px. Small controls: 14–22px.
- A tinted surface is allowed to group a process, result, or screenshot explanation. Do not tint every card.
- Glass effects may be used lightly, but do not depend on blur for legibility.

## Typography

- Use Chinese system sans-serif fonts: `PingFang SC`, `Microsoft YaHei`, `Noto Sans SC`, sans-serif.
- Cover headline: 82–112px, weight 800–900, compact line-height.
- Interior headline: 56–76px, weight 750–850.
- Card title: 32–42px.
- Body copy: 25–32px.
- Caption: never below 22px on a 1080px portrait card.
- Use bold weight and spacing before adding another colored box.

## Composition grammar

- Reserve the top-right fixed brand-logo slot before placing text.
- Start the content column around 146–176px from the top, depending on headline length.
- Keep the dominant headline left-aligned unless a large-type cover recipe says otherwise.
- Prefer asymmetry: strong text area plus one visual proof area.
- Use a visible vertical rhythm of 24, 32, 48, 64, and 80px.
- The lower 170px should remain quiet enough for page number, source note, or CTA.

## Semantic color rules

- Blue: platform connection, automation framework, primary action, structural node.
- Orange: manual action, judgment, attention, or current step.
- Green: success, automatic completion, result, enabled state.
- Gray: old method, inactive state, secondary context.
- Platform brand colors: only on platform badges or logos; keep their total visual weight below the official blue hierarchy.

## Screenshot treatment

- Real screenshots sit inside a white evidence frame with a small context bar and a short claim label.
- Crop for proof but keep enough interface context to remain credible.
- Use one primary callout; a second small annotation is optional.
- Callouts use blue by default, orange for an action, and green for a completed state.
- Missing imagery uses the theme’s `media-placeholder`; never draw a fake interface.

## Avoid

- full-page blue dashboards;
- toxic-looking multicolor gradients;
- blue applied to every card, icon, and divider;
- decorative pills with no semantic meaning;
- five equal cards competing for attention;
- tiny UI screenshots shown only as texture;
- high-gloss advertising effects, excessive glass, or fake 3D chrome.
