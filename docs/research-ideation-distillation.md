# Research Ideation Project Distillation

Last updated: 2026-07-16

This document distills open-source research-agent and ideation systems into project-owned patterns for the idea-to-paper stage. It should guide `research-scout`, `research-problem-framer`, `pre-experiment-planner`, and `workflows/idea-to-paper.md`.

The goal is not to copy external prompts. The goal is to preserve useful workflow structure while keeping Paper-Writing-Hao evidence-first, local-first, and venue-aware.

## Projects Reviewed

| Project | Useful pattern | Project decision |
|---|---|---|
| Sakana AI `AI-Scientist` | End-to-end loop from idea generation to experiment execution, paper writeup, and automated review | Adopt the stage separation and review gate, not autonomous claim generation |
| `MAGenIdeas` | Multi-agent idea generation and candidate discussion | Adopt candidate pools, role-based critique, and decision records |
| Microsoft `ResearchAgent` | Iterative research idea generation grounded in related work | Adopt iterative expansion/revision loops and novelty checks |
| Stanford OVAL `STORM` / `Co-STORM` | Question-driven knowledge curation from multiple perspectives | Adopt question trees and perspective coverage for literature scouting |
| FutureHouse `paper-qa` | Citation-backed answers over scientific papers | Adopt provenance requirements and "answer only from retrieved evidence" behavior |
| `OpenScholar` | Retrieval-augmented scientific literature synthesis | Adopt claim/source separation and missing-evidence reporting |
| `AwesomeLit` | Literature exploration and hypothesis-oriented workflows | Adopt literature graph/query-tree thinking |
| `Deep-Researcher-Agent` | Think-execute-reflect loop for research tasks | Adopt experiment ledger, reflection, and stop/revise gates |
| `PaperPilot` | Structured multi-agent academic workflow | Adopt explicit checkpoints and artifact handoffs |

## Distilled Design Patterns

### 1. Question Tree Before Idea List

Start from questions, not methods.

Required artifacts:

- root research question;
- perspective questions;
- query tree;
- source coverage map;
- unanswered or contradictory findings.

This prevents "new architecture first" ideation and aligns with the current `research-scout` skill.

### 2. Candidate Pool With Decision Records

Generate multiple candidates, then preserve why each was locked, revised, or killed.

Required fields:

- contradiction;
- closest work;
- decisive test;
- main risk;
- resource fit;
- decision.

This is more useful than a ranked novelty list because it keeps dead ends and risk reasoning visible.

### 3. Provenance-Gated Claims

Every observation used to form a candidate must be tagged as one of:

- source-backed;
- preliminary-result-backed;
- domain-expert-backed;
- hypothesis only;
- unchecked.

Unchecked observations cannot become abstract, introduction, or contribution claims.

### 4. Multi-Perspective Critique

Before locking a research problem, review it from at least these roles:

- closest-work critic;
- experiment feasibility critic;
- mechanism critic;
- reviewer-attack critic;
- venue-fit critic;
- ethics/privacy/domain critic when relevant.

This should improve `research-problem-framer` without creating a separate autonomous agent framework.

### 5. Falsification Before Method Design

Do not design the full method until a small sprint checks whether the problem exists and whether simple alternatives remove it.

Required outputs:

- kill condition;
- strongest simple baseline;
- variable isolated;
- result that supports the problem;
- result that kills the problem;
- next decision.

### 6. Experiment Ledger And Reflection

Pre-experiments should leave a lightweight record:

- date;
- hypothesis;
- configuration;
- result;
- interpretation;
- decision;
- artifact path;
- remaining risk.

This avoids the common failure where a negative pre-experiment disappears from the paper story and the project drifts into post-hoc method design.

### 7. Idea-To-Paper Handoff

A problem is ready for `draft-to-submission` only when these artifacts exist:

- frontier problem map;
- locked problem statement;
- novelty boundary;
- non-claim;
- falsification sprint result;
- method-design rationale;
- main/supplementary experiment plan.

## Anti-Patterns To Avoid

- Treating "latest paper" as "best paper".
- Producing a ranked list of ideas without closest-work boundaries.
- Starting from method modules instead of a measured contradiction.
- Letting an agent invent missing citations, results, or reviewer opinions.
- Treating automated review as acceptance prediction.
- Hiding killed candidates and negative pre-experiments.
- Claiming a problem is broad when it only appears on one benchmark.

## Source Notes

- Sakana AI AI-Scientist: https://github.com/SakanaAI/AI-Scientist
- MAGenIdeas: https://github.com/ChenShuai00/MAGenIdeas
- ResearchAgent: https://github.com/microsoft/ResearchAgent
- STORM: https://github.com/stanford-oval/storm
- PaperQA: https://github.com/Future-House/paper-qa
- OpenScholar: https://github.com/ZhuKerui/OpenScholar
- AwesomeLit: https://github.com/GAIR-NLP/AwesomeLit
- Deep Researcher Agent: https://github.com/GAIR-NLP/Deep-Researcher-Agent
- PaperPilot: https://github.com/Roihn/paper-pilot
