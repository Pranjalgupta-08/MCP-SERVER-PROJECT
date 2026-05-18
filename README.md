# MCP SERVER PROJECT 🚀

This repository contains my learning and hands-on implementation of MCP (Model Context Protocol) concepts using Python, HTTP communication, and Docker.

The goal of this project was to understand how modern AI systems and tools can communicate in a structured way using MCP architecture.

---

# 📚 What I Learned

* MCP Server basics
* HTTP-based MCP communication
* Python project structuring
* Docker setup for MCP services
* Virtual environment management using `uv`
* Git & GitHub workflow
* Understanding how AI systems interact with external tools/services

---

# 🛠️ Tech Stack

* Python 🐍
* MCP
* HTTP
* Docker 🐳
* Git & GitHub

---

# 📂 Project Structure

```bash
MCP-SERVER-PROJECT/
│
├── CH-2_HTTP_MCP/
├── CH-6_MCP_Docker/
├── src/
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Pranjalgupta-08/MCP-SERVER-PROJECT.git
```

## 2. Move into Project

```bash
cd MCP-SERVER-PROJECT
```

## 3. Create Virtual Environment

Using `uv`:

```bash
uv venv
```

Activate environment:

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

# ▶️ Run Project

Install dependencies:

```bash
uv sync
```

Run project files/chapters as needed.

Example:

```bash
python filename.py
```

---

# 🐳 Docker

For Docker-based chapters:

```bash
docker build -t mcp-server .
docker run -p 8000:8000 mcp-server
```

---

# 🔗 GitHub Repository

Repository Link:

https://github.com/Pranjalgupta-08/MCP-SERVER-PROJECT

---

# 📌 Note

This is a beginner learning project created while exploring MCP architecture and AI system integrations.

Still learning and improving 🚀
