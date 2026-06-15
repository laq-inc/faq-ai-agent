# RAG Agent Review App

社内FAQを検索できるRAGアプリケーションです。

本プロジェクトでは、RAG実装だけでなく、Claude Codeによるコードレビュー、自動レビュー、AIエージェント化、Kubernetesデプロイまでを学習します。

---

# Goal

以下の技術を組み合わせた実践的なAIアプリケーションを構築します。

* Docker
* FastAPI
* PostgreSQL
* pgvector
* OpenAI API
* RAG
* AI Agent
* Claude Code
* GitHub Actions
* Kubernetes

---

# Roadmap

| Step | 内容                        |
| ---- | ------------------------- |
| 1    | Docker開発環境構築              |
| 2    | FastAPI API開発             |
| 3    | PostgreSQL + pgvector     |
| 4    | RAG実装                     |
| 5    | テスト実装（pytest）             |
| 6    | Dev Container導入           |
| 7    | コード品質改善（ruff / formatter） |
| 8    | Claude Codeローカルレビュー       |
| 9    | GitHub Actions CI         |
| 10   | Claude自動レビュー              |
| 11   | AIエージェント化                 |
| 12   | Kubernetes化               |
| 13   | GitHub公開                  |


---

# Architecture

```txt
faq-ai-agent/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
├── CLAUDE.md
├── REVIEW.md
├── app/
│   ├── main.py
│   ├── domain/
│   ├── usecase/
│   ├── infrastructure/
│   └── presentation/
├── tests/
├── .claude/
│   └── commands/
│       ├── review.md
│       ├── rag-review.md
│       └── agent-review.md
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── claude-review.yml
└── k8s/
    ├── namespace.yaml
    ├── deployment.yaml
    ├── service.yaml
    ├── configmap.yaml
    ├── secret.yaml
    └── postgres.yamlå
```

---

# RAG Flow

```txt
ユーザー質問
      ↓
FAQ検索
      ↓
関連ドキュメント取得
      ↓
OpenAIへ問い合わせ
      ↓
回答生成
```

---

# Agent Flow

```txt
ユーザー依頼
      ↓
意図解析
      ↓
実行ツール選択
      ↓
ツール実行
      ↓
結果返却
```

---

# Use Cases

### FAQ検索

```txt
有給申請の方法を教えて
```

↓

```txt
FAQ検索
→ 回答生成
```

### FAQ登録

```txt
このFAQを追加して
```

↓

```txt
FAQ登録
→ Embedding生成
→ DB保存
```

### 類似FAQ検索

```txt
似た質問があるか確認して
```

↓

```txt
類似FAQ検索
→ 結果表示
```

---

# Final Deliverables

* 社内FAQ RAGチャット
* FAQ管理AIエージェント
* Claude Codeレビュー環境
* GitHub Actions自動レビュー
* Kubernetesデプロイ環境
