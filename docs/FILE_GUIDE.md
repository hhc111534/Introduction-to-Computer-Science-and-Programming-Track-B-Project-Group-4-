# 文件说明与分工

本文件逐项说明仓库中的空占位文件，并标明负责人和后续填写内容。当前共有 **44 个空文件**，其余为已经写入基础内容的配置文件。

## 负责人代号

| 代号 | 角色 | 主要负责范围 |
|---|---|---|
| A | PDF 与数据 | PDF 解析、清洗、页码映射、文本层质量检测、测试论文 |
| B | 模型与摘要 | 大模型客户端、Prompt、摘要、引用校验 |
| C | 术语与检索 | 上下文、全文检索、术语解释、可选联网搜索 |
| D | 界面与集成 | Flask 页面、路由、划词、集成、文档、演示 |
| All | 全员 | 需要共同确认的共享文件 |

> 共享文件（`paperlens/common/`、`docs/`）由 D 负责维护，但涉及接口变更时必须由 A/B/C 中受影响的一方 Review。

## 根目录

| 文件 | 用途 | 负责人 | 后续填写内容 |
|---|---|---|---|
| `app.py` | Flask 启动入口 | D | 创建应用、注册路由、启动开发服务器 |
| `config.py` | 项目配置 | D | 上传大小、页数限制、模型配置入口；不要写真实 Key |
| `requirements.txt` | 运行依赖 | D | Flask、PyMuPDF、OpenAI SDK、Pydantic 等 |
| `requirements-dev.txt` | 开发依赖 | D | pytest、pytest-cov、ruff 等 |

## PDF 模块（A）

| 文件 | 用途 | 负责人 | 后续填写内容 |
|---|---|---|---|
| `paperlens/pdf/__init__.py` | PDF 包入口 | A | 导出 `extract_pdf` 等公共函数 |
| `paperlens/pdf/extractor.py` | PDF 文本提取 | A | 使用 PyMuPDF 提取页码、段落、文本块 |
| `paperlens/pdf/cleaner.py` | 文本清洗 | A | 去页眉页脚、合并断行、规范空白字符 |
| `paperlens/pdf/quality.py` | 文本层质量检测 | A | 统计每页字符数，识别扫描件并给出错误信息 |

## AI 与摘要模块（B）

| 文件 | 用途 | 负责人 | 后续填写内容 |
|---|---|---|---|
| `paperlens/ai/__init__.py` | AI 包入口 | B | 导出客户端和摘要接口 |
| `paperlens/ai/client.py` | 大模型客户端 | B | OpenAI 兼容调用、超时、重试、异常转换 |
| `paperlens/ai/summary.py` | 摘要流程 | B | 分块、逐块提取、汇总摘要、页码引用 |
| `paperlens/ai/schemas.py` | 模型输出结构 | B | Pydantic 模型：摘要、术语解释、引用 |

## 术语与检索模块（C）

| 文件 | 用途 | 负责人 | 后续填写内容 |
|---|---|---|---|
| `paperlens/terms/__init__.py` | 术语包入口 | C | 导出术语解释接口 |
| `paperlens/terms/context.py` | 选区上下文 | C | 根据词语、页码、段落截取前后文 |
| `paperlens/terms/retrieval.py` | 全文相关段落检索 | C | 关键词检索或 BM25，返回相关段落及页码 |
| `paperlens/terms/search.py` | 可选联网搜索 | C | 搜索 API 封装、结果清洗、URL 和来源标注 |
| `paperlens/terms/explain.py` | 术语解释流程 | C | 组织上下文、调用模型、校验证据、返回解释 |

## Web 与界面模块（D）

| 文件 | 用途 | 负责人 | 后续填写内容 |
|---|---|---|---|
| `paperlens/web/__init__.py` | Web 包入口 | D | 注册蓝图或路由 |
| `paperlens/web/routes.py` | API 路由 | D | `/api/parse`、`/api/summarize`、`/api/explain`、`/api/health` |
| `paperlens/web/templates/base.html` | 页面基础模板 | D | 顶部栏、页脚、通用布局、静态资源引用 |
| `paperlens/web/templates/index.html` | 主页面 | D | 上传区、阅读区、摘要区、解释区 |
| `paperlens/web/static/css/app.css` | 页面样式 | D | 三栏布局、响应式、按钮和错误提示样式 |
| `paperlens/web/static/js/selection.js` | 划词交互 | D | 获取选区、定位页码、发送解释请求、展示结果 |

## 共享代码（D 维护，相关成员 Review）

| 文件 | 用途 | 负责人 | 后续填写内容 |
|---|---|---|---|
| `paperlens/__init__.py` | 应用包入口 | D | 应用工厂或包级初始化 |
| `paperlens/common/__init__.py` | 共享包入口 | D | 导出公共模型和异常 |
| `paperlens/common/models.py` | 核心数据结构 | D | `Document`、`Selection`、`Summary`、`Explanation` |
| `paperlens/common/errors.py` | 统一错误处理 | D | 自定义异常、API 错误码、用户可读提示 |
| `paperlens/common/cache.py` | 缓存 | D | 按 PDF 哈希和 Prompt 版本缓存结果 |

## Prompt（B/C）

| 文件 | 用途 | 负责人 | 后续填写内容 |
|---|---|---|---|
| `prompts/summary.md` | 摘要 Prompt | B | 摘要结构、引用规则、中文输出要求 |
| `prompts/explain.md` | 术语解释 Prompt | C | 上下文优先、来源分层、证据和置信度要求 |

## 测试

| 文件 | 用途 | 负责人 | 后续填写内容 |
|---|---|---|---|
| `tests/conftest.py` | 测试公共夹具 | D | 临时目录、Mock LLM、示例文档夹具 |
| `tests/fixtures/.gitkeep` | 测试文件目录占位 | A | 放入 1–2 篇小型公开论文，并注明来源和许可证 |
| `tests/test_pdf.py` | PDF 模块测试 | A | 文本层、扫描件、页码、清洗规则 |
| `tests/test_summary.py` | 摘要模块测试 | B | 分块、JSON 解析、引用校验、Mock 调用 |
| `tests/test_terms.py` | 术语模块测试 | C | 上下文截取、检索、歧义、来源校验 |
| `tests/test_api.py` | API 集成测试 | D | 上传、摘要、解释、错误码、无 Key 场景 |

## 脚本、文档与仓库配置

| 文件 | 用途 | 负责人 | 后续填写内容 |
|---|---|---|---|
| `scripts/inspect_pdf.py` | PDF 调试脚本 | A | 输入 PDF，输出每页字符数、文本块和提取结果 |
| `docs/proposal.md` | 项目提案 | All / D 汇总 | 放入最终英文或中文 Proposal |
| `docs/architecture.md` | 架构说明 | D | 模块边界、数据流、外部 API 调用关系 |
| `docs/api.md` | API 契约 | D | 请求/响应格式、错误码、示例 |
| `docs/data-model.md` | 数据模型 | D | 四个核心数据结构的字段和约束 |
| `data/uploads/.gitkeep` | 上传目录占位 | D | 保持空目录；实际文件不提交 |
| `data/cache/.gitkeep` | 缓存目录占位 | D | 保持空目录；实际缓存不提交 |
| `.github/ISSUE_TEMPLATE/task.md` | Issue 模板 | D | 任务目标、输入输出、验收标准、负责人 |

## 已写入基础内容的文件

以下文件不是空占位，已经包含基础说明或配置：

| 文件 | 用途 |
|---|---|
| `README.md` | 项目介绍、分工、目录结构、开发约定 |
| `.gitignore` | 忽略虚拟环境、密钥、论文、缓存等 |
| `.env.example` | 本地环境变量示例 |
| `AGENTS.md` | AI coding 工具的项目规则 |
| `docs/ai-usage.md` | AI 使用日志，成员本人填写 |
| `docs/logs-members.md` | 成员人工开发日志 |
| `docs/FILE_GUIDE.md` | 本文件，逐项说明空文件与负责人 |
| `.github/workflows/ci.yml` | 占位 CI，后续替换为真实测试 |
| `.github/pull_request_template.md` | PR 模板，包含 AI 使用声明 |

## 填写顺序建议

1. 先确定 `paperlens/common/models.py`、`docs/data-model.md` 和 `docs/api.md`。
2. 再分别实现 `pdf/`、`ai/`、`terms/` 三个模块。
3. 最后接入 `web/`，补测试、README 和演示。
4. 任何使用 AI 辅助完成的任务，都在 `docs/ai-usage.md` 中记录一行。
