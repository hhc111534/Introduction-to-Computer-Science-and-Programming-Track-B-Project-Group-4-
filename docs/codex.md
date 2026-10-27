# 在 PaperLens 仓库中使用 Codex

本文档面向小组成员，说明如何在本仓库中安装、登录和使用 Codex CLI。Codex Cloud 的用法见文末。

## 1. Codex 会读取什么

Codex 启动时会自动读取：

- 仓库根目录的 `AGENTS.md`
- 当前工作目录到仓库根目录之间的 `AGENTS.md`
- 信任项目后，项目级 `.codex/config.toml`

本仓库已经配置：

```text
AGENTS.md                 Codex 项目规则
.codex/config.toml        项目级沙箱与审批设置
docs/architecture.md      架构说明
docs/data-model.md        数据模型
docs/TEAM_ROLES.md        四人分工
docs/ai-usage.md          AI 使用日志
```

修改 `AGENTS.md` 或 `.codex/config.toml` 后，重启 Codex 会话才会重新加载。

## 2. 安装 Codex CLI

### Windows PowerShell

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

### 使用 npm

```bash
npm install -g @openai/codex
```

安装后在终端确认：

```bash
codex --version
```

## 3. 首次登录

进入仓库根目录：

```bash
cd E:\ds-harness\paperlens_repo
codex
```

第一次运行：

1. 选择 **Sign in with ChatGPT**，按提示完成登录。
2. 如果提示是否信任当前项目，选择信任，这样 `.codex/config.toml` 才会生效。
3. 不要使用 `--yolo` 或 `danger-full-access`。

## 4. 第一次对话

先让 Codex 阅读规则，不要马上改代码：

```text
请先阅读 AGENTS.md、docs/architecture.md、docs/data-model.md 和 docs/TEAM_ROLES.md。
总结项目约束、我负责的模块，以及哪些文件不能直接修改。
暂时不要编辑任何文件。
```

确认它理解了模块边界后，再分配具体任务。

## 5. 推荐工作流

### 第一步：建分支

```bash
git switch -c feat/<your-task>
```

### 第二步：在对应模块目录启动

例如 A 负责 PDF：

```bash
codex --cd paperlens/pdf
```

B 负责摘要：

```bash
codex --cd paperlens/ai
```

C 负责术语：

```bash
codex --cd paperlens/terms
```

D 负责 Web：

```bash
codex --cd paperlens/web
```

### 第三步：给 Codex 一个范围明确的任务

示例：

```text
在 paperlens/pdf/extractor.py 中实现 extract_pdf()。
返回包含页码、文本块和全文的 Document。
增加文本层质量检测：字符数过低的页面提示疑似扫描件。
在 tests/test_pdf.py 中增加测试。
不要修改 paperlens/common/models.py，不要调用外部 API。
完成后运行 pytest 的 PDF 测试。
```

### 第四步：人工检查

```bash
git diff
pytest -q
```

必须确认：

- 只改了本模块的文件
- 没有改共享接口
- 没有提交 Key、论文或个人数据
- 测试通过
- 自己能解释 AI 生成的代码

### 第五步：提交和 PR

```bash
git add <files>
git commit -m "feat(pdf): add page-level extraction"
git push
```

然后在 GitHub 开 PR，填写 AI 使用声明，并让 Review 配对成员检查。

## 6. 本仓库的 Codex 安全设置

`.codex/config.toml` 当前设置：

- `sandbox_mode = "workspace-write"`：只能修改当前仓库
- `approval_policy = "on-request"`：需要联网或越界时询问
- `network_access = false`：默认禁止联网
- `shell_environment_policy`：自动排除名称含 `KEY`、`SECRET`、`TOKEN` 的环境变量

因此：

- 普通代码修改和本地测试可以直接运行
- 需要联网、安装依赖或访问外部 API 时，Codex 会请求批准
- 不要把真实 API Key 放进仓库内的 `.env`；Codex 可以读取工作区文件
- 不要把未公开论文、用户数据或完整 Prompt 粘贴进 Codex 对话

## 7. 模块边界

| 成员 | 主要目录 | 不要直接修改 |
|---|---|---|
| A | `paperlens/pdf/` | `paperlens/ai/`、`paperlens/terms/`、`paperlens/web/` |
| B | `paperlens/ai/` | `paperlens/pdf/`、`paperlens/terms/`、`paperlens/web/` |
| C | `paperlens/terms/` | `paperlens/pdf/`、`paperlens/ai/`、`paperlens/web/` |
| D | `paperlens/web/`、`app.py`、`config.py` | 其他成员的模块实现 |

共享文件：

- `paperlens/common/models.py`
- `docs/data-model.md`
- `docs/api.md`

修改前必须在小组内沟通，并由接口负责人 Review。

## 8. Codex Cloud（可选）

如果不想本地安装：

1. 打开 ChatGPT 的 **Codex → Cloud**
2. 连接 GitHub 仓库
3. 创建或选择环境
4. 启动任务
5. 在网页中检查 diff，再开 PR

Codex Cloud 同样会读取仓库中的 `AGENTS.md`。课程项目更推荐本地 CLI，因为测试、查看 diff 和修复环境问题更方便。

## 9. 常见问题

**`.codex/config.toml` 没有生效？**  
确认第一次运行时信任了该仓库；项目级配置只对受信任项目加载。

**Codex 改了不该改的文件？**  
立即停止，运行 `git diff` 检查；不要直接 commit。让它只修改指定模块，或恢复到任务前的提交。

**Codex 要联网安装依赖？**  
先由负责人在本地确认依赖，再批准单次网络访问；不要全局打开网络。

**规则看起来是旧的？**  
重启 Codex 会话，它会重新读取 `AGENTS.md`。

**忘记记录 AI 使用？**  
在 `docs/ai-usage.md` 补一行，并在 PR 中勾选 AI-assisted。

## 10. 官方文档

- Codex CLI：https://learn.chatgpt.com/docs/codex/cli
- AGENTS.md：https://learn.chatgpt.com/docs/agent-configuration/agents-md
- 项目级配置：https://learn.chatgpt.com/docs/config-file/config-advanced
- 审批与沙箱：https://learn.chatgpt.com/docs/agent-approvals-security
- Codex Cloud：https://learn.chatgpt.com/docs/cloud
