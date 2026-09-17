# Layout recipes

## Main cover

- Production size: `1800 × 766`.
- Platform ratio: equivalent to `900 × 383`, produced at 2×.
- Default composition: left copy, right product screenshot.
- Protect the left copy region; a screenshot must not squeeze it.
- Crop overflow from the screenshot viewport instead of stretching the screenshot.
- Keep the screenshot's visible right and bottom edges when the design calls for a full window.
- This is the listing/share-cover purpose: reserve room for the platform's article title and prioritize only essential designed content. The same-sized article header uses a separate, fuller composition.

### Dark platform-title text

Use when WeChat will overlay dark title text in the lower title zone and the background there is pale.

- Keep the lower platform-title zone pale and quiet.
- Do not add a mask when the platform title already passes the contrast check.
- Keep the result clean and editorial.

Starter: `assets/starter/main-cover-light.html`.

### White platform-title text + bottom protection

Use when WeChat will overlay white title text across the lower portion of the cover.

- Add a feathered dark scrim only in the bottom platform-title zone, across the canvas width.
- Fade the scrim upward to transparent before it reaches the designed copy or screenshot focal region.
- The scrim must read as tonal depth, not as a card or gray rectangle.
- Use roughly the bottom `18–22%` of the canvas as the protection zone.
- This percentage is a starting point for the scrim, not a guarantee of content safety. Use the supplied platform preview and actual article-title wrapping to determine the exclusion area; expand it when necessary. A scrim does not prevent overlap between platform text and designed text.
- Start with a bottom-edge opacity around `0.38–0.48`; use less when the lower background is already dark.

Starter: `assets/starter/main-cover-dark-protected.html`.

### Customer-case person cover

Use when a real customer, speaker, operator, or executive appears in a supplied on-site photo and the person is the primary proof of the story.

- Production size remains `1800 × 766`.
- Prefer the directional composition: put the real photo on the side the person looks away from, and place copy where the gaze or gesture leads. A person facing or pointing right normally means photo left, copy right.
- Do not mirror a photo that contains readable screens, logos, product UI, or other asymmetric evidence. If the direction is unsuitable, swap the layout instead of flipping the image.
- For the standard photo-left version, use a full-height photo viewport at `left: 0`, `top: 0`, `width: 1160px`, `height: 766px`.
- Preserve aspect ratio with `object-fit: cover`. Choose `object-position` so the face, torso, and gesture remain visible; accept intentional side cropping rather than distortion.
- Fade the photo's text-side edge into the canvas background across roughly `x = 940–1260px`. The fade must be soft and must not read as a rectangular overlay.
- Treat approximately `x = 990–1800px` as the complete copy region. Place the copy group near its visual center, starting around `left: 1080px`, `top: 204px`, with a working width near `700px`.
- Keep the complete copy group left-aligned. Do not center individual lines.
- Default category line: `标杆客户案例`, around `34px`, weight `650`, letter spacing about `5px`.
- Default main headline: two lines, around `79px`, weight `760–800`, letter spacing `4px`, line-height `1.42`.
- Use white for structural words and the registered theme gradient for the core phrase. For an explicit before/after contrast, one gradient phrase per line is allowed when both phrases form one semantic pair.
- Omit the explanatory subtitle by default. Add it only when the user explicitly requests a third text level.
- Keep the category line and both headline lines inside the centered copy region. If a line overflows, shorten copy first, then use `fit-text.js` to shrink that line; do not tighten the approved spacing or shift neighboring lines.
- Retain the bottom platform-title protection zone when WeChat will overlay white text.

Starter: `assets/starter/main-cover-customer-case.html`.

### Text-only headline cover

Use when the headline itself is the strongest asset and no screenshot is needed.

- The starter provides three available text slots: short topic mark, dominant headline and support line. Retain only the slots needed by the confirmed copy and platform safe area; do not force three text levels into a crowded main cover.
- At `1800 × 766`, start near `154px` for the topic mark, `166px` for the main headline, and `74px` for the subtitle; adjust only when copy length requires it.
- Keep Chinese headline tracking tight, around `-3px` to `-6px`, and avoid inserting decorative spaces around Latin abbreviations.
- Treat the three line regions as fixed slots. Never move one slot because another line is longer.
- Keep every slot on one line. When text exceeds its slot, shrink only that slot until it fits.
- Never enlarge short copy beyond the registered baseline sizes.
- Use the bundled `scripts/fit-text.js`; do not manually add line breaks to solve overflow.
- Reserve the bottom platform-title zone; do not place the supporting subtitle inside it.
- Use theme variables only. Do not add unrelated decorative objects merely to fill space.

Starter: `assets/starter/main-cover-title-only.html`.

## Blog cover

- Production size: `900 × 540`.
- Reference display size: `450 × 270`; always render the production file at 2× instead of enlarging a low-resolution reference.
- Use the name `博客封面` in requests, filenames, delivery notes, and output manifests.
- Treat it as a regular paired output with the `1800 × 766` main cover unless the user narrows the requested formats.
- Recompose the blog cover independently. Do not stretch, crop, or proportionally scale a finished main cover into this ratio.
- Default to one centered title line for a short four-to-eight-character topic. Start near `160px`, weight `760–800`, letter spacing around `14–24px`, and keep at least `64px` of horizontal safe margin.
- When a title is longer, rewrite it concisely first; then use `fit-text.js` to shrink only the title until it fits. Keep the registered tracking unless it still overflows.
- Use one emphasized phrase or semantic half in the selected theme's title treatment; keep the remaining text in the theme's primary text color.
- A screenshot-led variant may use left copy and a right screenshot only when the supplied screenshot remains legible at `450 × 270` preview size.

Starter: `assets/starter/blog-cover.html`.

## Secondary cover

- Production size: `766 × 766`.
- Platform ratio: square. Use this exact size so a secondary cover can be joined directly to the `1800 × 766` main cover without scaling or white edges.
- For the standard two-line short-title layout, use a fixed centered text viewport of `498 × 536px`: `left: 134px`, `top: 115px`.
- The viewport geometry is fixed. The title must neither escape it nor make the viewport move.
- Start a two-line, four-to-six-character Chinese title at `249px`; use `PingFang SC`, weight near `550`, `letter-spacing: 0`, and `line-height: 1.22`.
- Keep the two title lines visibly separated. Let the fit-text script reduce font size before tightening line spacing; avoid reducing `line-height` below `1.15` for dense Chinese display titles.
- Center every title line inside the fixed viewport. When two lines have unequal lengths, the shorter line must remain visually centered instead of inheriting the longer line's left edge.
- Fill the viewport assertively. Short copy keeps the registered maximum size; longer copy shrinks through `data-fit-block` until it fits.
- Do not shrink a short title merely to create more empty space.
- Keep manual line breaks semantic and balanced; for four Chinese characters, default to two characters per line.
- Prefer no screenshot; when necessary, use one simplified crop occupying no more than half the canvas.
- Keep critical text away from all four edges.

Starter: `assets/starter/secondary-cover.html`.

## Article header / 公众号正文头图

- Default production size: `1800 × 766`, the same dimensions as the main cover but a separate purpose and composition.
- No platform-title reservation or protection scrim. Keep normal edge margins and distribute the information across the complete canvas.
- Use the confirmed visual type: text-only, person plus copy, or title plus real screenshot. Available co-brand logos, person introduction and subtitle can enrich the hierarchy when useful.
- For a person layout, preserve the real image and make a source-cropped edge meet the canvas boundary. Center the copy group vertically in its region where appropriate; individual lines may remain left-aligned.
- Do not deliver a duplicate main cover merely renamed as the header, or just remove its scrim without reconsidering information hierarchy and whitespace.

Starter: `assets/starter/article-header.html`. Adapt its content and layout to the confirmed direction; a real-person version may reuse the customer-case components.

## Optional article landscape visual / 正文横图

- Production size: `1920 × 1080`, only when requested or part of the confirmed scope.
- Default composition: centered title and support line above a large product screenshot.
- Default screenshot margins: `80px` left and right.
- Default screenshot top: `360px`.
- Default title top: `80px`; support line top: about `236px`.
- Keep the screenshot proportional and crop through the canvas boundaries.
- Give the screenshot visible rounded top corners; use full rounding when all four edges are visible.

Starter: `assets/starter/article-hero.html` (retained for the optional 16:9 format).

## Main-plus-secondary composite

- Production size: `2566 × 766`.
- Join the finished `1800 × 766` main cover on the left and the finished `766 × 766` secondary cover on the right.
- Keep both source images at native production size.
- Use the platform-title-safe main cover on the left, not the richer article header.
- Use no seam, gap, white edge, or extra margin by default.

## Single article screenshot illustration

- Use real screenshots supplied by the user; do not recreate product evidence.
- Preserve screenshot pixels and aspect ratio.
- Add a themed outer background, normally `20px` on all sides.
- Make the outer background, border, shadow, and contrast follow the selected theme.
- Use about `22px` corner radius when all screenshot edges are visible.
- For vertically stacked screenshots, use a `20px` gap by default.
- Keep unequal-width screenshots at native width and center the narrower one on the wider canvas.
- Do not force multiple screenshots to the same width.

## Multi-screenshot article collage

- Use when 2–4 real screenshots from one business scene must appear in one article-body illustration.
- Use the starter `assets/starter/article-screenshot-collage.html` and read [article-screenshot-collage.md](article-screenshot-collage.md).
- Build labeled screenshot cards plus one bottom explanation sentence; do not add a cover headline.
- Render the `1920 × 1080` master before creating a compact crop.
- Use separate 2-, 3-, and 4-column geometry; do not squeeze all screenshot counts into one fixed card width.

## Adaptation rule

Recompose content separately for each recipe. Reuse themes and components, but never resize a finished main cover into a blog cover, square cover, or article hero. Only the registered main-plus-secondary composite directly joins finished outputs.
