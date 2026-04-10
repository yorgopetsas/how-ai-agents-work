---
lang: en
title: Tutorial - Build Your First AI Agent (2 Free Paths)
slug: tutorial-build-your-first-ai-agent
date: 2026-04-09
section: tutorial
difficulty: dev-no-ai
category: Tutorial
tags: [Open-Source, API, Cloude, OpenAI, ChatGPT]
summary: A combined no-code and code-based tutorial path for developers entering AI agents.
status: published
---

# Tutorial: Build Your First AI Agent (2 Free Paths)

## What you will build
A simple AI Agent that:
- Takes a task from the user
- Thinks about it step by step
- Produces a structured result
- (Optional) keeps basic memory

No frameworks, no complexity—just the core idea of an agent.

---

# 🟢 PART A — No-Code AI Agent (Flowise + Ollama)

> Best for beginners, non-technical users, and fast understanding

---

## STEP 1 — Install Ollama (Local AI Model)

Go to: https://ollama.com

Install it for your system.

Then open terminal and run:

```bash
ollama run llama3.1

You now have your first local AI model running.

👉 Why this matters:
You now have an AI running locally—no API, no cloud.

STEP 2 — Install Node.js

Download:
https://nodejs.org

Install the LTS version.

Check installation:

node -v
npm -v

STEP 3 — Install Flowise

Run:
npx flowise start
Then open:
http://localhost:3000
👉 You now have a visual AI builder running locally.

STEP 4 — Create Your First Flow

In Flowise:

Click “Create New Chat Flow”
You will see a blank canvas

This is your AI system workspace.

STEP 5 — Add Chat Model Node

Add a node:

ChatOllama

Configure it:

Base URL: http://localhost:11434
Model: llama3.1
STEP 6 — Add Prompt Template

Add a Prompt Template node and use:

You are an AI Agent.
Break tasks into steps and respond clearly.

Task: {input}

STEP 7 — Connect the System

Connect the nodes like this:

User Input → Prompt Template → ChatOllama → Output

👉 This is your first AI system pipeline.

STEP 8 — Test Your Agent

Try this input:

Plan a simple website structure for a coffee shop

You now have a working AI Agent.

STEP 9 — Improve Structure

Update your prompt:

You are an AI Agent.

Follow this structure:
1. Understand the task
2. Break it into steps
3. Provide a final structured answer

Task: {input}
STEP 10 — Add System Thinking Instruction

Add this line:

Always think step-by-step before answering.
STEP 11 — Save Your Flow
Click Save
Name it: My First AI Agent
STEP 12 — What You Built

You did NOT build a chatbot.

You built:

A controlled reasoning system
A structured input/output pipeline
A basic AI agent architecture

👉 This is the foundation of all modern AI systems.

🟡 PART B — Code-Based AI Agent (Python + Ollama)

Best for people who want to understand how agents actually work

STEP 1 — Install Python

Download Python:
https://python.org

Check installation:

python --version
STEP 2 — Install Ollama

Same as before:

ollama run llama3.1
STEP 3 — Install Python Dependency
pip install requests
STEP 4 — Create Project File

Create a file called:

agent.py
STEP 5 — Basic AI Connection

Paste this code:

import requests

MODEL = "llama3.1"
URL = "http://localhost:11434/api/generate"

def ask_ai(prompt):
    response = requests.post(URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]
STEP 6 — Create Your Agent Logic
def agent(task):
    prompt = f"""
You are an AI Agent.

Step 1: Understand the task
Step 2: Break it into steps
Step 3: Provide a structured solution

Task: {task}
"""
    return ask_ai(prompt)
STEP 7 — Run Your Agent
result = agent("Design a simple login system")
print(result)
STEP 8 — Add Simple Memory (Optional)
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
STEP 9 — Test Multiple Calls
print(agent("Create a to-do app"))
print(agent("Now improve it"))
STEP 10 — What Changed?

Now your agent can:

Remember previous interactions
Use context over time
Improve continuity of responses
STEP 11 — Why This Is an Agent

Because it:

Receives input
Processes instructions
Maintains memory
Produces structured outputs

This is the core definition of an AI Agent.

STEP 12 — Final Insight

You just built the foundation of modern AI systems.

Not a chatbot.

A system that transforms input into controlled behavior.

🔥 Final Summary

You now have two versions of your first AI Agent:

🟢 No-code version (Flowise)
🟡 Code version (Python)

Both demonstrate the same principle:

An AI Agent is not the model.
It is the system built around the model.