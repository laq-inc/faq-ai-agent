# FAQ AI Agent

FAQ AI Agent is a full-stack AI-powered knowledge platform that enables users to search and manage company knowledge using Retrieval-Augmented Generation (RAG).

The project includes a modern web frontend built with Next.js and TypeScript, and a production-oriented backend built with FastAPI and PostgreSQL.

This project is not only about building a RAG application, but also about learning:

* DDD (Domain-Driven Design)
* Clean Architecture
* Modular Monolith
* Event-Driven Architecture
* Microservices
* AI Agents
* Claude Code Review
* GitHub Actions CI/CD
* Kubernetes

The goal is to build a practical system that can be used as a portfolio and serve as preparation for real-world AI development projects.

---

# Overview

FAQ AI Agent evolves from a simple RAG application into a production-ready full-stack AI platform.

Throughout the roadmap, the project demonstrates:

- Modern backend development with FastAPI
- Full-stack web development with Next.js
- Retrieval-Augmented Generation (RAG)
- AI Agent implementation
- DDD and Clean Architecture
- Cloud-native deployment with Kubernetes

---

# Goal

The goal of this project is to build a production-oriented AI application that demonstrates:

- Full-stack development
- Modern backend architecture
- AI application development
- Cloud-native deployment
- Scalable software architecture

while serving as a practical portfolio for AI and backend engineering roles.

---

# Roadmap

| Step | Description |
| ---- | ----------- |
| 1 | Docker Development Environment |
| 2 | FastAPI API Development |
| 3 | PostgreSQL + pgvector |
| 4 | RAG Implementation |
| 5 | Testing with pytest |
| 6 | Dev Container Setup |
| 7 | Code Quality Improvement (ruff / formatter) |
| 8 | Claude Code Local Review |
| 9 | Frontend Setup with Next.js / TypeScript |
| 10 | Frontend UI Refinement |
| 11 | FAQ / Knowledge Management UI |
| 12 | GitHub Actions CI |
| 13 | Claude Automated Review |
| 14 | GitHub Publication |
| 15 | AI Agent Implementation |
| 16 | Kubernetes Deployment |
| 17 | Modular Monolith Refactoring |
| 18 | Event-Driven Architecture |
| 19 | Microservices Migration |
| 20 | API Gateway Integration |
| 21 | Message Broker Integration |
| 22 | Kubernetes Operation for Microservices |
| 23 | Distributed Tracing & Monitoring |

---

# Tech Stack

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- Biome

## Backend

- FastAPI
- Python
- SQLAlchemy

## Database

- PostgreSQL
- pgvector

## AI

- OpenAI API
- Embedding
- RAG

## DevOps

- Docker
- GitHub Actions
- Kubernetes

## Architecture

- DDD
- Clean Architecture
- Modular Monolith
- Event-Driven Architecture
- Microservices

---

# Target Architecture

```txt
faq-ai-agent/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── pyproject.toml
│   ├── CLAUDE.md
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── features/
│   │   ├── utils/
│   │   ├── types/
│   │   └── lib/
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.ts
│   └── README.md
│
├── docker-compose.yml
├── Makefile
├── .env.example
├── README.md
│
├── .github/
│   └── workflows/
│
└── k8s/
```

---

# Full Stack Architecture

```txt
                +----------------------+
                |    Next.js Frontend  |
                +----------+-----------+
                           |
                      REST API
                           |
                +----------v-----------+
                |       FastAPI        |
                | DDD / Clean Arch.    |
                +----+------------+----+
                     |            |
                     |            |
        PostgreSQL + pgvector   OpenAI API
                               (LLM / Embeddings)
```

---

# RAG Flow

```txt
User Question
      ↓
Vector Search
      ↓
Related Documents Retrieval
      ↓
OpenAI API
      ↓
Generated Answer
```

---

# Agent Flow

```txt
User Request
      ↓
Intent Analysis
      ↓
Tool Selection
      ↓
Tool Execution
      ↓
Response Generation
```

---

# Use Cases

## FAQ Search

Input:

```txt
How do I apply for paid leave?
```

Process:

```txt
FAQ Search
→ Retrieve Related Documents
→ Generate Answer
```

---

## FAQ Registration

Input:

```txt
Add this FAQ
```

Process:

```txt
FAQ Registration
→ Generate Embedding
→ Save to Database
```

---

## Similar FAQ Search

Input:

```txt
Find similar questions
```

Process:

```txt
Similarity Search
→ Display Results
```

---

# Development Principles

## Domain-Driven Design (DDD)

The project follows DDD principles:

* Entity
* Value Object
* Repository
* Domain Service
* Aggregate

---

## Clean Architecture

Dependency direction:

```txt
Presentation (FastAPI)
        │
        ▼
Application (Use Cases)
        │
        ▼
Domain
├── Entity
├── Value Object
├── Repository Interface
└── Domain Service
        ▲
        │ implements
        │
Infrastructure
├── SQLAlchemy Repository
├── PostgreSQL
├── pgvector
└── OpenAI API
```

Business rules do not depend on frameworks or databases.

---

## Modular Monolith

The application will first be structured as a modular monolith.

```txt
modules/
├── faq
├── document
├── embedding
├── chat
└── auth
```

Each module communicates through well-defined interfaces.

---

## Microservices

After the modular monolith stage, modules will be extracted into independent services.

```txt
API Gateway
      │
 ┌────┼────┐
 │    │    │
FAQ Chat Auth
 │
Kafka
 │
Embedding
```

---

# Frontend Features

* FAQ List
* FAQ Registration
* Knowledge Search
* AI Chat Interface
* Responsive UI
* Type-safe API Communication

---

# Backend Features

* REST API
* RAG Search
* Embedding Generation
* Vector Similarity Search
* DDD
* Clean Architecture
* Repository Pattern
* AI Agent

---

# Future Enhancements

* Multi-document RAG
* Hybrid Search
* Agent Memory
* Tool Calling
* Multi-Agent Architecture
* Observability
* Auto Scaling
* GitOps Deployment
* ArgoCD Integration

---

# Final Deliverables

* Full-Stack AI Application
* Next.js Frontend
* FastAPI Backend
* FAQ RAG Chat System
* AI Agent
* DDD Sample Application
* Clean Architecture Sample
* Modular Monolith Sample
* Microservices Sample
* Claude Code Review Environment
* GitHub Actions CI/CD
* Kubernetes Deployment Environment
* Production-Oriented AI Portfolio

---

# Development

Run the following commands from the project root.

## Start the frontend development server

```bash
make frontend-dev
```

The frontend is available at:

```text
http://localhost:3000
```

Stop the development server with `Ctrl + C`.

## Run backend tests

```bash
make backend-test
```

## Validate the backend

Run formatting checks, lint checks, and tests:

```bash
make backend-validate
```

## Automatically fix backend code style

Run Ruff auto-fix and formatting:

```bash
make backend-fix
```

## Validate the frontend

Run Biome checks and create a production build:

```bash
make frontend-validate
```

Stop the frontend development server before running this command because the development server and production build both use the `frontend/.next` directory.

## Validate the entire project

Run all backend and frontend validations:

```bash
make validate
```

## Start the frontend production server

Build and start the frontend production server:

```bash
make frontend-start
```

The frontend is available at:

```text
http://localhost:3000
```


---

# Screenshots

## Home

(TODO)

## Knowledge Search

(TODO)

## AI Chat

(TODO)

## Knowledge Management

(TODO)

---

# Demo

(TODO)

---

# License

MIT License
