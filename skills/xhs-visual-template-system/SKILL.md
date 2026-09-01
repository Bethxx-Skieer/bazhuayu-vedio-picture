---
name: xhs-visual-template-system
name_en: Xiaohongshu Visual Template System
name_zh: 小红书视觉模板生产系统
description: Plan, build, export, and audit reusable 1080×1440 Xiaohongshu visual systems from topics, articles, product facts, screenshots, brand assets, and user value. Use for Xiaohongshu covers, image-text pages, screenshot-evidence pages, process pages, pain-point comparisons, feature collections, IP dialog covers, dual-IP collaboration covers, co-brand screenshot covers, 3:4 product-demo video covers, Octoparse RPA Xiaohongshu visuals, and reusable HTML/CSS social-image templates. Do not use for WeChat Official Account long-form article formatting or copy-paste HTML; that belongs to the separate gzh-design-skill.
description_en: Plan, build, export, and audit reusable 1080×1440 Xiaohongshu visual systems from topics, articles, product facts, screenshots, brand assets, and user value; covers, image-text sets, evidence pages, comparisons and 3:4 product-demo video covers with registered themes and HTML/CSS templates.
description_zh: 围绕选题、文章、产品事实、真实截图、品牌资产和用户价值，规划、搭建、导出并审计可复用的 1080×1440 小红书视觉系统。适用于小红书封面、小红书图文、内容页、截图证据页、流程页、痛点对比页、功能合集、IP 对话封面、双IP协作封面、联合品牌截图封面、3:4产品演示视频封面、八爪鱼 RPA 小红书视觉，以及可复用的 HTML/CSS 社媒图模板。不用于微信公众号长文排版或复制粘贴式 HTML；公众号排版属于独立的 gzh-design-skill。
argument-hint: Provide topic/article/product facts/screenshots/brand assets, state the deliverable (cover / image set / video cover) and the delivery folder
argument-hint-en: Provide topic/article/product facts/screenshots/brand assets, state the deliverable (cover / image set / video cover) and the delivery folder
argument-hint-zh: 附上选题/文章/产品资料/截图/品牌资产，说明要产出什么（封面 / 图文组 / 3:4视频封面）以及交付目录
user-invocable: true
version: 1.0.0
---

# Official Brand Visual Production

本文件 `name`+`description` 与 `agents/openai.yaml` 供 WorkBuddy 加载，双语元数据与 `.skill-metadata.yaml` 供千问办公加载，两端共享同一份模板、规范与校验闸门。

## Operating model

Build with four layers:

1. brand kernel: official logo, primary color, typography, spacing, screenshot ethics, and export quality;
2. registered theme: background, surfaces, accent balance, and component skin;
3. semantic components: title, process, screenshot, comparison, feature, result, CTA, and media placeholder;
4. page and image-set recipes: allowed component combinations for each communication job.

Keep the brand kernel stable. Use one registered theme for an entire image set. Vary composition through page recipes. Never improvise a new palette or mix themes page by page.

Prefer HTML/CSS for text-dense graphics. Use generated imagery only for atmosphere or illustration. Keep visible Chinese text in HTML.

This skill is independent from `gzh-design-skill`. Never load, alter, or migrate WeChat long-form components while producing Xiaohongshu images.

## Load the right resources

For every production task:

1. Read [references/theme-index.md](references/theme-index.md) and select one active theme. Use the default unless the user requests another active theme.
2. Read the selected theme file listed in the index.
3. Read [references/component-library.md](references/component-library.md) for component semantics, limits, and asset states.
4. Read [references/page-recipes.md](references/page-recipes.md) before storyboarding or choosing components.
5. Read [references/copy-rules.md](references/copy-rules.md) before writing visible copy.
6. Read [references/design-rules.md](references/design-rules.md) for global logo, screenshot, canvas, and export constraints.
7. For Octoparse work, read [references/theme-octopus-blue.md](references/theme-octopus-blue.md), [references/octopus-template-index.md](references/octopus-template-index.md), and [references/production-learning.md](references/production-learning.md).
8. When `封面-IP-业务场景.html` is selected, also read [references/image-generation-scenario-cover.md](references/image-generation-scenario-cover.md) before generating the background.

Use [references/layout-patterns.md](references/layout-patterns.md) only when auditing legacy work or translating an old layout into the new recipe system.

## Gather inputs

Extract or reasonably infer:

- topic, intended audience, and channel;
- official account identity and product name;
- product facts, application link, and allowed CTA;
- single most important user value;
- screenshots and the exact claim each proves;
- count, ratio, dimensions, and delivery folder.

Ask only when a missing fact would materially change the claim or screenshot meaning. Never invent capabilities, numbers, customer results, endorsements, UI states, or platform support.

## Storyboard before assembly

Assign every page one primary job:

- main-value cover;
- pain-point comparison;
- process explanation;
- screenshot evidence;
- feature collection;
- large-type atmosphere;
- scenario explanation cover;
- result or next-step page.
- 3:4 product-demo video cover.

Use the shortest image-set recipe that completes the argument. For each page record the job, one message, headline, evidence, screenshot role, and reader takeaway. If the one-message field contains “and,” consider splitting it.

## Select components by recipe

Start from the selected page recipe. Use only its required components and allowed options.

- Do not choose components only because they look attractive.
- Do not repeat the same hero or card grid on every page.
- Do not use more component types than the recipe allows.
- Keep one obvious focal point.
- Keep blue modules within the selected theme’s area and frequency limits.
- Use platform colors only as semantic identifiers beneath the official brand hierarchy.

Copy the selected starter files from `assets/templates/<theme-id>/` into the output project. Copy the official logo beside the delivered HTML and keep all asset paths relative.

For short-term Octoparse production, adapt an existing registered template before creating a new one. Add a template only when the current set cannot express the page job without structural distortion.

When a partner or customer cover is led by a real screenshot rather than mascot interaction, use `封面-联合品牌-截图.html`. Keep the Octoparse identity, partner logo and name, computer shell, real screenshot, headline, and value band as separate replaceable layers. Use `封面-IP-合作.html` only when the two approved mascots are themselves part of the message.

For a scene-heavy cover that must explain several tables, objects, or states, use `封面-IP-业务场景.html`. Follow its dedicated generation rule, generate one coherent 3:4 atmosphere image, overlay the headline and support line in HTML, then attach 2–4 HTML callouts to their exact scene targets.

For a 3:4 product-demo video cover, start from the standalone `封面-视频演示.html`. Replace the title and real proof image without introducing a separate video-inner-page workflow.

## Handle screenshots and missing images

Treat screenshots as evidence, not decoration.

When a screenshot exists:

1. identify the claim;
2. crop the smallest region that proves it while retaining context;
3. remove or obscure personal data;
4. use the real-image component;
5. add at most one primary callout and one secondary annotation.

When a required screenshot or image is missing:

1. use the `media-placeholder` component from the component library;
2. state the exact required asset and what it must prove;
3. preserve the planned aspect ratio and page structure;
4. add `data-asset-state="missing"` to the placeholder;
5. report the missing asset at delivery.

Never fabricate a product screenshot. A placeholder is a production state, not a visual failure.

## Build and export

1. Default to `1080 × 1440` for Xiaohongshu portrait cards and 3:4 video canvases.
2. Use CSS variables from the selected theme. Do not replace them with ad hoc colors.
3. Use semantic sections and reusable classes from the starter CSS.
4. Reserve the fixed logo slot before arranging the title.
5. Keep each page independently exportable.
6. Render every HTML at the exact viewport.
7. Run `scripts/validate_visual_template.py` on the output project.
8. Inspect rendered PNGs at full size and as a thumbnail montage.
9. Revise and rerender until both deterministic checks and visual audit pass.

During revision, change one system variable at a time and inspect the assembled page. If a component accumulates compensating offsets, cover-up layers, or pseudo-elements, redraw it with one coordinate system instead of adding another patch.

## Visual audit

Reject or revise when any answer is no:

- Is the one main message understandable in about one second?
- Is the focal point obvious at thumbnail size?
- Does every card, arrow, icon, pill, and color improve understanding?
- Does each screenshot prove the adjacent statement?
- Is important copy readable on a phone preview?
- Are margins and vertical rhythm balanced?
- Is the blue-module amount within the active theme’s limits?
- Does the set vary page structure while remaining one system?
- Is the official logo present in the fixed slot, unless the registered 3:4 video-cover template explicitly omits it?
- Are all assets portable and technically clean?

## Evolve the system

When repeated real usage reveals a stable need:

1. extract a semantic component or recipe from successful outputs;
2. add it to the active theme starter and component reference;
3. add or update a validation case;
4. render the component gallery and a realistic image set;
5. register a new theme only when color, density, surface, and composition grammar all differ—not for a minor palette variation.

Keep validated source assets intact, but do not retain duplicate legacy template workpacks inside the installed skill.

## Deliver

Provide:

- storyboard and chosen theme;
- final HTML and PNG files;
- a thumbnail montage;
- validation result;
- missing-asset list, if placeholders remain;
- a short note for deliberate exceptions or newly tested components.

## Maintenance entry

- Use the installed copy for normal production tasks.
- When the user explicitly asks to record a problem, iterate, or update this skill, create or locate a separate local development project, record its current state, and modify only that project's `skill/` copy during development and validation.
- Do not publish the development copy to the installed directory until regression checks pass.
