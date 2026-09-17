# Production rules

## Portable project contract

Deliver each visual as a self-contained folder:

```text
delivery/
├── index.html
├── styles/
│   ├── common.css
│   └── themes.css
├── assets/
│   ├── product-shot.png
│   └── optional-logo.svg
└── output.png
```

- Use relative paths only.
- Use `styles/common.css`, `styles/themes.css`, and `assets/product-shot.png`.
- Never reference `/Users/...`, `file://...`, temporary clipboard paths, or parent directories outside the delivery folder.
- Copy supplied assets into `assets/`; do not link back to their original locations.
- Avoid remote fonts and remote images. Prefer the bundled/system font stack.
- Preserve source image pixels whenever possible.
- Make screenshot surroundings theme-dependent. Never hard-code blue–purple framing when another theme was selected.

## Screenshot rules

- Treat screenshots as evidence.
- Keep the original aspect ratio.
- Use `object-fit: cover` or an overflow viewport to control the crop.
- Never set both width and height to unrelated values.
- Do not upscale a screenshot merely to fill space; request a larger source or accept a tighter crop.
- Prefer source screenshots near `1600 × 1000` for the established horizontal screenshot viewport.
- Use `image-rendering: auto`.
- Keep personal information out of delivered screenshots.
- Separate reference/context images from actual screenshots. Never place an explicit reference image into the finished collage.
- For multi-screenshot article collages, use `object-fit: contain` by default and keep each system/platform label outside the screenshot.
- For article screenshot illustrations, default to `20px` themed outer margins, about `22px` corner radius, and a `20px` gap between stacked screenshots.
- When stacking screenshots of different widths, preserve both native sizes and center the narrower screenshot.

## Customer-case photo rules

- Use a real photo supplied by the user. Do not generate, reconstruct, beautify, or replace the customer's face, body, clothing, product screen, venue, or gesture.
- Treat the photo as evidence: preserve its aspect ratio and keep the identity-defining face, body posture, and relevant on-site screen visible.
- A directional pose determines composition. Put copy where the subject looks or points whenever practical.
- Never horizontally flip a photo containing readable screens, logos, product UI, text, or asymmetric real-world evidence.
- For the standard photo-left cover, fill the photo viewport vertically and crop only through an explicit overflow container. Do not leave top or bottom bars.
- Use a soft edge fade from photo to copy region. Do not cover the person with a hard mask, card, or decorative frame.
- Keep the photo source inside the portable project's `assets/` directory. Keep layout-reference screenshots out of the rendered cover.

## Typography

- Font stack: `-apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif`.
- Main title weight: `700–800`.
- Support line weight: `400–500`.
- Emphasis weight: `600–700`.
- Use color or gradient for emphasis; avoid ornamental outline text.
- Keep one dominant title and at most one support line on covers.
- For fixed-slot text templates, preserve slot geometry and shrink only the overflowing line. Do not reflow neighboring lines.
- For the `900 × 540` blog cover, start a short one-line title near `160px` with `14–24px` tracking. Inspect again at `450 × 270`; shrink only when the title or safe margins fail.
- For the standard `766 × 766` secondary short-title template, keep all title glyphs inside the fixed `498 × 536px` centered viewport. Adjust font size, never the viewport.
- For the customer-case person template, keep the category and two-line headline as one centered copy group, left-aligned within its fixed region. Use the registered `34px` category and `79px` headline as baselines; shrink overflowing lines instead of compressing the `4px` tracking or `1.42` line-height.

## Composition

- Track usage purpose separately from width and height. `main-cover` and `article-header` are distinct 1800×766 outputs with distinct filenames and layouts.
- Compose the article header using the complete canvas and normal margins. Include supported identity/context information when useful; do not inherit the main cover's platform-title exclusion area.
- Keep text and screenshot in separate protected regions.
- Compose the `900 × 540` blog cover independently from the `1800 × 766` main cover; never resize or crop one finished format into the other.
- Do not let a screenshot expand into reserved copy space.
- Crop only through explicit overflow containers.
- Use consistent radii, borders, and shadows from the selected theme.
- Do not add grids, arrows, cursors, or pseudo-technical decorations by default.

## WeChat platform-title protection

- Apply this section to platform-displayed main covers, not article-body headers.
- Treat the bottom title zone as a platform overlay area, separate from the copy designed into the image.
- When WeChat uses dark title text, keep that lower zone pale and do not add a mask.
- When WeChat uses white title text, add a full-width feathered scrim only inside the bottom `18–22%` of the canvas.
- Build the scrim as a vertical multi-stop gradient: transparent at the top and darkest at the bottom edge.
- Do not place the scrim behind the designed left-side headline.
- Do not use a hard-edged translucent rectangle, visible card border, or full-canvas dark overlay.
- Keep important screenshot evidence out of the platform-title zone whenever possible.
- Inspect a preview with temporary platform-title text. Increase bottom opacity only until the white title becomes stable.
- Use the supplied platform preview and actual article title to check line wrapping, crop and overlap. The bottom 18–22% is an initial scrim recipe, not a fixed safe-area boundary. Move or simplify designed content when it conflicts with platform text; opacity alone cannot solve text-on-text overlap.
- Save the simulation only as an inspection preview; omit simulated platform text from the final PNG.

## Export audit

- Render at the exact recipe dimensions.
- Confirm the main cover and article header are separately composed at 1800×766: the cover passes the platform-title simulation, and the header uses a complete layout without that overlay reservation.
- Confirm the joined output uses the main cover plus square, and the agreed purpose/size list is complete. Do not add unrequested 16:9 or article-body outputs automatically.
- Confirm that no text is clipped.
- Confirm that the screenshot is not distorted.
- Confirm that all assets resolve after copying the delivery folder.
- Confirm that no absolute path remains in HTML or CSS.
- Inspect at full resolution and in a small WeChat preview.
- Confirm blog covers are exactly `900 × 540` and remain legible at `450 × 270`.
- For a multi-screenshot article collage, inspect both the `1920 × 1080` master and the compact crop; confirm that the crop removes only background and preserves cards, shadows, labels, and the explanation box.
