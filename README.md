# Local LLM API Bridge

> Bridge local LLM models (Ollama, llama.cpp) to OpenAI-compatible API endpoints.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-teal)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

Local LLM API Bridge is a lightweight FastAPI proxy that exposes locally running LLM models (via Ollama or llama.cpp) through OpenAI-compatible REST API endpoints. This allows any application or SDK built for the OpenAI API to seamlessly work with local models, enabling private, offline, and cost-free inference.

## Features

- OpenAI-compatible `/v1/chat/completions` endpoint
- Proxy requests to local Ollama instance
- Drop-in replacement for OpenAI API in existing applications
- FastAPI-based with automatic OpenAPI documentation
- Lightweight with minimal dependencies
- Support for any model available in Ollama

## Tech Stack

- **Language**: Python 3.9+
- **Framework**: FastAPI
- **HTTP Client**: Requests
- **ASGI Server**: Uvicorn
- **LLM Backend**: Ollama (default port 11434)

## Prerequisites

Ollama must be installed and running locally:

```bash
# Install Ollama (https://ollama.ai)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama3

# Verify Ollama is running
curl http://localhost:11434/api/tags
```

## Quick Start

```bash
# Clone the repository
git clone https://github.com/razinahmed/local-llm-api-bridge.git
cd local-llm-api-bridge

# Install dependencies
pip install -r requirements.txt

# Start the API bridge
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Test the endpoint
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "llama3", "messages": [{"role": "user", "content": "Hello"}]}'
```

## Project Structure

```
local-llm-api-bridge/
├── app/
│   └── main.py         # FastAPI application with proxy endpoint
├── requirements.txt    # Python dependencies
├── Makefile            # Build and test commands
├── LICENSE             # MIT License
├── SECURITY.md         # Security policy
└── README.md           # Project documentation
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/chat/completions` | Chat completion (OpenAI-compatible) |
| GET | `/docs` | Interactive API documentation (Swagger UI) |

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| Ollama host | `localhost:11434` | Ollama API base URL |
| Bridge port | `8000` | Port for the FastAPI bridge server |

## Use Cases

- Use local models with OpenAI SDKs (Python, Node.js, etc.)
- Private inference without sending data to cloud APIs
- Development and testing without API key costs
- Air-gapped environments requiring local LLM access

## Contributing

Contributions are welcome. Fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
