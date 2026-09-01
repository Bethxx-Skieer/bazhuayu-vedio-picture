# Theme Registry

This file is the single source of truth for production themes. A theme may be used only when its status is `active` and both its reference file and starter directory exist.

| ID | Name | Status | Default | Visual character | Reference | Starter |
|---|---|---|---|---|---|---|
| `octopus-blue` | 八爪鱼冰蓝品牌视觉 | active | yes | 冰蓝留白、官方品牌蓝、白色或玻璃表面、真实截图证据、可选八爪鱼 IP | [theme-octopus-blue.md](theme-octopus-blue.md) | `assets/templates/octopus-blue/` |
| `hr-light-tech` | HR 蓝白轻科技 | active | no | 大面积蓝白留白、轻网格、白色信息卡、少量蓝色结构块，橙色表示动作，绿色表示完成 | [theme-hr-light-tech.md](theme-hr-light-tech.md) | `examples/hr-light-tech-validation-set/` |

## Selection rules

- Use `octopus-blue` for Octoparse RPA and the current official account.
- Use `hr-light-tech` only for HR recruiting automation or when explicitly requested.
- Use one theme for a complete image set. Never switch page by page.
- Platform colors may identify a platform or business object, but may not replace the theme hierarchy.
- A palette adjustment is not a new theme. Register a new theme only when background, surface, density, color balance, and composition grammar form a repeatable system.
- Planned themes stay outside this registry until they have variables, starter pages, a component gallery, a realistic validation set, and a passing audit.

## Registration gate

A new entry requires all of the following:

1. a complete theme reference;
2. a production CSS file with semantic tokens;
3. starter HTML for the core page jobs;
4. real screenshot and missing-media states;
5. component-gallery renders;
6. one realistic multi-page set;
7. passing structural validation and visual review.
