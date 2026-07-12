FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    git \
    curl \
    ca-certificates \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

RUN npm install -g @anthropic-ai/claude-code

RUN npm install -g @openai/codex

COPY . .

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]