---
lang: es
title: Tutorial — Construye tu primer agente de IA (2 rutas gratuitas)
slug: tutorial-build-your-first-ai-agent
date: 2026-04-09
section: tutorial
difficulty: dev-no-ai
category: Tutorial
tags: [Open-Source, API, Cloude, OpenAI, ChatGPT]
summary: Tutorial combinado sin código y con código para desarrolladores que empiezan con agentes de IA.
status: published
template: tutorial_md
---

# Tutorial: construye tu primer agente de IA (2 rutas gratuitas)

## Qué vas a construir

Un agente de IA sencillo que:

- Recibe una tarea del usuario
- La piensa paso a paso
- Produce un resultado estructurado
- (Opcional) mantiene memoria básica

Sin marcos ni complejidad innecesaria —solo la idea central del agente.

---

# Comandos para copiar

Usa estos fragmentos directamente.

```bash
# Modelo Ollama
ollama run llama3.1
```

```bash
# Comprobar Node.js
node -v
npm -v
```

```bash
# Iniciar Flowise
npx flowise start
```

```bash
# Dependencias Python
pip install requests
```

---

# PARTE A — Agente de IA sin código (Flowise + Ollama)

> Ideal para principiantes, perfiles no técnicos y comprensión rápida.

## PASO 1 — Instalar Ollama (modelo local)

Ve a `https://ollama.com`, instálalo y ejecuta:

```bash
ollama run llama3.1
```

## PASO 2 — Instalar Node.js

Descarga e instala la versión LTS desde `https://nodejs.org` y verifica:

```bash
node -v
npm -v
```

## PASO 3 — Instalar Flowise

```bash
npx flowise start
```

Abre: `http://localhost:3000`

## PASO 4 — Crear tu primer flujo

En Flowise, crea un nuevo chat flow y añade:

- Entrada de usuario
- Plantilla de prompt
- ChatOllama
- Salida

## PASO 5 — Nodo de modelo de chat

Usa:

- URL base: `http://localhost:11434`
- Modelo: `llama3.1`

## PASO 6 — Plantilla de prompt

```text
You are an AI Agent.
Break tasks into steps and respond clearly.

Task: {input}
```

## PASO 7 — Conectar el sistema

```text
User Input → Prompt Template → ChatOllama → Output
```

## PASO 8 — Probar tu agente

```text
Plan a simple website structure for a coffee shop
```

## PASO 9 — Mejorar la estructura

```text
You are an AI Agent.

Follow this structure:
1. Understand the task
2. Break it into steps
3. Provide a final structured answer

Task: {input}
```

## PASO 10 — Añadir instrucción de razonamiento

```text
Always think step-by-step before answering.
```

## PASO 11 — Guardar el flujo

Guárdalo como `My First AI Agent`.

## PASO 12 — Qué has construido

Has construido un pipeline de razonamiento controlado, no solo un chatbot.

---

# PARTE B — Agente de IA con código (Python + Ollama)

> Para desarrolladores que quieren entender los entresijos.

## PASO 1 — Instalar Python

Instala desde `https://python.org` y verifica:

```bash
python --version
```

## PASO 2 — Instalar Ollama

```bash
ollama run llama3.1
```

## PASO 3 — Dependencia de Python

```bash
pip install requests
```

## PASO 4 — Crear el archivo del proyecto

Crea `agent.py`.

## PASO 5 — Conexión básica con la IA

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

## PASO 6 — Lógica del agente

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

## PASO 7 — Ejecutar el agente

```python
result = agent("Design a simple login system")
print(result)
```

## PASO 8 — Memoria simple (opcional)

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

## PASO 9 — Probar varias llamadas

```python
print(agent("Create a to-do app"))
print(agent("Now improve it"))
```

## PASO 10 — ¿Qué cambió?

El agente mantiene contexto entre peticiones.

## PASO 11 — Por qué esto es un agente

Recibe entrada, ejecuta lógica, mantiene memoria y devuelve salida estructurada.

## PASO 12 — Idea final

Un agente de IA no es solo el modelo; es el sistema alrededor del modelo.
