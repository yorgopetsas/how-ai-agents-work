---
lang: en
title: Tutorial - Build Your First AI Agent (2 Free Paths)
slug: tutorial-build-your-first-ai-agent
date: 2026-04-09
section: tutorial
difficulty: dev-no-ai
category: Tutorial
tags: [Open-Source, API, Cloude, OpenAI, ChatGPT]
summary: Two free paths to the same outcome—no-code (Flowise + Ollama) and code (Python + Ollama)—so you see that an agent is the system around the model, not the model alone.
status: published
template: tutorial_md
---

# Tutorial: Build Your First AI Agent (2 Free Paths)

## What you will build

You will build a simple AI agent that can:

- Take a task from the user
- Think about it step by step
- Produce structured output
- (Optional) keep simple memory

You will build the **same idea** in two ways:

- **No-code** — Flowise + Ollama  
- **Code** — Python + Ollama  

Both paths lead to a working first agent.

---

# Copy Commands

Use these command snippets directly.

```bash
# Ollama model
ollama run llama3.1
```

```bash
# Check Node.js
node -v
npm -v
```

```bash
# Start Flowise
npx flowise start
```

```bash
# Python deps
pip install requests
```

---

# PART A — No-Code AI Agent (Flowise + Ollama)

> Best for beginners, non-technical users, and fast understanding.

## STEP 1 — Install Ollama (Local AI Model)

Go to `https://ollama.com`, install it, then run:

```bash
ollama run llama3.1
```

## STEP 2 — Install Node.js

Download and install the LTS version from `https://nodejs.org`, then verify:

```bash
node -v
npm -v
```

## STEP 3 — Install Flowise

```bash
npx flowise start
```

Open: `http://localhost:3000`

## STEP 4 — Create Your First Flow

In Flowise, create a new chat flow and add:

- User Input
- Prompt Template
- ChatOllama
- Output

## STEP 5 — Add Chat Model Node

Use:

- Base URL: `http://localhost:11434`
- Model: `llama3.1`

## STEP 6 — Add Prompt Template

```text
You are an AI Agent.
Break tasks into steps and respond clearly.

Task: {input}
```

## STEP 7 — Connect the System

```text
User Input → Prompt Template → ChatOllama → Output
```

## STEP 8 — Test Your Agent

```text
Plan a simple website structure for a coffee shop
```

## STEP 9 — Improve Structure

```text
You are an AI Agent.

Follow this structure:
1. Understand the task
2. Break it into steps
3. Provide a final structured answer

Task: {input}
```

## STEP 10 — Add System Thinking Instruction

```text
Always think step-by-step before answering.
```

## STEP 11 — Save Your Flow

Save as `My First AI Agent`.

## STEP 12 — What You Built

You built a controlled reasoning pipeline, not just a chatbot.

---

# PART B — Code-Based AI Agent (Python + Ollama)

> Best for developers who want to understand the internals.

## STEP 1 — Install Python

Install from `https://python.org`, then verify:

```bash
python --version
```

## STEP 2 — Install Ollama

```bash
ollama run llama3.1
```

## STEP 3 — Install Python Dependency

```bash
pip install requests
```

## STEP 4 — Create Project File

Create `agent.py`.

## STEP 5 — Basic AI Connection

```python
import requests

MODEL = "llama3.1"
URL = "http://localhost:11434/api/generate"

def ask_ai(prompt):
    response = requests.post(
        URL,
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=60,
    )
    return response.json()["response"]
```

## STEP 6 — Create Your Agent Logic

```python
def agent(task):
    prompt = f"""
You are an AI Agent.

Step 1: Understand the task
Step 2: Break it into steps
Step 3: Provide a structured solution

Task: {task}
"""
    return ask_ai(prompt)
```

## STEP 7 — Run Your Agent

```python
result = agent("Design a simple login system")
print(result)
```

## STEP 8 — Add Simple Memory (Optional)

```python
memory = []

def agent(task):
    context = "\n".join(memory[-5:])
    prompt = f"""
You are an AI Agent.

Memory:
{context}

Task: {task}
"""
    result = ask_ai(prompt)
    memory.append(task)
    memory.append(result)
    return result
```

## STEP 9 — Test Multiple Calls

```python
print(agent("Create a to-do app"))
print(agent("Now improve it"))
```

## STEP 10 — What Changed?

The agent now maintains context across requests.

## STEP 11 — Why This Is an Agent

It receives input, runs logic, maintains memory, and returns structured output.

## STEP 12 — Final insight

An AI agent is not only the model; it is the **system** around the model.

---

## Summary

You built:

- A **no-code** agent (Flowise + Ollama)
- A **code** agent (Python + Ollama)

Same principle:

**AI ≠ model — AI = system** (the orchestration, prompts, tools, and memory around the model).