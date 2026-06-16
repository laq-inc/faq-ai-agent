# FAQ AI Agent

A production-oriented AI application project for learning modern backend architecture and AI development.

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

FAQ AI Agent is an AI-powered FAQ platform that enables users to search company knowledge using RAG (Retrieval-Augmented Generation).

The project evolves step by step from a simple RAG application into a production-ready platform with:

* AI Agent capabilities
* Automated code reviews
* CI/CD pipelines
* Kubernetes deployment
* Microservice architecture

---

# Goal

Build a practical AI application using the following technologies:

* Python
* FastAPI
* PostgreSQL
* pgvector
* OpenAI API
* RAG
* AI Agents
* Docker
* DDD
* Clean Architecture
* Modular Monolith
* Event-Driven Architecture
* Microservices
* Claude Code
* GitHub Actions
* Kubernetes

---

# Roadmap

| Step | Description                                 |
| ---- | ------------------------------------------- |
| 1    | Docker Development Environment              |
| 2    | FastAPI API Development                     |
| 3    | PostgreSQL + pgvector                       |
| 4    | RAG Implementation                          |
| 5    | Testing with pytest                         |
| 6    | Dev Container Setup                         |
| 7    | Code Quality Improvement (ruff / formatter) |
| 8    | Claude Code Local Review                    |
| 9    | GitHub Actions CI                           |
| 10   | Claude Automated Review                     |
| 11   | AI Agent Implementation                     |
| 12   | Kubernetes Deployment                       |
| 13   | GitHub Publication                          |
| 14   | Modular Monolith Refactoring                |
| 15   | Event-Driven Architecture                   |
| 16   | Microservices Migration                     |
| 17   | API Gateway Integration                     |
| 18   | Message Broker Integration                  |
| 19   | Kubernetes Operation for Microservices      |
| 20   | Distributed Tracing & Monitoring            |

---

# Current Architecture

```txt
faq-ai-agent/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
└── app/
    └── main.py
```

---

# Target Architecture

```txt
faq-ai-agent/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
├── CLAUDE.md
├── REVIEW.md
│
├── app/
│   ├── domain/
│   ├── usecase/
│   ├── infrastructure/
│   ├── presentation/
│   └── shared/
│
├── tests/
│
├── .claude/
│   └── commands/
│       ├── review.md
│       ├── rag-review.md
│       └── agent-review.md
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── claude-review.yml
│
└── k8s/
    ├── namespace.yaml
    ├── deployment.yaml
    ├── service.yaml
    ├── configmap.yaml
    ├── secret.yaml
    └── postgres.yaml
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
Presentation
      ↓
UseCase
      ↓
Repository Interface
      ↓
Infrastructure
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

* FAQ RAG Chat System
* FAQ Management AI Agent
* DDD Sample Application
* Clean Architecture Sample
* Modular Monolith Sample
* Microservices Sample
* Claude Code Review Environment
* GitHub Actions CI/CD
* Kubernetes Deployment Environment
* Production-Oriented AI Application Portfolio

---

# License

MIT License
