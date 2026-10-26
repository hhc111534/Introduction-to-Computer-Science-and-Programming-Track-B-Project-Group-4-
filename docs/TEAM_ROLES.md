# 四人分工方案

> 请每位成员在本文件中填写自己的真实姓名，并确认自己承担的分工。确认后再开始各自模块的开发。

## 填写说明

1. 找到自己的成员代号 **A / B / C / D**。
2. 将“姓名”一列中的 `[待填写]` 替换为真实姓名。
3. 在“本人确认”一列中勾选 `[x]`。
4. 如果需要调整分工，先在小组内沟通，不要直接修改其他成员的内容。
5. AI 使用记录填写在 [`docs/ai-usage.md`](ai-usage.md)；人工开发进展填写在 [`docs/logs-members.md`](logs-members.md)。

## 分工总表

| 代号 | 姓名 | 主责模块 | 具体任务 | 适合交给 AI coding 的任务 | 本人确认 |
|---|---|---|---|---|---|
| A | [刘千钰] | PDF 与数据 | PDF 解析、文本清洗、页码映射、文本层检测、扫描件拒绝、测试论文收集；维护 `paperlens/common/models.py` | PyMuPDF 解析骨架、清洗函数、调试脚本、测试样本 | [yes] |
| B | [陈星宏] | 模型与摘要 | 大模型客户端、Prompt、分块、摘要、引用校验、Token/费用记录 | OpenAI 兼容客户端、重试与超时、JSON 解析、分块骨架、单元测试 | [yes ] |
| C | [丁周楠] | 术语与检索 | 选区上下文、全文检索、术语解释、缩写歧义处理、可选联网搜索 | 上下文截取、关键词检索、搜索 API 封装、输出结构、测试用例 | [yes] |
| D | [黄晨睿] | 界面与集成 | Flask 页面、路由、划词交互、错误处理、模块集成、API Key 安全、演示 | Flask 路由、HTML/CSS/JS、划词事件、错误页面、README 草稿 | [ yes] |

## 文件边界

| 成员 | 主要负责的文件 |
|---|---|
| A | `paperlens/pdf/`、`paperlens/common/models.py`、`tests/test_pdf.py`、`tests/fixtures/`、`scripts/inspect_pdf.py` |
| B | `paperlens/ai/`、`prompts/summary.md`、`tests/test_summary.py` |
| C | `paperlens/terms/`、`prompts/explain.md`、`tests/test_terms.py` |
| D | `app.py`、`config.py`、`paperlens/web/`、`paperlens/common/errors.py`、`paperlens/common/cache.py`、`tests/test_api.py`、`.github/`、`README.md` |
| 共享 | `docs/` 和 `paperlens/common/models.py` 的接口变更需要 A 与受影响成员 Review |

## 接口负责人

| 接口 | 负责人 | 说明 |
|---|---|---|
| `Document` | A | PDF 解析后的页面、段落、全文和哈希 |
| `Selection` | C | 用户选中的词语、页码、段落和前后文 |
| `Summary` | B | 摘要结构、页码引用和模型用量 |
| `Explanation` | C | 术语解释、原文证据、外部来源和置信度 |
| API 路由 | D | `/api/parse`、`/api/summarize`、`/api/explain`、`/api/health` |

## Review 配对

- A ↔ B
- C ↔ D
- D 负责最终合并

共享接口改动必须由接口负责人和至少一名受影响成员确认。

## AI 使用边界

- AI 可以生成代码草稿、测试、调试建议和文档草稿。
- AI 不负责决定接口和架构、处理 API Key、校验引用或 URL、批准合并。
- 每位成员必须能解释自己模块中的全部代码，包括 AI 生成的代码。
- 所有 AI 辅助任务都记录在 [`docs/ai-usage.md`](ai-usage.md)。

## 确认方式

每位成员填写完成后，在小组群说明“已填写并确认”，然后由 D 统一检查并合并。

```bash
git switch -c docs/team-roles-<你的名字>
# 编辑 docs/TEAM_ROLES.md
git add docs/TEAM_ROLES.md
git commit -m "docs: confirm team role for <你的名字>"
git push
```
