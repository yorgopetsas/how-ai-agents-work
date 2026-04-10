---
lang: en
title: AI Agent Type - Simple Reflex Agents
slug: agent-type-simple-reflex
date: 2026-04-10
section: agent-type
category: Agent Types
tags: [Open-Source, API, ChatGPT]
summary: Rule-based agents that react only to current input, without memory.
status: published
---

# Simple Reflex Agents

Simple reflex agents follow condition-action rules:

- If condition A happens, do action B.
- No memory of previous states.
- No planning.

In short: this is the fastest and easiest agent style to ship when the environment is stable and rules are clear.

## How it works (architecture)

1. Receive input or event.
2. Match input against fixed rules.
3. Execute predefined action.
4. End cycle.

This is often implemented as event triggers, webhook handlers, or policy-based routing with no long-term memory.

## Best use cases

- Deterministic automation
- Alerts and threshold triggers
- Very stable environments
- Basic lead routing
- Safety filters and policy enforcement

## Real-world company and service examples

These products are not always labeled "simple reflex," but many features behave this way internally:

- OpenAI - `omni-moderation-latest` (policy checks, allow/block style decisions).  
  Approximate price: **free** (API moderation endpoint, check current policy limits).
- Anthropic - Claude guardrail or policy-layer checks in front of model calls.  
  Approximate price: depends on model path; common API ranges are around **$1-$15 per 1M output tokens** for many production models.
- Zapier / Make style automations - "if trigger then action" business workflows.  
  Approximate price: commonly **$0 to $20+/month** depending on plan and task volume.

## Cost profile (rough)

- Build complexity: **Low**
- Runtime cost: **Low**
- Typical latency: **Very low**
- Best for: high-volume, low-complexity tasks

## Limitations

- Break under ambiguity
- Cannot reason over long tasks
- Repeats mistakes
- No adaptation unless humans update rules

## When to use vs avoid

Use when:
- You need reliability over creativity.
- The policy can be written as clear rules.
- Compliance and predictability matter most.

Avoid when:
- The task requires planning, memory, or optimization.
- Inputs are fuzzy, incomplete, or frequently changing.

## Quick implementation pattern

- Put a reflex gate first (cheap rules).
- Escalate only uncertain cases to a stronger goal-based or utility-based agent.
- Log rule misses weekly to improve rule coverage.
