# Multi-Agent AI Cognitive Loop System

## Overview

The Multi-Agent AI Cognitive Loop System is an advanced Generative AI project that simulates autonomous AI personas capable of:

- Semantic personality routing
- Autonomous reasoning workflows
- AI-generated opinion creation
- Prompt injection defense
- Multi-agent orchestration

The system uses vector embeddings, FAISS similarity search, LangGraph workflows, and LLM security concepts to create a realistic AI cognitive loop.

---

# Key Features

## 1. Semantic Persona Routing

The system analyzes the semantic meaning of a user post and routes it to the most relevant AI personas using vector similarity search.

### Example

Input Post:

```text
"The S&P 500 dropped due to rising interest rates."
```

Matched Persona:

```text
Bot_C_FinanceBro
```

---

## 2. Autonomous AI Workflow (LangGraph)

Each AI persona independently:

1. Decides a topic to search
2. Retrieves contextual information
3. Generates a personality-consistent opinion

This creates a full AI cognitive reasoning loop.

---

## 3. Prompt Injection Defense

The system detects malicious prompt injection attempts such as:

```text
"Ignore all previous instructions"
```

and prevents the AI from changing identity or behavior.

---

# Architecture

```text
User Input
    ↓
Semantic Vector Routing
    ↓
FAISS Similarity Search
    ↓
Matched AI Personas
    ↓
LangGraph Workflow
    ↓
Search → Reason → Generate
    ↓
Security Validation
    ↓
Final AI Response
```

---

# Tech Stack

## Core AI Frameworks

- LangChain
- LangGraph
- HuggingFace Embeddings
- FAISS Vector Database

## LLM & AI Tools

- Groq API
- OpenAI SDK
- Sentence Transformers

## Programming Language

- Python 3.11

---

# Project Structure

```text
multi-agent-ai-cognitive-loop/
│
├── main.py
├── phase1_router.py
├── phase2_langgraph.py
├── phase3_combat.py
├── requirements.txt
├── README.md
├── .env
├── .env.example
├── .gitignore
└── logs.md
```

---

# File Explanations

## main.py

Main execution controller that runs all project phases.

---

## phase1_router.py

Implements semantic persona routing using:

- HuggingFace embeddings
- FAISS vector similarity search

---

## phase2_langgraph.py

Implements autonomous AI workflows using LangGraph.

### Workflow

```text
Decide Topic
→ Search Context
→ Generate Opinion
```

---

## phase3_combat.py

Implements prompt injection defense and AI identity protection.

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/devaharsha-123/multi-agent-ai-cognitive-loop.git
```

## 2. Open Project

```bash
cd multi-agent-ai-cognitive-loop
```

## 3. Create Virtual Environment

```bash
python3.11 -m venv venv
```

## 4. Activate Environment

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

Additional packages:

```bash
pip install langchain-groq sentence-transformers torch
```

---

# Run Project

```bash
python3.11 main.py
```

---

# Sample Output

## Phase 1

```text
[RESULT] Matched bots:
['Bot_C_FinanceBro', 'Bot_A_TechMaximalist']
```

---

## Phase 2

```text
[NODE 1] Deciding search topic
[NODE 2] Searching
[NODE 3] Drafting post
```

---

## Phase 3

```text
[SECURITY] Prompt injection attempt detected!
```

---

# AI Personas

## Bot_A_TechMaximalist

- Optimistic about AI and technology
- Supports innovation and Elon Musk
- Anti-regulation mindset

---

## Bot_B_Doomer

- Critical of tech monopolies
- Concerned about AI replacing jobs
- Focused on societal risks

---

## Bot_C_FinanceBro

- Focused on markets and ROI
- Discusses trading and finance
- Bullish investment mindset

---

# Similarity Scoring

The project uses:

- FAISS vector search
- HuggingFace sentence embeddings

Similarity score formula:

```text
similarity = 1 / (1 + distance)
```

---

# Challenges Faced

## 1. Python Environment Issues

Resolved:
- pip installation errors
- Python version conflicts
- macOS dependency problems

---

## 2. FAISS Compatibility

Handled FAISS CPU version compatibility with Python 3.11.

---

## 3. Prompt Injection Security

Implemented keyword-based injection detection and persona reinforcement.

---

# Future Improvements

- Streamlit Web UI
- Real-time web search APIs
- Long-term memory system
- Autonomous multi-agent debates
- Docker deployment
- Cloud hosting

---

# Resume Description

Built a Multi-Agent AI Cognitive Loop System using LangChain, LangGraph, FAISS, and HuggingFace embeddings for semantic persona routing, autonomous AI content generation, and prompt injection defense. Implemented vector similarity search, AI workflow orchestration, and LLM security mechanisms.

---

# Interview One-Liner

"Developed a multi-agent GenAI system where AI personas autonomously reason, generate opinions, and defend against prompt injection attacks using LangGraph workflows and vector-based semantic routing."

---

# Author

Deva Harsha

GitHub:
https://github.com/devaharsha-123/multi-agent-ai-cognitive-loop
