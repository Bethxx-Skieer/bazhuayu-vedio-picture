# bazhuayu-vedio-picture

团队技能仓库：视频封面与视觉资产类技能。

## 技能清单

| 技能 | 说明 | 兼容端 |
| --- | --- | --- |
| [skills/xhs-visual-template-system](skills/xhs-visual-template-system/) | 1080×1440 小红书封面、图文内容页、截图证据页、痛点对比页、功能合集与 3:4 产品演示视频封面的模板生产系统（octopus-blue / hr-light-tech 两套注册主题） | 千问办公 + WorkBuddy 双端 |
| [skills/wechat-visual-system](skills/wechat-visual-system/) | 微信公众号头条封面、正文头图、博客封面、客户案例人物封面、次条图与截图拼图/GIF 的视觉系统（7 套注册主题） | 千问办公 + WorkBuddy 双端 |

## 安装

把对应技能目录整个复制到：

- 千问办公：`%USERPROFILE%\.qwenworkcn\skills\`（macOS/Linux：`~/.qwenworkcn/skills/`）
- WorkBuddy：`%USERPROFILE%\.codex\skills\`（macOS/Linux：`~/.codex/skills/`）

详细说明见各技能目录内 README.md。

## 双端格式约定

与 bazhuayu-vedio-cut 仓库的 tutorial-video-slicing-workflow 一致：

- WorkBuddy：SKILL.md `name`+`description` + `agents/openai.yaml`
- 千问办公：SKILL.md 双语 frontmatter（`name_en/name_zh/description_en/description_zh` 等）+ `.skill-metadata.yaml` 示例库
- 两端共享同一份模板、规范与校验脚本；修改规范时不要只改其中一端的元数据

## 注意

视频/图片等大文件应放技能 assets 内必要最小集；勿向仓库塞成片或临时产物。
