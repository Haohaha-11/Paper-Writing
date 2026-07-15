# Paper-Writing 项目蒸馏清单

> Status note, 2026-07-15: this is the original design sketch. The current v0.1 direction is a GitHub-native paper-writing knowledge base with `skills/`, `venues/`, `workflows/`, `templates/`, and `examples/`, not a CLI-first Python package. Keep this file as historical planning context.

> 目标：构建一个面向 arXiv、ICLR、NeurIPS、CVPR、ICML、ECCV、AAAI、IEEE TMI 等会议与期刊的论文写作工程，暂时聚焦文章写作、模板管理和 LaTeX 工具链，不处理论文绘图和 idea 调研。

---

## 1. 项目范围

### 1.1 当前阶段需要完成

- [ ] 建立可复用的学术写作 Skill 系统
- [ ] 支持按论文 section 加载不同写作 Skill
- [ ] 支持按 venue 加载会议或期刊风格
- [ ] 收集并管理各 venue 最新官方模板
- [ ] 建立统一的 LaTeX 编译环境
- [ ] 支持论文检查、审稿、修改和 diff
- [ ] 支持 arXiv 清理与打包
- [ ] 支持 GitHub Actions 自动编译
- [ ] 为 Skill、模板和工作流建立测试

### 1.2 当前阶段暂不处理

- [ ] 自动生成科研 idea
- [ ] 自动运行和修改实验代码
- [ ] 自动绘制论文框架图
- [ ] 自动绘制实验图表
- [ ] 自动完成完整文献调研
- [ ] 无监督自动生成整篇论文

---

## 2. 第一优先级蒸馏项目

## 2.1 K-Dense-AI Scientific Agent Skills

- 仓库：<https://github.com/K-Dense-AI/claude-scientific-skills>
- 定位：科研 Skill 基础设施和组织规范
- 优先级：S+

### 重点研究

- [ ] `SKILL.md` 的标准结构
- [ ] Skill 的元数据设计
- [ ] Skill 的触发条件
- [ ] Skill 的输入和输出约束
- [ ] Skill 的执行步骤描述方式
- [ ] Skill 的示例组织方式
- [ ] Skill 的参考资料组织方式
- [ ] Skill 的自动发现机制
- [ ] Skill 的跨 Agent 兼容方式
- [ ] Skill 的测试方式
- [ ] Skill 的安全扫描方式

### 计划蒸馏

- [ ] 定义本项目统一的 `SKILL.md` 规范
- [ ] 建立 Skill schema
- [ ] 建立 Skill validator
- [ ] 建立 Skill registry
- [ ] 建立 Skill dependency 机制
- [ ] 支持组合加载多个 Skill
- [ ] 支持 Claude Code、Codex、Cursor 等不同 Agent

### 不直接照搬

- [ ] 不保留过于宽泛的通用科研 Skill 分类
- [ ] 不把所有科研任务都放入第一版
- [ ] 不直接复制缺少论文写作针对性的 Prompt

---

## 2.2 PaperDebugger

- 仓库：<https://github.com/PaperDebugger/PaperDebugger>
- 定位：在真实 LaTeX 工程中完成论文审查、修改和修订
- 优先级：S+

### 重点研究

- [ ] 如何解析完整 LaTeX 项目
- [ ] 如何识别主文件和子文件
- [ ] 如何理解 section 之间的上下文
- [ ] 如何处理 `\input` 和 `\include`
- [ ] 如何处理 label、ref 和 citation
- [ ] 如何定位需要修改的段落
- [ ] 如何生成修改建议
- [ ] 如何生成可审阅 diff
- [ ] 如何避免直接覆盖用户原稿
- [ ] 如何让用户选择接受或拒绝修改
- [ ] 如何组织 researcher、reviewer、reviser 等角色
- [ ] 如何验证新增引用是否真实存在
- [ ] 如何保证术语和符号的一致性

### 计划蒸馏

- [ ] 实现 project-level paper context
- [ ] 实现 section-level context retrieval
- [ ] 实现 patch-based revision
- [ ] 实现 dry-run 模式
- [ ] 实现 review report
- [ ] 实现用户确认后的文件写回
- [ ] 实现修改历史和回滚

---

## 2.3 PaperMentor / Venue-Aware Writing Skills

- 候选仓库：<https://github.com/jiarui-liu/overleaf>
- 定位：按 venue、section、任务和写作类型组合不同专家 Skill
- 优先级：S
- 注意：蒸馏前需要进一步核对论文、代码和 Skill 文件的完整对应关系

### 重点研究

- [ ] venue 维度的 Skill 分类
- [ ] paper type 维度的 Skill 分类
- [ ] section 维度的 Skill 分类
- [ ] figure/table 描述 Skill
- [ ] academic style Skill
- [ ] terminology Skill
- [ ] formatting Skill
- [ ] 多个 Skill 的组合加载方法
- [ ] 专家角色之间的协作方式
- [ ] 会议风格知识如何抽取和维护

### 计划蒸馏

将写作知识拆成以下正交维度：

```text
通用学术规范
×
论文领域
×
目标 venue
×
论文类型
×
当前 section
×
当前写作任务
×
目标长度和语气
```

示例组合：

```text
academic-writing
+ machine-learning-paper
+ introduction-writing
+ contribution-positioning
+ iclr-style
+ concise-revision
```

### 核心原则

- [ ] 不为每个会议写一个巨大的单体 Prompt
- [ ] 通用写作规则与 venue 特定规则分离
- [ ] section Skill 与 venue Skill 分离
- [ ] 写作风格与年度投稿规则分离
- [ ] 多年稳定规则与逐年更新规则分离

---

## 2.4 SakanaAI AI Scientist v1

- 仓库：<https://github.com/SakanaAI/AI-Scientist>
- 定位：从实验材料到论文大纲、草稿和自动审稿的完整流水线
- 优先级：S

### 重点研究

- [ ] 论文模板的组织方式
- [ ] 实验结果如何转化为写作上下文
- [ ] 如何从实验材料生成论文大纲
- [ ] 如何逐 section 写作
- [ ] 如何维护长上下文
- [ ] 如何生成内部 reviewer 意见
- [ ] 如何根据 reviewer 意见修改
- [ ] 如何管理写作过程中的状态
- [ ] 如何组织论文生成 pipeline
- [ ] 如何检查生成的 LaTeX

### 计划蒸馏

- [ ] Outline generation
- [ ] Section-by-section drafting
- [ ] Result-to-text conversion
- [ ] Internal review
- [ ] Revision loop
- [ ] Paper state tracking
- [ ] LaTeX validation

### 暂不蒸馏

- [ ] 自动提出科研 idea
- [ ] 自动修改实验代码
- [ ] 自动运行模型生成的未知代码
- [ ] 无监督完成全部研究流程
- [ ] 直接复制其完整代码或受限制模块

### 许可证检查

- [ ] 阅读仓库 LICENSE
- [ ] 检查模型生成内容相关条款
- [ ] 检查代码复用和分发限制
- [ ] 仅蒸馏思想时记录来源
- [ ] 避免直接复制受限实现

---

## 2.5 Google Research arXiv LaTeX Cleaner

- 仓库：<https://github.com/google-research/arxiv-latex-cleaner>
- 定位：清理 LaTeX 工程并生成适合 arXiv 上传的版本
- 优先级：S

### 重点研究

- [ ] 删除未使用图片
- [ ] 删除编译缓存
- [ ] 清理注释
- [ ] 检查文件大小
- [ ] 处理图片压缩
- [ ] 处理不必要资源
- [ ] 生成干净上传目录
- [ ] 保持原工程不被修改
- [ ] 输出清理报告

### 计划集成命令

```bash
paper-writing export arxiv
```

### 预期流程

- [ ] 复制原始项目到临时目录
- [ ] 检查主 TeX 文件
- [ ] 清理中间文件
- [ ] 删除未引用资源
- [ ] 清理注释
- [ ] 检查图片和单文件大小
- [ ] 检查 BibTeX 和引用
- [ ] 重新编译
- [ ] 检查 PDF 是否正常
- [ ] 输出 `.zip` 或 `.tar.gz`
- [ ] 生成 arXiv 上传检查报告

---

## 2.6 xu-cheng/latex-action

- 仓库：<https://github.com/xu-cheng/latex-action>
- 定位：GitHub Actions 中自动编译 LaTeX
- 优先级：S

### 重点研究

- [ ] GitHub Actions 编译 LaTeX 的标准方式
- [ ] 如何缓存 TeX Live 依赖
- [ ] 如何选择编译引擎
- [ ] 如何调用 `latexmk`
- [ ] 如何上传 PDF artifact
- [ ] 如何解析编译错误
- [ ] 如何在 pull request 中显示检查结果

### 计划工作流

```text
.github/workflows/
├── compile.yml
├── lint.yml
├── arxiv-check.yml
└── release-pdf.yml
```

### 编译检查项

- [ ] LaTeX 编译成功
- [ ] 无 undefined citation
- [ ] 无 undefined reference
- [ ] 无 multiply-defined label
- [ ] 无严重 overfull box
- [ ] 无缺失图片
- [ ] 无缺失字体
- [ ] 无 BibTeX/Biber 错误
- [ ] PDF 页数符合限制
- [ ] PDF 文件大小符合限制

---

## 2.7 官方会议和期刊模板

- ICLR：<https://github.com/ICLR/Master-Template>
- CVPR：<https://github.com/cvpr-org/author-kit>
- 其他 venue：优先从官方会议网站、官方 GitHub、出版社页面获取
- 定位：模板和年度规则的唯一可信上游
- 优先级：S

### 首批支持 venue

- [ ] arXiv
- [ ] ICLR
- [ ] NeurIPS
- [ ] ICML
- [ ] CVPR
- [ ] ECCV
- [ ] AAAI
- [ ] IEEE TMI

### 每个 venue 需要收集

- [ ] 官方模板
- [ ] 官方 Author Guide
- [ ] Call for Papers
- [ ] 投稿页数限制
- [ ] camera-ready 页数限制
- [ ] appendix 规则
- [ ] supplementary material 规则
- [ ] 匿名要求
- [ ] arXiv 和公开预印本政策
- [ ] 代码匿名规则
- [ ] Ethics Statement 要求
- [ ] Reproducibility Statement 要求
- [ ] LLM 使用披露要求
- [ ] 引用格式
- [ ] 字体和页面尺寸
- [ ] 投稿系统
- [ ] 重要日期
- [ ] 官方来源链接
- [ ] 获取日期
- [ ] 版本号或 commit
- [ ] 文件 checksum
- [ ] 模板许可证

### 模板注册表建议

```yaml
venue: iclr
year: 2026
type: conference

source:
  type: github
  repository: ICLR/Master-Template
  commit: "<commit-sha>"
  retrieved_at: "YYYY-MM-DD"

template:
  main_style: iclr2026_conference.sty
  bibliography_style: iclr2026_conference.bst
  checksum: "<sha256>"

page_limit:
  submission: 9
  rebuttal: 10
  camera_ready: 10

policies:
  anonymous_review: true
  appendix_allowed: true
  llm_disclosure: true
```

---

## 3. 第二优先级参考项目

## 3.1 Stanford STORM

- 仓库：<https://github.com/stanford-oval/storm>
- 定位：长文研究、观点组织、提纲生成和引用支撑
- 优先级：A

### 适合蒸馏

- [ ] 多视角问题生成
- [ ] 从材料生成层级提纲
- [ ] claim 与来源绑定
- [ ] 长文上下文管理
- [ ] outline-first 写作
- [ ] 来源和论点之间的映射

### 暂不作为核心

- [ ] 它主要面向调研报告和百科长文
- [ ] 不直接覆盖机器学习顶会论文风格
- [ ] 当前项目暂不做完整文献调研

---

## 3.2 GPT Researcher

- 仓库：<https://github.com/assafelovic/gpt-researcher>
- 定位：自动检索、信息整合和研究报告生成
- 优先级：A-

### 后续可蒸馏

- [ ] 多查询搜索
- [ ] 来源质量筛选
- [ ] 文献调研任务分解
- [ ] 研究上下文压缩
- [ ] 引用链接管理
- [ ] 深度研究 workflow

### 当前处理

- [ ] 加入候选列表
- [ ] 暂不纳入 v0.1
- [ ] 等调研模块启动后再深入分析

---

## 3.3 LaTeX Workshop

- 仓库：<https://github.com/James-Yu/LaTeX-Workshop>
- 定位：VS Code LaTeX 开发体验
- 优先级：A-

### 适合参考

- [ ] 自动编译配置
- [ ] PDF 预览
- [ ] SyncTeX
- [ ] LaTeX 补全
- [ ] 错误解析
- [ ] lint 集成
- [ ] recipes 配置
- [ ] magic comments

### 项目可提供

```text
.vscode/
├── settings.json
├── extensions.json
└── tasks.json
```

---

## 3.4 Overleaf Toolkit

- 仓库：<https://github.com/overleaf/toolkit>
- 定位：自托管 Overleaf
- 优先级：B

### 未来用途

- [ ] 浏览器内协同编辑
- [ ] 自托管论文写作平台
- [ ] Agent 与 Overleaf 深度集成
- [ ] 团队论文项目管理

### 当前不做

- [ ] 不在 v0.1 部署完整 Overleaf
- [ ] 不引入过重基础设施
- [ ] 不在未明确许可证影响前整合其代码

---

## 4. 推荐蒸馏顺序

### 第 1 阶段：Skill 基础设施

1. [ ] K-Dense Scientific Agent Skills
2. [ ] PaperMentor 的 Skill 分类方法
3. [ ] 定义本项目的 Skill schema
4. [ ] 实现 Skill registry
5. [ ] 实现 Skill loader
6. [ ] 实现 Skill composition
7. [ ] 实现 Skill validator

### 第 2 阶段：真实论文编辑

1. [ ] PaperDebugger
2. [ ] LaTeX project parser
3. [ ] paper context builder
4. [ ] section locator
5. [ ] patch/diff generator
6. [ ] revision history
7. [ ] user approval workflow

### 第 3 阶段：写作流水线

1. [ ] AI Scientist v1
2. [ ] outline generation
3. [ ] section drafting
4. [ ] internal review
5. [ ] revision loop
6. [ ] result-to-text
7. [ ] consistency checking

### 第 4 阶段：模板和工具链

1. [ ] 官方 Author Kits
2. [ ] 模板 registry
3. [ ] Docker/Dev Container
4. [ ] latexmk
5. [ ] chktex
6. [ ] latexindent
7. [ ] GitHub Actions
8. [ ] arXiv cleaner
9. [ ] PDF/page-limit checks

---

## 5. 项目目录结构建议

```text
paper-writing/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── pyproject.toml
├── uv.lock
│
├── skills/
│   ├── core/
│   │   ├── academic-writing/
│   │   ├── claim-evidence-check/
│   │   ├── terminology-consistency/
│   │   ├── notation-consistency/
│   │   ├── citation-placement/
│   │   └── latex-writing/
│   │
│   ├── sections/
│   │   ├── title/
│   │   ├── abstract/
│   │   ├── introduction/
│   │   ├── related-work/
│   │   ├── method/
│   │   ├── experiments/
│   │   ├── ablation/
│   │   ├── limitations/
│   │   └── conclusion/
│   │
│   ├── review/
│   │   ├── novelty-review/
│   │   ├── clarity-review/
│   │   ├── experiment-review/
│   │   ├── citation-review/
│   │   └── venue-review/
│   │
│   ├── revision/
│   │   ├── rewrite/
│   │   ├── shorten/
│   │   ├── expand/
│   │   ├── polish/
│   │   └── rebuttal-response/
│   │
│   └── publication/
│       ├── anonymous-check/
│       ├── camera-ready/
│       └── arxiv-export/
│
├── venues/
│   ├── arxiv/
│   ├── iclr/
│   │   ├── 2026/
│   │   │   ├── rules.yaml
│   │   │   ├── style.md
│   │   │   ├── checklist.md
│   │   │   └── template.lock
│   │   └── latest
│   ├── neurips/
│   ├── icml/
│   ├── cvpr/
│   ├── eccv/
│   ├── aaai/
│   └── tmi/
│
├── workflows/
│   ├── initialize-paper/
│   ├── outline-to-draft/
│   ├── write-section/
│   ├── rewrite-section/
│   ├── shorten-to-page-limit/
│   ├── internal-review/
│   ├── rebuttal/
│   ├── camera-ready/
│   └── arxiv-release/
│
├── templates/
│   ├── registry.yaml
│   ├── upstream/
│   ├── patched/
│   └── licenses/
│
├── toolchain/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── devcontainer/
│   ├── latexmkrc
│   ├── chktexrc
│   ├── latexindent.yaml
│   └── scripts/
│
├── src/
│   └── paper_writing/
│       ├── cli/
│       ├── skills/
│       ├── venues/
│       ├── latex/
│       ├── review/
│       ├── revision/
│       └── export/
│
├── evals/
│   ├── skill-evals/
│   ├── style-evals/
│   ├── latex-evals/
│   ├── venue-evals/
│   └── regression/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│
├── examples/
│   ├── iclr-paper/
│   ├── cvpr-paper/
│   └── tmi-paper/
│
└── .github/
    ├── workflows/
    │   ├── compile.yml
    │   ├── lint.yml
    │   ├── arxiv-check.yml
    │   └── release-pdf.yml
    └── ISSUE_TEMPLATE/
```

---

## 6. Skill 分类建议

## 6.1 通用核心 Skill

- [ ] Academic Writing
- [ ] Claim–Evidence Alignment
- [ ] Citation Placement
- [ ] Citation Verification
- [ ] Terminology Consistency
- [ ] Notation Consistency
- [ ] Paragraph Coherence
- [ ] Logical Flow
- [ ] Conciseness
- [ ] Academic Tone
- [ ] Avoid Overclaiming
- [ ] Avoid Ambiguous Pronouns
- [ ] LaTeX Safety
- [ ] Cross-Reference Safety
- [ ] Anonymity Check

## 6.2 Section Skill

- [ ] Title
- [ ] Abstract
- [ ] Introduction
- [ ] Related Work
- [ ] Problem Formulation
- [ ] Method
- [ ] Theory
- [ ] Experimental Setup
- [ ] Main Results
- [ ] Ablation Study
- [ ] Qualitative Analysis
- [ ] Limitations
- [ ] Ethics Statement
- [ ] Reproducibility Statement
- [ ] Conclusion
- [ ] Appendix
- [ ] Rebuttal

## 6.3 修改任务 Skill

- [ ] Rewrite
- [ ] Polish
- [ ] Shorten
- [ ] Expand
- [ ] Merge Paragraphs
- [ ] Split Paragraph
- [ ] Improve Logic
- [ ] Improve Novelty Positioning
- [ ] Strengthen Motivation
- [ ] Reduce Repetition
- [ ] Convert Notes to Prose
- [ ] Convert Results to Analysis
- [ ] Respond to Reviewer
- [ ] Camera-Ready Revision

## 6.4 Venue Skill

- [ ] arXiv style
- [ ] ICLR style
- [ ] NeurIPS style
- [ ] ICML style
- [ ] CVPR style
- [ ] ECCV style
- [ ] AAAI style
- [ ] IEEE TMI style

---

## 7. Venue 风格与年度规则分离

### 7.1 Venue Style

长期相对稳定，描述：

- [ ] 论文通常如何组织
- [ ] 如何表述贡献
- [ ] 如何写 motivation
- [ ] 如何评价 novelty
- [ ] 实验通常需要覆盖什么
- [ ] 常见 reviewer 关注点
- [ ] 推荐的 claim 强度
- [ ] 推荐的篇幅分配
- [ ] 常见写作问题

### 7.2 Venue Rules

每年更新，描述：

- [ ] 投稿日期
- [ ] 页数限制
- [ ] 模板版本
- [ ] 匿名要求
- [ ] supplementary 规则
- [ ] appendix 规则
- [ ] ethics 要求
- [ ] reproducibility 要求
- [ ] LLM disclosure
- [ ] arXiv policy
- [ ] dual submission policy
- [ ] reviewer registration
- [ ] camera-ready 规则

### 7.3 必须避免

- [ ] 不把会变化的年度规则写死在通用 Skill 中
- [ ] 不把写作风格和格式要求混在一起
- [ ] 不依赖第三方截止日期作为唯一来源
- [ ] 不自动覆盖旧版本模板
- [ ] 不使用未记录来源的模板

---

## 8. LaTeX 工具链清单

### 8.1 基础环境

- [ ] TeX Live
- [ ] `latexmk`
- [ ] `pdflatex`
- [ ] `xelatex`
- [ ] `lualatex`
- [ ] BibTeX
- [ ] Biber
- [ ] Python
- [ ] Perl
- [ ] ImageMagick 或等价图片工具

### 8.2 检查工具

- [ ] `chktex`
- [ ] `lacheck`
- [ ] `latexindent`
- [ ] `aspell` 或 LanguageTool
- [ ] PDF page counter
- [ ] PDF metadata checker
- [ ] file-size checker
- [ ] unused-image checker
- [ ] missing-reference checker
- [ ] missing-citation checker

### 8.3 环境封装

- [ ] Dockerfile
- [ ] Dev Container
- [ ] 固定 TeX Live 版本
- [ ] 固定 Python 依赖
- [ ] 固定系统字体和依赖
- [ ] 支持本地和 CI 使用同一环境
- [ ] 输出可复现环境信息

---

## 9. CLI 初步设计

```bash
paper-writing init --venue iclr --year 2027
paper-writing compile
paper-writing check
paper-writing lint
paper-writing review
paper-writing revise
paper-writing shorten --target-pages 9
paper-writing venue-check
paper-writing anonymous-check
paper-writing export arxiv
paper-writing export camera-ready
paper-writing template update
paper-writing template list
paper-writing skill list
paper-writing skill validate
```

### 第一版必须支持

- [ ] `init`
- [ ] `compile`
- [ ] `check`
- [ ] `venue-check`
- [ ] `anonymous-check`
- [ ] `export arxiv`
- [ ] `skill list`
- [ ] `skill validate`

---

## 10. 蒸馏记录模板

每分析一个仓库，建立一份记录：

```markdown
# Repository Distillation Record

## Basic Information

- Repository:
- URL:
- License:
- Main language:
- Last checked:
- Relevant version or commit:

## Why It Is Relevant

## Architecture

## Valuable Components

## Components Not Needed

## Reusable Ideas

## Code That May Be Reused

## License Risks

## Security Risks

## Proposed Integration

## Minimal Prototype

## Open Questions

## Final Decision

- [ ] Direct dependency
- [ ] Optional dependency
- [ ] Reimplement
- [ ] Conceptual reference only
- [ ] Do not use
```

---

## 11. 仓库评估维度

每个候选项目按以下维度打分，满分 5 分：

| 维度 | 说明 |
|---|---|
| Relevance | 与论文写作项目的相关程度 |
| Architecture | 架构是否值得复用 |
| Code Quality | 代码质量和可维护性 |
| Documentation | 文档是否清晰 |
| Activity | 是否仍在维护 |
| License | 是否适合复用 |
| Extensibility | 是否容易扩展到多个 venue |
| Agent Compatibility | 是否兼容不同 Agent |
| LaTeX Integration | 是否能操作真实 LaTeX 项目 |
| Evaluation | 是否有测试或 benchmark |

### 评估结果

- [ ] 建立 `docs/repository-evaluation.md`
- [ ] 为每个项目给出总分
- [ ] 给出“直接依赖 / 重写 / 仅参考”的决策
- [ ] 记录所有许可证和安全风险
- [ ] 记录采用的具体模块和来源

---

## 12. v0.1 最小可用版本

### 功能目标

- [ ] 支持初始化 ICLR、CVPR 和 TMI 工程
- [ ] 支持自动编译
- [ ] 支持模板版本记录
- [ ] 支持 venue rule 检查
- [ ] 支持匿名检查
- [ ] 支持 5 个核心写作 Skill
- [ ] 支持 Introduction 和 Abstract 修改
- [ ] 支持 diff 输出
- [ ] 支持 arXiv 导出
- [ ] 支持 GitHub Actions

### 首批核心 Skill

- [ ] Abstract Writer
- [ ] Introduction Writer
- [ ] Contribution Refiner
- [ ] Academic Rewriter
- [ ] Claim–Evidence Checker

### 首批 venue

- [ ] ICLR
- [ ] CVPR
- [ ] IEEE TMI

### v0.1 不做

- [ ] 全自动整篇生成
- [ ] 自动文献调研
- [ ] 自动 idea 生成
- [ ] 自动实验
- [ ] 绘图
- [ ] Overleaf 自托管

---

## 13. 第一轮执行任务

### 仓库准备

- [ ] 创建 `paper-writing` GitHub 仓库
- [ ] 确定开源许可证
- [ ] 创建 README
- [ ] 创建 CONTRIBUTING
- [ ] 创建 Roadmap
- [ ] 创建 issue templates
- [ ] 配置 branch protection
- [ ] 配置 pre-commit

### 蒸馏工作

- [ ] Clone K-Dense Scientific Skills
- [ ] Clone PaperDebugger
- [ ] 阅读 PaperMentor 论文和代码
- [ ] Clone AI Scientist v1
- [ ] Clone arXiv LaTeX Cleaner
- [ ] 阅读 latex-action
- [ ] 收集 ICLR 官方模板
- [ ] 收集 CVPR 官方模板
- [ ] 收集 TMI 官方模板和 IEEEtran

### 产出文档

- [ ] `docs/architecture.md`
- [ ] `docs/skill-spec.md`
- [ ] `docs/template-registry.md`
- [ ] `docs/venue-rules.md`
- [ ] `docs/repository-evaluation.md`
- [ ] `docs/security.md`
- [ ] `docs/licenses.md`
- [ ] `ROADMAP.md`

### 第一版代码

- [ ] Skill schema
- [ ] Skill validator
- [ ] Skill registry
- [ ] Venue registry
- [ ] Template registry
- [ ] LaTeX compile command
- [ ] Basic checks
- [ ] GitHub Actions
- [ ] arXiv exporter

---

## 14. 建议的首轮决策

| 项目 | 决策 |
|---|---|
| K-Dense Scientific Agent Skills | 深度蒸馏 Skill 规范，优先考虑重写基础设施 |
| PaperDebugger | 深度蒸馏 LaTeX 工程编辑与 diff 工作流 |
| PaperMentor | 蒸馏 venue × section × task 的知识分类 |
| AI Scientist v1 | 蒸馏写作流水线，不复制完整科研自动化 |
| arXiv LaTeX Cleaner | 可作为依赖或封装 |
| latex-action | 直接用于 GitHub CI 或参考其配置 |
| 官方 Author Kits | 作为模板和规则的唯一可信上游 |
| STORM | 后续调研模块参考 |
| GPT Researcher | 后续文献调研模块参考 |
| LaTeX Workshop | 提供推荐配置，不作为核心依赖 |
| Overleaf Toolkit | 暂不纳入 v0.1 |

---

## 15. 最终架构原则

- [ ] Skill-first，而不是 Prompt collection
- [ ] Venue-aware，而不是统一生成风格
- [ ] Project-level context，而不是只处理单段文字
- [ ] Patch-based revision，而不是无条件覆盖
- [ ] Official-source-first，而不是依赖第三方规则
- [ ] Reproducible toolchain，而不是依赖本地环境
- [ ] Human-in-the-loop，而不是完全自动写论文
- [ ] Testable skills，而不是无法评估的长 Prompt
- [ ] Stable style + yearly rules 分离
- [ ] 写作、模板、调研三个子系统解耦

---

## 16. 推荐总路线

```text
K-Dense Scientific Skills
        ↓
定义 Skill 的形式和基础设施

PaperMentor
        ↓
定义写作知识的分类和组合方式

PaperDebugger
        ↓
定义如何在真实 LaTeX 工程中审查和修改

AI Scientist v1
        ↓
定义从大纲到 section 草稿再到内部审稿的流水线

Official Author Kits
        ↓
提供最新模板与年度投稿规则

latex-action
        ↓
负责持续编译和自动检查

arxiv-latex-cleaner
        ↓
负责 arXiv 发布清理和打包
```

项目最终应定位为：

> 一个面向主流 AI 会议和期刊、支持多 Agent、具备真实 LaTeX 工程理解能力的 venue-aware paper engineering framework。
