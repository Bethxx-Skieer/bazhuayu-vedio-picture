# Octopus Blue theme

Use this as the default theme for Octoparse RPA Xiaohongshu images.

## Brand tokens

- primary blue: `#0055FF`;
- secondary interface blue: `#1689FF`;
- headline ink: `#14213D`;
- body text: `#34415C`;
- muted text: `#72809A`;
- success: `#159A67`;
- light background: ice blue-white gradients;
- primary surface: pure white or restrained translucent white.

Use one semantic accent only when needed: orange for a human action or green for completion. Do not turn all labels, arrows, and modules blue.

## Typography

Use `PingFang SC`, `Microsoft YaHei`, or `Noto Sans SC` with a system fallback. Keep visible Chinese text in HTML.

- cover headline: two manually controlled lines, normally `88–120px`;
- subtitle or product line: normally `44–60px`;
- content-page title: normally `52–72px`;
- supporting copy: normally `28–38px`;
- small labels and pills: normally `22–28px`.

Use whitespace and weight before adding decorative effects.

## Fixed elements

- Place the official blue horizontal logo in the top-right safe slot.
- Registered co-branded collaboration templates may instead use one approved joint brand lockup in the top-left safe area and omit the duplicate top-right logo.
- Use one obvious focal point.
- Keep the background quiet and preserve large readable title zones.
- Use real screenshots as evidence, not decoration.
- Prefer original approved Octopus IP assets over unstable regenerated variants.
- Use `assets/templates/octopus-blue/assets/octopus-3d-work-neutral.png` as the fixed 3D IP for generic work scenes. Event-specific variants belong in the source IP library and must be copied into a project only when explicitly required.

## Surfaces

- Use pure-white cards on ice blue backgrounds.
- Separate white speech bubbles with a subtle blue-to-white gradient edge or broad low-opacity blue shadow.
- Keep glass/IP speech-bubble interiors near white (`#FFFFFF` to pale ice blue), never medium gray. Increase separation with a pale brand-blue edge and soft blue glow rather than a darker fill.
- Build speech bubbles and tails as one CSS/SVG path.
- Do not stack several glass layers until boundaries disappear.

## Current production status

The registered starter contains nine production templates: screenshot cover, atmosphere cover, hand-drawn IP cover, 3D glass IP cover, WorkBuddy collaboration IP cover, co-branded screenshot cover, generated business-scene IP cover, product-demo video cover, and standard explanatory inner page. The IP collaboration cover uses independent background, computer, real screenshot, and two-IP layers. The co-branded screenshot cover omits mascots and keeps both brands, the centered computer, and the real screenshot as separate layers. Reuse them before inventing new compositions.
