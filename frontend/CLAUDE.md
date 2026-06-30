# faq-ai-agent Frontend Claude Code Guide

## Project Overview

The frontend is built with:

* Next.js (App Router)
* React
* TypeScript
* Tailwind CSS

The frontend communicates with the FastAPI backend through REST APIs.

The goal is to build a maintainable, production-oriented frontend suitable for AI-powered applications.

---

## Architecture Policy

Follow these principles:

* Feature-oriented structure
* Reusable UI components
* Separation of UI and API logic
* Type safety
* Small components
* Single Responsibility Principle

Avoid unnecessary complexity.

---

## Directory Guidelines

* `app/` : Routing, layouts and pages
* `components/` : Reusable UI components
* `features/` : Feature-specific components
* `services/` : API clients
* `types/` : TypeScript types
* `hooks/` : Custom React hooks
* `lib/` : Shared libraries and configuration
* `utils/` : Utility functions

---

## Coding Rules

* Prefer functional components.
* Use TypeScript strictly.
* Avoid `any`.
* Keep components small.
* Move business logic outside UI components.
* Prefer composition over large components.
* Use async/await instead of chained promises.
* Use absolute imports when appropriate.

---

## Styling

* Use Tailwind CSS.
* Avoid inline styles.
* Keep styling consistent.
* Extract repeated UI into reusable components.

---

## API Communication

* Keep API calls inside `services/`.
* Do not call APIs directly from UI components.
* Define request/response types.
* Handle loading and error states.

---

## Review Focus

When reviewing code, focus on:

* Maintainability
* Readability
* Component separation
* Type safety
* Performance
* Accessibility
* Next.js best practices

Do not over-engineer.

---

## Before Commit

Run:

```bash
npm run lint
npm run build
```
