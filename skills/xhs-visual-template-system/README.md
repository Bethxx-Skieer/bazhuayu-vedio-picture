# 小红书视觉 Skill（xhs-visual-template-system）

双端兼容技能包：同一份内容同时供千问办公与 WorkBuddy 加载使用。用于制作和审计 1080×1440 小红书封面、图文内容页、截图证据页、流程页、对比页、功能合集和 3:4 产品演示视频封面。

## 双端加载方式

| 端 | 加载依据 |
| --- | --- |
| 千问办公 | SKILL.md 双语 frontmatter（`name_en/name_zh/description_en/description_zh`）+ `.skill-metadata.yaml` 示例库 |
| WorkBuddy | SKILL.md `name`+`description` + `agents/openai.yaml` |

两端共享同一份模板、主题、参考规范与校验脚本，不要只改其中一端的元数据。

## 安装

### 千问办公

把 `xhs-visual-template-system/` 整个目录复制到：

- Windows：`%USERPROFILE%\.qwenworkcn\skills\`
- macOS / Linux：`~/.qwenworkcn/skills/`

安装后最终路径应为：

```text
~/.qwenworkcn/skills/xhs-visual-template-system/SKILL.md
```

### WorkBuddy

把 `xhs-visual-template-system/` 整个目录复制到：

- macOS / Linux：`~/.codex/skills/`
- Windows：`%USERPROFILE%\.codex\skills\`

安装后最终路径应为：

```text
~/.codex/skills/xhs-visual-template-system/SKILL.md
```

## 包内包含

- 主 Skill 与全部分阶段参考规范（references/）
- `octopus-blue` 与 `hr-light-tech` 两套注册主题
- 小红书封面、内页、截图和视频封面 HTML/CSS 模板（assets/templates/）
- 八爪鱼品牌 Logo、IP 和模板所需图片资产（assets/）
- 模板导出脚本与视觉校验脚本（scripts/）
- 组件图库、模板总览和验证样例（examples/）
- 千问办公示例库（`.skill-metadata.yaml`）与 WorkBuddy 接口（`agents/openai.yaml`）

## 目标电脑还需要

- 千问办公或 WorkBuddy（Codex），用于加载和执行 Skill
- Node.js，用于运行 HTML 模板导出脚本
- Python 3，用于运行视觉模板校验脚本
- Chrome 或 Chromium，用于按 1080×1440 渲染 HTML
- 若使用业务场景生成封面，还需要可用的图片生成能力

这些是运行工具，不会因为复制 Skill 自动安装。

## 使用边界

- 小红书文字密集画面优先使用 HTML/CSS，中文文字不要交给图片生成模型绘制
- 产品截图必须使用真实截图，不得伪造
- 一个图文组只使用一个注册主题，不要逐页更换配色体系
- 微信公众号长文排版不属于本 Skill，应使用独立的公众号排版能力

## 验证

安装后可检查：

```text
xhs-visual-template-system/SKILL.md
xhs-visual-template-system/.skill-metadata.yaml
xhs-visual-template-system/agents/openai.yaml
xhs-visual-template-system/references/theme-index.md
xhs-visual-template-system/assets/templates/octopus-blue/
xhs-visual-template-system/scripts/validate_visual_template.py
```
