---
name: wechat-visual-system
name_en: WeChat Visual System
name_zh: 微信视觉生产系统
description: Infer a visual direction from an article, confirm it once, then create and audit a WeChat visual set with purpose-specific layouts, including distinct 1800×766 main covers and article headers, 900×540 blog covers, square covers and joined previews. Also supports real screenshot collages and GIFs. Not for Xiaohongshu sets or long-form article formatting.
description_en: Infer a visual direction from an article and confirm it once, then produce purpose-specific WeChat main covers, same-sized article headers, blog covers, square covers and composites using portable HTML/CSS. Also supports real screenshot collages and GIFs.
description_zh: 从文章推断视觉方向，确认后自动输出按用途独立排版的公众号头条封面、同尺寸正文头图、博客封面、方形图和拼接图；支持真实截图正文配图及GIF，不负责小红书套图或公众号长文排版。
argument-hint: Provide the topic/copy, real screenshots or photos, requested WeChat image type and dimensions, theme preference, and delivery folder
argument-hint-en: Provide the topic/copy, real screenshots or photos, requested WeChat image type and dimensions, theme preference, and delivery folder
argument-hint-zh: 附上主题或文案、真实截图或人物照片，说明要制作的微信图片类型、尺寸、配色偏好和交付目录
user-invocable: true
version: 1.1.0
---

# WeChat Visual System

本文件的 `name` 与 `description` 及 `agents/openai.yaml` 供 WorkBuddy 加载，双语元数据与 `.skill-metadata.yaml` 供千问办公加载；两端共享同一份模板、参考规范和校验脚本。

For palette inspiration collection, browsing, or maintenance (not finished visual production), read [references/palette-inspiration.md](references/palette-inspiration.md). Keep candidate palettes separate from registered themes; this route does not require a cover set.

Route visual production requests into one of two production branches:

1. **Cover branch**: communication-led main covers, article headers, blog covers, secondary covers, joined previews, and optional article landscape visuals. Build around headline hierarchy and one supporting visual claim.
2. **Article-body screenshot branch**: evidence-led illustrations that combine 2–4 real screenshots from one business scene. Build around labeled screenshot cards and one short explanatory sentence, without a cover headline.

Within either branch, keep theme, layout, and content/evidence as independent layers.

Do not merge theme values into layout coordinates. Do not stretch one finished image into another ratio.

## Load references

For every production task:

1. Read [references/theme-recipes.md](references/theme-recipes.md) and select one registered theme.
2. Read [references/layout-recipes.md](references/layout-recipes.md) for the requested WeChat image type.
3. Read [references/production-rules.md](references/production-rules.md) before assembling assets or exporting.
4. For the cover branch or a loosely specified topic, read [references/content-orchestration.md](references/content-orchestration.md) and derive the copy hierarchy before choosing layouts.
5. For the article-body screenshot branch, read [references/article-screenshot-collage.md](references/article-screenshot-collage.md) and classify reference images separately from actual screenshots.
6. Start from the matching file in `assets/starter/`; copy the entire starter folder into the delivery project before editing.

## Gather inputs

For an article-to-visual-set request, follow the confirmation workflow in `references/content-orchestration.md`: infer one recommended direction, present the copy, visual assets, theme and purpose/size list, and wait for the user's confirmation before production. An already approved direction or an explicit instruction to proceed counts as confirmation. After confirmation, export the agreed set without asking about each size. A scoped revision or size-only export uses the existing approved direction.

Determine:

- usage purpose and required pixel dimensions as separate fields; a main cover and article header can both be 1800×766;
- production branch;
- headline and support line for covers, or card labels and one explanatory sentence for article-body collages;
- whether a real product screenshot is available;
- which supplied images are reference context and which are actual output evidence;
- screenshot claim and preferred crop;
- selected theme or permission to choose the default;
- delivery folder.

For a customer-case person cover, also determine whether the real subject's gaze or gesture points left or right. Place the copy in that direction whenever practical. Never flip a photo that contains readable screens, logos, or asymmetric real-world evidence merely to force the preferred direction.

Ask only when a missing choice changes the content claim or output type. Never invent product UI, data, endorsements, or results.

When the user supplies a topic but does not prescribe every line of copy, make the editorial decisions yourself. In the cover branch, infer the central claim, supporting angle, concise secondary-cover label, and one emphasized phrase. In the article-body branch, infer only concise card labels, one factual explanatory sentence, and one emphasized phrase; do not invent a cover title or performance claim.

## Produce a complete set

Unless the user narrows the request, treat “use this topic/theme to make a WeChat visual set” as:

1. 公众号头条封面 / main cover: `1800 × 766`, simplified content with space for the platform title;
2. 公众号正文头图 / article header: `1800 × 766`, fuller information with no platform-title reservation;
3. 博客封面 / blog cover: `900 × 540`;
4. 次条方形图 / secondary cover: `766 × 766`;
5. 头条＋次条拼接图 / main-plus-secondary composite: `2566 × 766`, using the main-cover version, not the article header.

Add a `1920 × 1080` article landscape visual, screenshot illustrations or GIFs only when requested or included in the confirmed scope. The 16:9 size does not define “头图”.

Keep the set visually consistent while recomposing content separately for each format. Do not block the cover set merely because article screenshots have not yet been provided; finish the cover assets and state what screenshot input remains.

Even at identical dimensions, compose main covers and article headers separately. Main covers prioritize a short theme and essential subject in the safe area; article headers may retain approved co-brand logos, a full headline, a real person and their introduction, or a subtitle. Use only supported information. Logo removal and upward title movement are task-specific options, not universal requirements.

## Produce the cover branch

1. Copy `assets/starter/` as one complete project folder.
2. Put every supplied bitmap or vector under that project's `assets/` directory.
3. Use only relative references such as `assets/product-shot.png`.
4. Select the layout through its HTML starter and the theme through `data-theme`.
5. Keep visible Chinese text in HTML/CSS.
6. Keep screenshots proportional. Crop with an overflow viewport; never distort them.
7. For a customer-case person cover, use `main-cover-customer-case.html`; keep the real scene full-height on one side and the centered, left-aligned copy group on the other.
8. For a blog cover, use `blog-cover.html`; render directly at `900 × 540` and inspect it again at `450 × 270`.
9. Render at the exact production dimensions.
10. Run `scripts/validate_portability.py <project-folder>`.
11. Inspect the PNG at full size and thumbnail size; revise until both are clear.

For the `1800 × 766` article header, start from `article-header.html` or adapt the approved person/text composition to the header purpose. Inspect its complete composition without a simulated platform title. For the main cover, additionally inspect a temporary preview with the actual article title overlaid; export the clean artwork without that simulated title.

## Produce the article-body screenshot branch

1. Treat explicit reference images as layout/context only and exclude them from the output.
2. Group 2–4 actual screenshots from the same business scene into one illustration. Do not merge unrelated scenes merely to fill a row.
3. Copy `assets/starter/` as one complete project folder and use `article-screenshot-collage.html` as the starting file.
4. Copy actual screenshots into the project's `assets/` directory and replace the placeholder references with relative paths.
5. Use `light-blue` by default. Keep the page to screenshot cards plus one bottom explanation box; omit title badges, large headlines, side modules, arrows, grids, and decorative diagrams.
6. Preserve every screenshot's aspect ratio. Use `object-fit: contain` by default; use intentional cropping only when the focal UI remains complete and legible.
7. Render a `1920 × 1080` master PNG. Also export a compact cropped PNG that removes unused outer background while preserving roughly `30–50px` of breathing room.
8. When the user requests an animation, first normalize the approved static scene images to one size, then create a looping GIF; default to `2.5s` per frame and preserve the static PNGs.
9. Run `scripts/validate_portability.py <project-folder>` and inspect the master and compact output at full and thumbnail size.

## Defaults

- Use `dark-spectrum` for the cover branch when the user does not specify a theme.
- Use `light-blue` for explanatory article-body screenshot collages unless the user requests another registered theme.
- Use the system font stack defined by the starter CSS.
- Use one theme per image set.
- Use one emphasized phrase per headline or support line.
- For an explicit before/after customer-case headline, the paired terms may each use the same gradient treatment as one contrast device.
- Make screenshot framing colors, borders, shadows, and surrounding background follow the selected theme; blue–purple is one recipe, not a universal screenshot background.
- When WeChat will overlay dark title text, use a pale lower area without a mask.
- When WeChat will overlay white title text, use the starter with a soft bottom title-zone scrim. Do not place that scrim behind the designed left-side copy.
- Use top-only screenshot corner rounding when the screenshot intentionally continues below the canvas; otherwise round all visible corners.
- Remove arrows, cursors, glows, grids, and decorative marks unless the user explicitly asks for them.
- For a customer-case person cover, default the category line to `标杆客户案例`, omit the explanatory subtitle, and use `dark-spectrum` unless the user requests another registered theme.
- For an article-body collage, use one short system/platform label per card and one bottom explanation sentence with at most one emphasized phrase.

## Deliver

Provide:

- final PNG files named by purpose and dimensions; distinguish `公众号头条封面-1800x766.png` from `公众号正文头图-1800x766.png`;
- the `900 × 540` blog cover whenever it belongs to the requested cover set;
- both the `1920 × 1080` master and compact cropped PNG for an article-body collage;
- the GIF plus retained static scene PNGs when animation is requested;
- editable HTML/CSS;
- the complete portable asset folder;
- validation result;
- a short note for any deliberate crop or missing source asset.

## Maintenance entry

- Use this installed skill directory as the single maintained source for both production and updates. Update its instructions, templates and palette library directly when requested; do not create or require a parallel development copy.
- Validate changed data and affected previews after each update. Preserve unrelated templates and settings. For template or theme changes, run portability and relevant visual checks; palette-only additions do not require re-rendering unchanged templates.
- Keep temporary checks and generated test screenshots outside the installed skill. GitHub publishing is a separate requested action, not an automatic consequence of a local update.
