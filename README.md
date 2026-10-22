# PaperLens

**一个支持论文摘要与术语上下文解释的论文阅读助手。**

计算机 B 课程小组项目。当前仓库只有项目骨架，具体模块实现由小组后续补充。

## 小组分工

| 成员 | 负责模块 |
|---|---|
| A | PDF 解析、文本清洗、页码映射、文本层质量检测 |
| B | 大模型客户端、Prompt、摘要生成、引用校验 |
| C | 术语上下文、全文检索、术语解释、可选联网搜索 |
| D | Flask 页面、划词交互、模块集成、演示 |

> **请每位成员到 [`docs/TEAM_ROLES.md`](docs/TEAM_ROLES.md) 填写真实姓名，并确认自己承担的分工。**

## 仓库结构

```text
app.py                 Flask 启动入口
paperlens/
  pdf/                 PDF 解析与文本层质量检测
  ai/                  大模型客户端、摘要、输出结构
  terms/               上下文、检索、术语解释、联网搜索
  web/                 路由、页面模板、静态资源
  common/              共享数据结构、错误处理、缓存
prompts/               版本化的 Prompt 文件
tests/                 单元测试与集成测试
docs/                  项目提案、架构、API、数据模型、文件说明、AI 使用日志
data/                  本地上传文件与缓存（不提交到 Git）
.github/               CI、PR 模板、Issue 模板
```

每个空文件的用途、负责人和填写建议见 [`docs/FILE_GUIDE.md`](docs/FILE_GUIDE.md)。

## 当前进度

- [ ] 在 `requirements.txt` 中补充依赖
- [ ] 在 `docs/data-model.md` 中确定共享接口
- [ ] 实现 PDF 解析
- [ ] 实现摘要流程
- [ ] 实现术语解释
- [ ] 实现 Flask 页面与划词交互
- [ ] 完成测试、文档与演示

## AI 使用记录

所有 AI 辅助工作统一记录在 [`docs/ai-usage.md`](docs/ai-usage.md)。

- 每个 AI 辅助任务或 PR 记录一行；
- 由使用 AI 的成员本人填写；
- 由 Review 人确认代码已测试、可解释；
- 不得记录 API Key、未公开论文或个人隐私。

## 人工开发日志

所有成员的人工开发进展按时间顺序共同记录在 [`docs/logs-members.md`](docs/logs-members.md)，不按成员分开填写。

## 开发约定

- 每个模块由对应成员负责，跨模块修改需要提前沟通；
- 共享接口变更必须经过 Review；
- 所有改动通过分支和 Pull Request 合并，不直接 push `main`；
- 不提交 `.env`、真实 API Key、用户论文、缓存或数据库文件。
