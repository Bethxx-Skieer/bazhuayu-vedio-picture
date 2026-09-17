# Article-body screenshot collage

Use this branch for 微信文章内部配图、多张实际截图整合、流程截图集合、系统页面对比或截图型动图. The screenshots are evidence; the surrounding visual only organizes and explains them.

## 1. Classify inputs

- Exclude any image the user calls “参考图”“参考上下文” or otherwise marks as layout guidance.
- Include only images the user identifies as originals or final source screenshots.
- Follow an explicit folder naming convention from the user, such as `参考*` for context and `image (N)` for originals. Do not assume such a convention outside that task.
- When the user corrects the file set, replace the prior assets immediately and stop using the superseded files.
- Inspect every actual screenshot before layout. Identify the system/platform name, focal UI, aspect ratio, sensitive information, and whether the screenshot can be cropped safely.

## 2. Editorial structure

Build only two levels:

1. screenshot cards with concise labels such as “千牛后台”“伯俊 ERP”“支付宝对账中心”;
2. one bottom explanation sentence describing why the screenshots belong together.

Do not add a category badge, large cover title, secondary subtitle, CTA, decorative side panel, or extra results card.

Write the explanation as a factual scene statement. A useful pattern is:

`[数据或任务]分散在[多个系统]中，[角色]需要[连续动作]。`

Keep it to one sentence, normally `24–42` Chinese characters, and emphasize only one phrase. Do not invent efficiency figures, accuracy rates, endorsements, or business outcomes.

## 3. Layout recipes

Always build a `1920 × 1080` master first. Use a pale `light-blue` background, white cards, restrained blue borders/shadows, blue labels, and one white explanation box.

### Two screenshots

- Outer left/right: about `100px`.
- Grid width: about `1720px`.
- Gap: about `35px`.
- Prefer wider cards and preserve each screenshot at its natural ratio.

### Three screenshots

- Grid: `3` equal columns, `1720px` wide, about `35px` gaps.
- Top: about `80px`; card height: about `500px`.
- Media area: about `402px`; label area: about `96px`.
- Explanation: `1700px` wide, about `50px` below the cards, at least `150px` high.

### Four screenshots

- Grid: `4` equal columns, `1810px` wide, about `28px` gaps.
- Left/right outer margin: about `55px`; top: about `80px`.
- Card height: about `470px`; media area: about `376px`; label area: about `92px`.
- Explanation: `1700px` wide, about `50–60px` below the cards, at least `146px` high.

Use consistent side margins and inter-card gaps. Keep the explanation box centered. When actual screenshots have very different ratios, keep card geometry consistent but use internal whitespace instead of stretching images.

## 4. Screenshot treatment

- Use `object-fit: contain` by default so the whole screenshot remains visible.
- Use `object-fit: cover` or an overflow crop only when the crop is deliberate and does not remove the focal UI, system identity, or evidentiary content.
- Never stretch screenshots to unrelated width and height values.
- Do not recreate or beautify product UI. Preserve supplied pixels.
- Remove or mask personal data only when needed; do not expose account details.
- Keep labels outside screenshots so they remain readable at WeChat thumbnail size.

## 5. Compact crop

The `1920 × 1080` master preserves a reusable editing canvas but often contains unused lower background. Unless the user asks for the untouched master only, also deliver a compact crop.

- Crop only outer background; never crop cards, shadows, captions, or the explanation box.
- Preserve roughly `30–50px` at the top and sides and `40–70px` below the explanation box.
- Use `scripts/crop_article_collage.py` with the screenshot count as a baseline, then inspect and adjust the crop box if the layout changed.
- Keep the full master. Never overwrite it with the cropped file.

## 6. Animation

Use animation only when the user wants several approved static scene illustrations shown in one asset.

- Normalize all frames to the same dimensions before encoding.
- Default to `2.5s` per frame, infinite loop, and no transition effect.
- Keep text and card positions stable across frames.
- Preserve the individual static PNGs and the uncropped source GIF when creating a tighter derivative.

## 7. Delivery

Deliver a portable folder containing HTML/CSS, copied screenshots under `assets/`, a `1920 × 1080` master PNG, and a compact cropped PNG. Add a GIF only when requested. Report any deliberate screenshot crop or excluded reference image.
