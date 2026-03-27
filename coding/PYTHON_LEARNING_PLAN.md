# Python Learning Plan

This plan is for improving Python coding ability in two directions at the same time:

- algorithmic problem solving
- AI-oriented engineering

The point is not to treat these as separate worlds. Strong AI engineers still need solid data structures, debugging, API design, and implementation discipline. Strong algorithm practice also becomes more useful when it is applied to real systems.

## Outcomes

By the end of this track, you should be able to:

- solve common `ds/algo` problems cleanly in Python
- explain time and space complexity without guessing
- write Python that is testable, typed, and maintainable
- build AI-oriented components such as prompt pipelines, structured-output parsers, evaluation harnesses, and async tool integrations
- move from toy scripts to small production-style Python services

## Structure

The work is split into four stages:

1. `00_foundations/`
2. `01_ds_algo/`
3. `02_ai_engineering/`
4. `03_projects/`

Suggested duration: 12 weeks

- Weeks 1-2: Python foundations
- Weeks 3-6: `ds/algo`
- Weeks 7-10: AI engineering
- Weeks 11-12: integrated projects

Suggested weekly cadence:

- 3 practice sessions
- 1 implementation session
- 1 review session

## Stage 1: Python Foundations

Focus:

- syntax fluency
- functions and modules
- typing
- error handling
- file and JSON handling
- testing basics
- debugging basics

You should be able to:

- write small utilities without searching for basic syntax constantly
- organize code into modules instead of single scripts
- use `pytest` for straightforward unit tests
- use type hints to make interfaces easier to reason about

Deliverables:

- 5 short exercises
- 1 small CLI or parser utility
- 1 tested module

## Stage 2: DS/Algo in Python

Focus:

- arrays and strings
- hash maps and sets
- stacks and queues
- linked lists
- trees and graphs
- recursion and backtracking
- sorting and searching
- dynamic programming

Coding standard for this stage:

- solve first for correctness
- then explain complexity
- then refactor for clarity
- then compare alternative solutions

You should be able to:

- implement standard patterns from memory
- choose the right data structure deliberately
- explain why one solution is better than another
- avoid common Python-specific mistakes around mutation, copying, recursion, and default arguments

Deliverables:

- 20-30 solved problems
- 1 pattern cheat sheet
- 1 writeup comparing brute force, optimized, and idiomatic Python solutions
- 1 interview-practice set from `01_ds_algo/interview_practice/`

## Stage 3: AI Engineering in Python

Focus:

- API clients and SDK use
- prompt and response handling
- structured outputs
- retries and timeouts
- async calls
- batching
- embeddings and vector workflows
- evaluation harnesses
- logging and observability
- data cleaning and preprocessing

You should be able to:

- write wrappers around model APIs cleanly
- validate and parse model outputs instead of trusting raw strings
- build small evaluation scripts for prompts or workflows
- manage concurrency and rate limits without turning code into spaghetti
- structure AI code so it can evolve from script to service

Deliverables:

- 1 model-client wrapper
- 1 structured-output parser with tests
- 1 evaluation script
- 1 async or batched workflow exercise

## Stage 4: Integrated Projects

Focus:

- combine `ds/algo` rigor with AI-oriented engineering
- move beyond notebook-style code into reusable modules

Project ideas:

- document chunking and retrieval pipeline
- prompt evaluation harness with score aggregation
- support-ticket classifier with structured output validation
- tool-calling workflow with retry and fallback logic
- local dataset deduplication and indexing utility

Deliverables:

- 1 medium-size project
- 1 README explaining design decisions
- 1 test suite for core logic
- 1 short postmortem on what broke and what you changed

## Topic Map

### DS/Algo topics that matter most for Python growth

- arrays and strings
- dictionaries, sets, and heaps
- sorting and binary search
- recursion and backtracking
- trees and graphs
- dynamic programming
- sliding window and two pointers
- BFS and DFS

### Interview practice topics that matter most for hiring prep

- arrays, strings, and hash maps
- sliding window and two pointers
- intervals and scheduling
- heaps and top-k problems
- graph traversal and dependency ordering
- mutable data structure design
- tree traversal and recursion
- dynamic programming fundamentals

### AI engineering topics that matter most for Python growth

- clean data models
- request/response parsing
- schema validation
- asynchronous I/O
- retries and backoff
- file processing
- JSONL pipelines
- metrics and evaluation scripts
- logging and tracing hooks

## Quality Bar

Every exercise or project should be reviewed for:

- correctness
- readability
- complexity awareness
- testability
- error handling
- interface design

## How to Use This Folder

In each subfolder:

- keep notes brief
- prefer code over prose
- add tests when the logic is non-trivial
- write a short README only when it explains the exercise or tradeoff

If you want maximum improvement, alternate between:

- one `ds/algo` session that sharpens precision
- one AI engineering session that sharpens practical system-building
