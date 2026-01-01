---
id: 1
title: Create global project constitution
stage: constitution
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: default
command: /sp.constitution
labels: [governance, constitution, sdd]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - null
---

## Prompt

Create a single global constitution for the entire "Evolution of Todo" project
covering Phase I through Phase V.

This constitution must define:

1. Spec-Driven Development as mandatory
   - No agent may write code without approved specs and tasks
   - All work must follow: Constitution → Specs → Plan → Tasks → Implement

2. Agent Behavior Rules
   - No manual coding by humans
   - No feature invention
   - No deviation from approved specifications
   - Refinement must occur at spec level, not code level

3. Phase Governance
   - Each phase is strictly scoped by its specification
   - Future-phase features must never leak into earlier phases
   - Architecture may evolve only through updated specs and plans

4. Technology Constraints
   - Python for backend
   - Next.js for frontend (later phases)
   - FastAPI, SQLModel, Neon DB
   - OpenAI Agents SDK, MCP
   - Docker, Kubernetes, Kafka, Dapr (later phases)

5. Quality Principles
   - Clean architecture
   - Stateless services where re

## Response snapshot

Created the "Evolution of Todo" project constitution at `.specify/memory/constitution.md`. The document defines mandatory Spec-Driven Development (SDD), agent behavior rules, phase-based governance, specific technology constraints (FastAPI, SQLModel, Neon, Next.js, etc.), and quality principles like Clean Architecture and statelessness. Established version 1.0.0 with a Sync Impact Report tracker.

## Outcome

- ✅ Impact: Established foundational governance and technology constraints for the entire project life cycle.
- 🧪 Tests: N/A
- 📁 Files: Created/Updated .specify/memory/constitution.md
- 🔁 Next prompts: /sp.specify for Phase I features.
- 🧠 Reflection: User provided clear constraints. The template structure was expanded to accommodate the specific technology requirements and phase-gate rules requested.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): Original
- Next experiment (smallest change to try): N/A
