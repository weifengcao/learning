# Learning Plan

This learning plan is designed for both junior and senior engineers using the same repository.

The principle is simple:

- juniors need stronger implementation depth, debugging discipline, and repetition
- seniors need stronger architecture judgment, systems tradeoff analysis, and production controls
- both should share the same core topics, but with different expected outcomes

## Goals

By the end of this plan, learners should be able to:

- explain the CS and software foundations behind modern backend and AI systems
- build reliable software services with proper testing, data modeling, and operational awareness
- understand LLM and agent foundations well enough to avoid shallow design decisions
- design enterprise AI applications that are secure, observable, auditable, and cost-bounded

## Program Shape

Suggested duration: 24 weeks

- Phase 1, weeks 1-8: CS and software engineering foundations
- Phase 2, weeks 9-14: LLM and agent foundations
- Phase 3, weeks 15-22: enterprise AI application design and operations
- Phase 4, weeks 23-24: capstone project and architecture review

Suggested weekly cadence:

- 2 theory sessions
- 2 implementation or lab sessions
- 1 review session for writeups, architecture notes, or postmortems

## Level Expectations

### Junior Engineers

Juniors should focus on:

- writing working code with good structure
- learning how systems fail in practice
- building debugging and testing habits
- understanding standard patterns before exploring advanced tradeoffs

Expected evidence of progress:

- small working labs
- passing tests
- short notes explaining concepts in plain language
- simple design docs for projects

### Senior Engineers

Seniors should focus on:

- system decomposition and architectural tradeoffs
- reliability, security, and operational controls
- failure analysis and cost-awareness
- designing bounded AI workflows instead of overusing agents

Expected evidence of progress:

- architecture decision records
- tradeoff writeups
- risk registers and rollout plans
- project reviews focused on reliability, governance, and cost

## Folder-by-Folder Plan

### 1. coding/

Purpose:
Build programming fluency and software engineering discipline.

Junior outcomes:

- write clean modules and reusable functions
- understand data structures and algorithm basics
- write tests for normal and edge cases
- debug failures using logs, traces, and step-by-step reasoning

Senior outcomes:

- review design quality and maintainability
- enforce testing strategy and code review standards
- identify concurrency, correctness, and performance risks
- choose appropriate abstractions without overengineering

Suggested topics:

- Python fluency
- data structures and algorithms
- software design
- testing and debugging
- concurrency basics

Suggested output:

- 3-5 coding exercises
- 1 service or CLI tool
- 1 refactoring exercise with before/after notes

### 2. db/

Purpose:
Build strong data and storage fundamentals.

Junior outcomes:

- model tables and relationships correctly
- understand indexes and query basics
- write CRUD queries safely
- understand transactions at a practical level

Senior outcomes:

- reason about isolation, consistency, scaling, and schema evolution
- identify query-plan and data-model bottlenecks
- choose storage patterns for operational systems and AI pipelines
- define boundaries between relational, cache, and vector storage

Suggested topics:

- relational modeling
- indexes and query planning
- transactions and isolation
- schema evolution
- caching and consistency tradeoffs
- vector storage basics

Suggested output:

- 1 schema design exercise
- 1 query optimization lab
- 1 design note comparing relational and vector retrieval use cases

### 3. os/

Purpose:
Understand how systems behave underneath application code.

Junior outcomes:

- understand processes, threads, memory, and filesystems
- diagnose basic resource problems such as CPU spikes or memory growth
- understand blocking versus asynchronous execution

Senior outcomes:

- reason about performance bottlenecks and concurrency hazards
- connect OS behavior to containers, runtimes, and production incidents
- explain how system-level limits affect service design

Suggested topics:

- processes and threads
- scheduling
- memory and virtual memory
- synchronization
- filesystems and I/O

Suggested output:

- 2 short notes explaining real production symptoms using OS concepts
- 1 small concurrency or process-control lab

### 4. cloud/

Purpose:
Learn how modern systems are deployed and operated at scale.

Junior outcomes:

- understand containers, deployments, and service basics
- understand networking at the service level
- deploy a small application with logs and configuration

Senior outcomes:

- reason about reliability, failure domains, scaling, and observability
- understand tradeoffs between managed services and self-managed systems
- design deployment and rollback strategies for production services

Suggested topics:

- containers
- Kubernetes basics
- service networking
- load balancing
- distributed systems basics
- observability infrastructure

Suggested output:

- 1 deployed sample app
- 1 architecture note on service topology and failure handling

### 5. security/

Purpose:
Build trust boundaries and safe engineering habits.

Junior outcomes:

- understand authn, authz, and secrets handling
- avoid common application-security mistakes
- understand the basics of threat modeling

Senior outcomes:

- define security boundaries across systems and vendors
- design least-privilege access and auditability
- reason about secure AI integration patterns and blast-radius limits

Suggested topics:

- authentication
- authorization
- secrets management
- secure coding
- threat modeling
- cloud security basics

Suggested output:

- 1 threat model
- 1 secure-design checklist

### 6. saas/

Purpose:
Understand the architectural realities of enterprise software.

Junior outcomes:

- understand tenants, users, roles, audit logs, and billing basics
- understand why enterprise products need control-plane discipline

Senior outcomes:

- design multi-tenant system boundaries
- reason about metering, auditability, and platform extensibility
- connect SaaS architecture to enterprise AI deployment constraints

Suggested topics:

- multitenancy
- RBAC
- billing and metering
- feature flags
- workflow modeling
- audit logs

Suggested output:

- 1 SaaS domain model
- 1 design note on multitenancy and auditability

### 7. llm/

Purpose:
Learn model-side foundations so application decisions are grounded in reality.

Junior outcomes:

- understand what transformers, tokens, embeddings, and inference are
- understand common failure modes such as hallucination and context loss
- use models with clearer expectations and fewer magic assumptions

Senior outcomes:

- reason about model capability, latency, and cost tradeoffs
- choose model patterns based on task requirements
- define evaluation criteria and escalation paths when models are insufficient

Suggested topics:

- transformers
- tokenization
- embeddings
- inference
- evaluation
- model limitations

Suggested output:

- 2 concept notes
- 1 comparison writeup across model/task tradeoffs

### 8. agent/

Purpose:
Study agent patterns as a technique, not as a default product answer.

Junior outcomes:

- understand planners, executors, tool use, and memory
- build simple bounded agents with clear inputs and outputs
- recognize looping and over-autonomy risks

Senior outcomes:

- evaluate whether an agent is justified versus a deterministic workflow
- design approval gates, rollback, and state management
- reason about failure containment and multi-agent complexity

Suggested topics:

- planning loops
- tool use
- memory patterns
- state tracking
- single-agent vs multi-agent design

Suggested output:

- 1 bounded tool-using agent
- 1 writeup comparing an agent to a workflow solution

### 9. enterprise_ai_app/

Purpose:
Bring everything together into enterprise AI systems that can be deployed responsibly.

Junior outcomes:

- implement controlled AI features with clear prompts, tools, and validation
- build retrieval and workflow components with tests
- understand guardrails, logs, and human approvals

Senior outcomes:

- design enterprise AI architecture end to end
- define evaluation, security, governance, and cost controls
- review rollout readiness, failure modes, and operating model

Suggested sequence inside this folder:

1. `00_strategy/`
2. `01_llm_foundations/`
3. `02_data_and_rag/`
4. `03_workflows_and_agents/`
5. `04_evals_and_guardrails/`
6. `05_observability_and_ops/`
7. `06_security_and_governance/`
8. `07_cost_latency_and_scaling/`
9. `08_enterprise_integrations/`
10. `09_projects_and_case_studies/`

Suggested output:

- 1 internal copilot design
- 1 approval-heavy workflow automation design
- 1 production-readiness checklist for an enterprise AI feature

## Recommended 24-Week Schedule

### Phase 1: Weeks 1-8

Focus:
CS and software engineering foundations

- Weeks 1-2: `coding/`
- Week 3: `db/`
- Week 4: `os/`
- Week 5: `cloud/`
- Week 6: `security/`
- Week 7: `saas/`
- Week 8: integration review and small project

Junior emphasis:

- implementation reps
- debugging practice
- short concept notes

Senior emphasis:

- architecture critiques
- tradeoff analysis
- design review notes

### Phase 2: Weeks 9-14

Focus:
LLM and agent foundations

- Weeks 9-11: `llm/`
- Weeks 12-13: `agent/`
- Week 14: compare agent patterns with deterministic workflows

Junior emphasis:

- build small prototypes
- inspect model failures
- learn structured-output discipline

Senior emphasis:

- define when not to use agents
- compare approaches by risk, reliability, and cost

### Phase 3: Weeks 15-22

Focus:
Enterprise AI application architecture and operations

- Week 15: `enterprise_ai_app/00_strategy/`
- Week 16: `enterprise_ai_app/01_llm_foundations/`
- Week 17: `enterprise_ai_app/02_data_and_rag/`
- Week 18: `enterprise_ai_app/03_workflows_and_agents/`
- Week 19: `enterprise_ai_app/04_evals_and_guardrails/`
- Week 20: `enterprise_ai_app/05_observability_and_ops/`
- Week 21: `enterprise_ai_app/06_security_and_governance/`
- Week 22: `enterprise_ai_app/07_cost_latency_and_scaling/` and `08_enterprise_integrations/`

Junior emphasis:

- build safe, bounded components
- test retrieval, prompts, and tool interfaces
- learn to log and debug AI behavior

Senior emphasis:

- define rollout and governance plans
- write architecture and operating model docs
- review integration risk and spend controls

### Phase 4: Weeks 23-24

Focus:
Capstone and review

- Week 23: implement capstone
- Week 24: conduct architecture review and postmortem

Capstone options:

- enterprise search assistant with permissions-aware retrieval
- support workflow assistant with approval gates
- document-processing workflow with auditability and fallback paths
- internal operations copilot with tool restrictions and logging

## Review Rubric

Every major project should be reviewed across the same dimensions:

- correctness
- maintainability
- observability
- security
- cost awareness
- user trust and failure handling

Junior review standard:

- can explain how the system works and where it fails
- can implement, test, and debug the feature

Senior review standard:

- can justify the architecture and tradeoffs
- can define rollout, governance, and operational safeguards

## How to Use This Repo

For each folder:

- create `notes/` for distilled learning
- create `labs/` for experiments
- create `projects/` for end-to-end builds
- create `checklists/` for review criteria

For each major topic:

- write one summary note
- complete one hands-on lab
- complete one small project or design review

This repo should gradually become both a study system and a reference system.
