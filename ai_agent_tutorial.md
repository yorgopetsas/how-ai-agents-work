# 🧠 Tutorial: Build Your First AI Agent (2 Free Paths)

## What you will build

In this tutorial, you will build a simple AI Agent that can:

- Take a task from the user
- Think about it step by step
- Produce a structured output
- (Optional) keep simple memory

You will build the same agent in **two different ways**:
- 🟢 No-code (Flowise + Ollama)
- 🟡 Code (Python + Ollama)

Both approaches lead to the same result: a working first AI Agent.

---

# 🟢 PART A — No-Code AI Agent (Flowise + Ollama)

> Best for beginners and non-technical users

---

## STEP 1 — Install Ollama (Local AI Model)

Go to: https://ollama.com

Install it for your system.

Then open your terminal and run:

```bash
ollama run llama3.1
```

---

## STEP 2 — Install Node.js

Download Node.js: https://nodejs.org

Install the LTS version.

```bash
node -v
npm -v
```

---

## STEP 3 — Install Flowise

```bash
npx flowise start
```

Open: http://localhost:3000

---

## STEP 4 — Create Flow

Click “Create New Chat Flow”

---

## STEP 5 — Add ChatOllama Node

- Base URL: http://localhost:11434  
- Model: llama3.1

---

## STEP 6 — Prompt Template

```text
You are an AI Agent.
Break tasks into steps and respond clearly.

Task: {input}
```

---

## STEP 7 — Connect Nodes

User Input → Prompt → ChatOllama → Output

---

## STEP 8 — Test

Example:

Plan a simple website structure for a coffee shop

---

## STEP 9 — Improve Prompt

```text
You are an AI Agent.

1. Understand the task
2. Break into steps
3. Provide structured output

Task: {input}
```

---

## STEP 10 — Add Thinking

Always think step-by-step before answering.

---

## STEP 11 — Save

Name: My First AI Agent

---

## STEP 12 — Result

You built your first AI Agent system.

---

# 🟡 PART B — Code AI Agent (Python + Ollama)

---

## STEP 1 — Install Python

https://python.org

```bash
python --version
```

---

## STEP 2 — Run Ollama

```bash
ollama run llama3.1
```

---

## STEP 3 — Install Dependency

```bash
pip install requests
```

---

## STEP 4 — Create File

agent.py

---

## STEP 5 — Code

```python
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
```

---

## STEP 6 — Agent

```python
def agent(task):
    prompt = f"""
You are an AI Agent.

Step 1: Understand
Step 2: Break steps
Step 3: Solve

Task: {task}
"""
    return ask_ai(prompt)
```

---

## STEP 7 — Run

```python
print(agent("Build a login system"))
```

---

## STEP 8 — Memory

```python
memory = []

def agent(task):
    context = "\n".join(memory[-5:])

    prompt = f"""
Memory:
{context}

Task: {task}
"""

    result = ask_ai(prompt)
    memory.append(task)
    memory.append(result)

    return result
```

---

## STEP 9 — Test

```python
print(agent("Create a to-do app"))
print(agent("Improve it"))
```

---

## STEP 10 — Result

Agent now remembers.

---

## STEP 11 — Why it's an Agent

Input → Process → Memory → Output

---

## STEP 12 — Final Insight

An AI Agent = System around the model.

---

# 🔥 Summary

You built:
- No-code agent
- Code agent

Same principle:

AI ≠ model  
AI = system
