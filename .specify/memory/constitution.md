<!--
Sync Impact Report
- Version change: [INITIAL] -> 1.0.0
- List of modified principles:
  - Spec-Driven Development (SDD) -> I. Spec-Driven Development (SDD)
  - Agent Behavior Rules -> II. Agent Behavior Rules
  - Phase Governance -> III. Phase Governance
  - Technology Constraints -> IV. Technology Constraints
  - Quality Principles -> V. Quality Principles
- Added sections: Core Principles, Governance
- Removed sections: N/A
- Templates requiring updates:
  - .specify/templates/plan-template.md (⚠ pending)
  - .specify/templates/spec-template.md (⚠ pending)
  - .specify/templates/tasks-template.md (⚠ pending)
- Follow-up TODOs: Initial ratification.
-->

# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development (SDD)
Spec-Driven Development is mandatory for all contributors. No agent or human may write production code without approved specifications and tasks.
Rules:
- All work MUST follow the flow: Constitution → Specs → Plan → Tasks → Implement.
- Implementation only begins once tasks are defined and verified against the plan.
- Specifications must be detailed enough to prevent ambiguity during implementation.

### II. Agent Behavior Rules
Agents are the primary executors of development.
Rules:
- No manual coding by humans is permitted for production features; humans act as architects and reviewers.
- No feature invention: Agents must not add functionality that is not explicitly defined in the approved specification.
- No deviation from approved specifications: All implementation must align 100% with the spec.
- Refinement must occur at the specification level, not the code level. If the code reveals a spec flaw, the spec must be updated and approved first.

### III. Phase Governance
The project evolves through strictly defined phases (Phases I through V).
Rules:
- Each phase is strictly scoped by its respective specification.
- Future-phase features must NEVER leak into earlier phases (e.g., no Next.js scaffolding in Phase I Python-only tasks).
- Architecture may evolve only through updated specifications and architectural plans.

### IV. Technology Constraints
The following stack is mandatory and must not be bypassed without a constitutional amendment:
Backend:
- Python
- FastAPI
- SQLModel
- Neon DB
- OpenAI Agents SDK
- MCP
Frontend (Later Phases):
- Next.js
Distributed Systems (Later Phases):
- Docker
- Kubernetes
- Kafka
- Dapr

### V. Quality Principles
All development must adhere to high-quality software engineering standards.
Rules:
- Clean Architecture: Maintain strict separation of concerns and dependency inversion.
- Stateless Services: Services should be stateless whenever possible to ensure horizontal scalability.
- Test-First: Implementation is driven by passing the test cases defined in the tasks.

## Governance
This constitution is the supreme authority for the "Evolution of Todo" project.
Rules:
- All Pull Requests and code reviews must verify compliance with these principles.
- Complexity must be justified and minimal (YAGNI).
- Amendments to this constitution require a version bump and updates to all dependent templates.
- Any conflict between a specification and this constitution is resolved in favor of the constitution.

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
