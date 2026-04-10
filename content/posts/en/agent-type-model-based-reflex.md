---
lang: en
title: AI Agent Type - Model-Based Reflex Agents
slug: agent-type-model-based-reflex
date: 2026-04-10
section: agent-type
category: Agent Types
tags: [Open-Source, API, Cloude]
summary: Reflex agents with internal state to track partially observable environments.
status: published
---

# Model-Based Reflex Agents

Model-based reflex agents extend simple reflex behavior with an internal state model.

They keep short memory about the environment (what happened before), then still use reflex-style rules to act.

## How it works (architecture)

1. Observe current input.
2. Update internal state (recent context, status, last actions).
3. Match rules using both current input and state.
4. Execute action.

This is common in support bots, workflow bots, and stateful assistants where "current message only" is not enough.

## Best use cases

- Environments where not everything is visible at once
- Systems that need short memory
- Stateful workflows
- Session-aware assistants
- Incident handling with state transitions

## Trade-offs

- Better than pure reflex systems
- Still weaker than goal/utility planners for complex tasks
- State design can become fragile if not versioned

## Real-world company and service examples

Examples where stateful reflex behavior is common:

- OpenAI - Responses API tool-calling flows that keep conversation state and tool outputs in context.  
  Approximate API range: from about **$0.20 input / $1.25 output** up to **$2.50 input / $15 output per 1M tokens** depending on model class.
- Anthropic Claude API - stateful chat and tool sessions where decisions depend on prior turns.  
  Approximate API range: around **$1 input / $5 output** to **$3 input / $15 output per 1M tokens** for many common model tiers.
- Customer support platforms (Salesforce, Zendesk AI add-ons, Intercom AI) - ticket status and prior steps influence next action.  
  Approximate pricing: usually subscription or seat-based; often **tens to hundreds USD per agent/seat monthly** plus usage.

## Design tips

- Keep state minimal and explicit (`stage`, `last_action`, `confidence`).
- Add timeout/expiry for stale state.
- Store critical state server-side, not only in prompts.
- Add fallback: if state is inconsistent, route to human or reset safely.

## When to choose this type

Choose model-based reflex before goal-based if:
- The process is mostly deterministic.
- You need short memory but not full planning.
- You want low latency and low operational complexity.
