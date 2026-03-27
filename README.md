# learning

This repo is for building two parallel foundations:

1. Enterprise AI application design and operation
2. Core CS, software engineering, and systems fundamentals

The structure is intentionally split between applied enterprise AI work and deeper technical foundations. The goal is not only to learn how to use LLMs and agents, but also to understand the systems, controls, and engineering discipline required to ship reliable products.

The main study roadmap for this repo is in [LEARNING_PLAN.md](/Users/weifengcao/Documents/learning/LEARNING_PLAN.md).

## Folder map

- `enterprise_ai_app/`: how to build enterprise AI applications that are controllable, observable, secure, and cost-bounded
- `coding/`: programming practice, language fluency, software design, testing, debugging, and implementation discipline
- `db/`: relational databases, transactions, indexing, query planning, data modeling, and storage fundamentals
- `os/`: processes, threads, memory, filesystems, scheduling, and systems-level behavior
- `cloud/`: deployment, containers, orchestration, networking, and distributed systems basics
- `security/`: identity, authorization, secrets, application security, cloud security, and threat modeling
- `saas/`: traditional SaaS architecture, multitenancy, billing, auditability, and product/platform patterns
- `llm/`: model-side foundations such as transformers, inference, embeddings, fine-tuning, and evaluation
- `agent/`: agent patterns, tool use, planning loops, memory strategies, and multi-agent system design

## How the folders relate

- `enterprise_ai_app/` is application-facing. It focuses on what enterprises need to trust and operate AI systems in production.
- `llm/` is model-facing. It covers how the underlying model technology works.
- `agent/` is technique-facing. It explores agent architectures beyond narrow enterprise deployment concerns.
- `saas/`, `security/`, `cloud/`, `db/`, and `os/` provide the engineering backbone that enterprise AI applications still depend on.

## CS fundamentals coverage

The most important non-AI foundations to cover in this repo are:

- Programming and software engineering discipline in `coding/`
- Data and persistence fundamentals in `db/`
- Systems behavior in `os/`
- Networking, deployment, and distributed systems in `cloud/`
- Security and trust boundaries in `security/`
- Product architecture and multitenancy in `saas/`

For now, networking and distributed systems should live under `cloud/`, with some lower-level process and concurrency concepts under `os/`. If those topics become large enough, they can be promoted to their own top-level folders later.

## Suggested contents per folder

Each topic folder should eventually contain:

- `README.md` for scope and study plan
- `notes/` for theory and distilled concepts
- `patterns/` for reusable design ideas
- `labs/` for hands-on experiments
- `projects/` for end-to-end builds
- `checklists/` for review and deployment criteria
