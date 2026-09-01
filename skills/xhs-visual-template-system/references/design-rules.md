# Design rules

These are brand-kernel rules shared by every theme. For production colors, surface treatment, density, and component limits, the selected registered theme is authoritative. The current default is `hr-light-tech`.

## 1. System, not a single template

Keep these stable across a campaign:

- brand-primary and business-context colors;
- Chinese sans-serif typography and heavy headline weight;
- light, controlled background texture;
- restrained translucent or white cards;
- simple geometric icons and consistent stroke weight;
- strong information hierarchy;
- evidence-first screenshot treatment;
- repeatable spacing, radii, and export quality.

Vary composition according to the page’s job. Do not repeat the same hero, card grid, and footer on every page.

## 2. Canvas and safe area

- Default Xiaohongshu portrait canvas: `1080 × 1440`.
- Keep essential content roughly `72–92px` from left and right edges and `72–100px` from top and bottom.
- Design at the final pixel size. Avoid responsive assumptions in export-only cards.
- Use `overflow: hidden` on the canvas, but never use it to conceal accidental clipping.
- Use a fixed viewport and device scale factor when exporting; compare the PNG with the intended canvas dimensions.

For WeChat Official Account covers, use the ratio requested by the publishing surface. Do not stretch a 3:4 card into a wide cover. Treat wide official-account covers as a separate experimental family until the brand rules are validated with more examples.

## 3. Color logic

Start from brand and scene, not decoration.

### Established palettes from the reviewed library

- Octoparse RPA official brand: primary blue `#0055FF`, verified from the bundled official SVG. Use it for the logo, main brand anchor, key title phrase, primary process node, and official conversion entry.
- Existing template blue `#2267EB`: keep only as an optional lighter interface blue or legacy-template accent. Do not treat it as the official primary color.
- Supporting system colors: dark navy text near `#14213D`, green success near `#14BF78`, orange emphasis near `#FF7A21`.
- WeChat automation: WeChat green near `#07C160`, deep green-black text near `#10261B`, pale mint surfaces, restrained yellow underline or signal accents.
- Glass automation: pale blue-white base, blue and green atmospheric gradients, optional low-opacity orange warmth.

Use one dominant hue, one semantic accent, and neutrals. A third accent is allowed only when it encodes a real category or process state. Platform colors may identify BOSS, Liepin, Feishu, WeChat, and similar services, but must not replace the official brand hierarchy.

Avoid random gradients, rainbow decoration, and saturated colors without semantic meaning.

## 4. Fixed logo system

Place an official Octoparse RPA logo on every published image. Reserve the slot before arranging titles, screenshots, or decorative elements.

### Default slot for `1080 × 1440`

- Anchor the horizontal logo combination to the top-right.
- Keep its right edge `72px` from the canvas and its top edge `64–72px` from the canvas.
- Use a visible width of approximately `168–210px`; preserve the original aspect ratio.
- Reserve at least the logo’s icon height as clear space on every side. Do not let text, grid accents, card borders, or IP artwork enter this area.
- Keep the logo at full opacity. Do not use it as a watermark.

### Variant selection

- On white, pale blue, pale mint, or other light backgrounds, prefer `assets/brand/octoparse-rpa/数阔八爪鱼RPA_文字+图标蓝.png`.
- On dark, photographic, or saturated backgrounds, prefer `assets/brand/octoparse-rpa/数阔八爪鱼RPA_文字+图标bai.png`.
- When background contrast is unstable, place the logo inside a quiet white or dark translucent plate with `16–24px` internal padding. Do not add glow, bevel, or recoloring.
- Use the icon-only mark only when the horizontal combination would be illegible, such as a very narrow secondary badge. The default published-page signature remains the horizontal combination.

### Wide WeChat covers and alternate ratios

- Keep the same top-right logic and use a safe inset of roughly `6–7%` of canvas width.
- Confirm platform crop zones before export. Move the entire reserved slot only when the publishing surface would crop it; keep the chosen alternate position consistent across the whole series.

### Prohibitions

- Do not stretch, crop, rotate, outline, recolor, or separate elements of the official combination mark.
- Do not place the logo over a busy screenshot.
- Do not repeat the full logo elsewhere on the same page. Product icons inside screenshots do not count as repeated brand signatures.
- Keep the bottom area available for scene notes, search entry, application link, or CTA; do not move the fixed brand signature there by default.

## 5. Background texture

Use quiet structure that survives behind information:

- pale linear gradients;
- one or two radial glows;
- a very low-contrast technical grid when the topic benefits from it;
- translucent white overlays for glass variants.

The background must not compete with the title or screenshot. Grid lines should be felt before they are noticed. Avoid fake depth created by many unrelated blobs, stars, rings, or noise layers.

## 6. Typography and hierarchy

Use a dependable Chinese system stack such as:

```css
font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
```

Recommended starting ranges for `1080 × 1440`:

- main cover headline: `72–128px`, up to about `142px` for very short display words;
- secondary headline: `44–68px`;
- card title or process step: `30–40px`;
- supporting copy: `22–30px`;
- disclaimer or footer: `18–24px`, never used for important evidence.

Use no more than three obvious text levels on one page. Prefer weight, scale, and whitespace over many colors. Set Chinese headline line-height around `0.96–1.16` and supporting copy around `1.25–1.45`. Manually control line breaks; do not leave a single punctuation mark or weak word stranded.

## 7. Cards and glass surfaces

- Use cards to group a unit of meaning, not to fill empty space.
- Use a small family of radii, typically `24–40px` on this canvas.
- Prefer subtle colored borders and broad, low-opacity shadows.
- Glass treatment requires contrast: translucent white surface, restrained blur, readable foreground, and a quiet background behind it.
- Do not stack glass on glass until boundaries become unclear.
- Avoid a page made entirely of identical rounded rectangles. Change grouping only when the meaning changes.

## 8. Icons, pills, arrows, and highlights

- Use geometric or product-native icons with consistent visual weight.
- Use numbered circles for ordered steps.
- Use arrows only to show sequence, direction, transfer, or before/after movement.
- Use pills for category, status, short outcome, or conversion entry. Do not place every phrase in a pill.
- Use underline/highlight blocks for one decisive phrase, not several unrelated lines.
- Keep decorative marks subordinate to content.

## 9. Screenshot evidence

A screenshot is evidence, not wallpaper.

1. Identify the claim first.
2. Select the smallest UI region that visibly proves it.
3. Preserve enough surrounding interface to establish authenticity and context.
4. Crop irrelevant chrome, empty areas, personal data, and unrelated controls.
5. Enlarge the key region rather than shrinking an entire desktop screenshot.
6. Add at most one primary callout and one secondary annotation when possible.
7. Place labels outside important UI and connect them with a short leader line or highlight box.
8. Never fabricate interface states or imply that a screenshot proves something it does not show.

Use real screenshots on evidence pages. Use simplified CSS illustrations only for atmosphere, category recognition, or mechanism diagrams.

When the needed screenshot is not available, use the registered `media-placeholder` component. Keep the intended ratio, name the missing asset, and state what the future screenshot must prove. A placeholder may preserve production structure, but it may not be described as proof.

## 10. Asset portability

- Store assets beside the template or in a stable `assets/` directory.
- Reference them with relative paths.
- Avoid `file:///Users/...`, Desktop folders, temporary downloads, and external hotlinks.
- Use filenames that describe content and purpose.
- Keep source screenshots separate from cropped derivatives when practical.
- Verify every image loads in a clean export environment.

### Bundled source libraries

- Official logo source package: `assets/brand/octoparse-rpa/`.
- Octopus mascot/IP source package: `assets/ip/octopus-ip/`.
- Preserve the source files. Copy only selected production assets into each output project.
- Treat mascot artwork as optional content illustration, never as a substitute for the fixed official logo.

## 11. Clean HTML rules

- Declare design tokens with CSS variables.
- Prefer flex and grid for layout.
- Keep the base template free of editing-tool inline `transform`, width, height, and font overrides.
- Use absolute positioning only for intentional overlays or decorative layers.
- Keep visible text in HTML, not flattened into a background image.
- Make each page independently exportable.

## 12. Review findings by family

### HR recruiting automation — mature

Strengths: immediate category recognition, high-contrast blue hierarchy, four-step mechanism, platform proof, before/after emotional contrast. Preserve the chain “find → judge → reach → write back.”

Watchouts: the information-overview cover is dense; do not add more support cards. The comparison page has many tags; reduce tags if the title or real screenshot becomes more important.

### WeChat RPA — mature visual direction, asset cleanup required

Strengths: scene-specific green, strong feature grouping, clear search entry, official and practical tone.

Watchouts: avoid presenting eight capabilities as equal; prioritize by user job. Registered templates must use Skill-local relative asset paths. Generic CSS phone/document illustrations do not replace screenshot evidence.

### Glass Xiaohongshu covers — mature as a layout family

Strengths: minimal elements, large typography, clear process rows, premium atmospheric depth.

Watchouts: the pure glass process page lacks a topic headline and is better as an inner process page than a click cover. Large empty areas must create focus, not merely look sparse.

### WeChat Official Account black-tech cover — experimental

Only an export script and a title reference were found during review; the source HTML and rendered image were unavailable. Treat dark technology covers as an unvalidated direction. Establish wide-cover hierarchy, portrait or subject treatment, brand presence, and mobile crop safety through future examples before declaring fixed rules.

## 13. Final visual audit

Reject or revise when any answer is “no”:

- Can a reader understand the page’s one main message in about one second?
- Is there one obvious visual center?
- Does every card, arrow, icon, and pill improve understanding?
- Does a screenshot prove the nearby statement?
- Is important copy readable on a phone preview?
- Are margins and vertical rhythm visibly balanced?
- Does the page belong to the brand and the business context?
- Does it feel useful and credible rather than like a generic ad?
- Are assets portable and the exported PNG technically clean?
- Is the official logo in the fixed top-right slot, using the correct contrast variant and adequate clear space?
