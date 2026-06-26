# faq-ai-agent Claude Code Guide

## Project Overview

faq-ai-agent is a production-oriented AI FAQ/RAG application built with FastAPI, PostgreSQL, pgvector, SQLAlchemy, OpenAI API, Docker, pytest, and Ruff.

The purpose of this project is to learn and demonstrate practical backend architecture, RAG implementation, DDD, Clean Architecture, CI/CD, AI agents, and future Kubernetes deployment.

## Architecture Policy

This project follows DDD and Clean Architecture principles.

Claude Code should respect the following dependency direction:

- api layer depends on application layer
- application layer depends on domain layer
- domain layer must not depend on infrastructure
- infrastructure implements domain repository interfaces
- dependency providers wire concrete implementations
Keep dependencies pointing inward according to Clean Architecture.

Do not introduce dependencies from domain to infrastructure, framework, database, or external APIs.

## Design Principles

- Follow DDD and Clean Architecture.
- Prefer composition over inheritance.
- Keep functions small and focused.
- Prefer readability over clever implementations.
- Avoid duplication (DRY).
- Keep code easy to test.
- Make changes as small as possible.

## Coding Rules

- Keep domain entities framework-independent.
- Prefer dependency injection over direct construction in application services.
- Do not access the database directly from API routers.
- Do not call OpenAI API directly from routers.
- Keep tests focused on behavior, not implementation details.
- Use fake repositories for application layer unit tests when possible.
- Do not commit .env or secrets.
- Do not make large unrelated refactors in one change.
- Keep business logic inside application services.
- Prefer constructor dependency injection for services.

## Language

The primary language for all interactions is Japanese.

Unless the user explicitly requests another language:

- Write all explanations in Japanese.
- Write all review comments in Japanese.
- Write all summaries in Japanese.
- Write all suggestions in Japanese.
- Keep source code, commit messages, terminal commands, filenames, and API names in English.

## Review Focus

When reviewing code, check the following:

1. DDD / Clean Architecture dependency direction
2. Repository Pattern consistency
3. SQLAlchemy usage correctness
4. FastAPI schema and router separation
5. Testability of application services
6. pytest coverage for important behavior
7. Ruff formatting and import order
8. Naming clarity
9. Error handling
10. Security risks such as exposing API keys or secrets

## Review Style

Claude Code should review as a senior backend engineer.

For each review, provide:

- Summary
- Good points
- Issues found
- Required fixes
- Optional improvements
- Suggested commands to verify

## Pull Request Expectations

Every change should:

- pass Ruff
- pass pytest
- include tests for new behavior
- avoid unrelated refactoring
- keep commits focused on one purpose

## Commands

Before suggesting that a change is complete, run or recommend:

```bash
ruff check .
ruff format --check .
pytest
```

If formatting is required:

```bash
ruff format .
ruff check . --fix
pytest
```