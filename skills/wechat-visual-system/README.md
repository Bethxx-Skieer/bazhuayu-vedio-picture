# 微信视觉生产 Skill（wechat-visual-system）

双端兼容技能包：同一份内容同时供千问办公与 WorkBuddy 加载使用。用于制作微信公众号头条封面、博客封面、客户案例人物封面、次条图、文章头图，以及由真实截图组成的正文配图与 GIF。

## 双端加载方式

| 端 | 加载依据 |
| --- | --- |
| 千问办公 | `SKILL.md` 双语 frontmatter（`name_en/name_zh/description_en/description_zh`）与 `.skill-metadata.yaml` 示例库 |
| WorkBuddy | `SKILL.md` 的 `name`、`description` 与 `agents/openai.yaml` |

两端共享同一份主题、母板、参考规范与校验脚本。修改能力边界时，应同步维护双语元数据和两端入口。

## 安装

### 千问办公

把 `wechat-visual-system/` 整个目录复制到：

- Windows：`%USERPROFILE%\.qwenworkcn\skills\`
- macOS / Linux：`~/.qwenworkcn/skills/`

安装后入口应为：

```text
~/.qwenworkcn/skills/wechat-visual-system/SKILL.md
```

### WorkBuddy

把 `wechat-visual-system/` 整个目录复制到：

- macOS / Linux：`~/.codex/skills/`
- Windows：`%USERPROFILE%\.codex\skills\`

安装后入口应为：

```text
~/.codex/skills/wechat-visual-system/SKILL.md
```

## 主要能力与尺寸

- 公众号头条封面：`1800 × 766`，精简内容并预留平台标题空间
- 公众号正文头图：`1800 × 766`，信息更丰富，不预留平台标题区
- 博客封面：`900 × 540`
- 公众号次条图：`766 × 766`
- 可选正文横图：`1920 × 1080`，按需追加
- 头条与次条直接拼接预览：`2566 × 766`
- 客户案例人物型头条封面
- 正文多截图配图：`1920 × 1080` 母版与紧凑裁切版
- 截图型循环 GIF，并保留静态 PNG

提供文章后，先推断视觉类型并推荐文案、素材、主题及用途/尺寸清单。用户确认一次后，自动输出约定系列，无需逐张确认。默认五项为头条封面、正文头图、博客封面、方形图和头条＋方形拼接图；用户只要部分尺寸时按指定范围执行。

用途与尺寸分别记录：即使头条封面与正文头图同为1800×766，也要分别排版。封面用实际文章标题叠加预览检查安全区，头图检查完整信息层级；拼接图使用头条封面版。不同画幅独立重排，不拉伸现有成品。

## 包内包含

- 主 Skill 与内容、主题、布局、生产和截图拼图参考规范（`references/`）
- 7 套注册主题
- 配色灵感库：打开 `assets/palette-inspiration/index.html` 浏览，包含色号、渐变预览和取样证据；公开版不包含来源不明的原始参考截图
- 头条、博客、客户案例、次条、文章头图和正文截图拼图 HTML/CSS 母板（`assets/starter/`）
- 自适应文字脚本、可移植性检查与紧凑裁切脚本（`scripts/`）
- 千问办公示例库（`.skill-metadata.yaml`）与 WorkBuddy UI 入口（`agents/openai.yaml`）

## 使用边界

- 中文标题和说明文字使用 HTML/CSS，不交给图片生成模型绘制
- 产品截图、人物照片、Logo 和业务结果必须使用真实素材，不得伪造
- 同一视觉套图只使用一个注册主题
- `1080 × 1440` 小红书图文属于独立的 `xhs-visual-template-system`
- 微信公众号长文 HTML 排版属于独立排版能力，不属于本 Skill

## 验证

当前以安装目录作为唯一维护源，新增配色和修改规范直接更新此目录，不再维护独立开发版。临时测试输出放在 Skill 目录外；GitHub 发布另行执行。配色数据更新后运行 `node scripts/build_palette_catalog.cjs` 重新生成目录。

安装或修改后检查：

```text
wechat-visual-system/SKILL.md
wechat-visual-system/.skill-metadata.yaml
wechat-visual-system/agents/openai.yaml
wechat-visual-system/references/theme-recipes.md
wechat-visual-system/references/layout-recipes.md
wechat-visual-system/assets/starter/blog-cover.html
wechat-visual-system/scripts/validate_portability.py
```

对交付项目运行：

```bash
python3 scripts/validate_portability.py <project-folder>
```
