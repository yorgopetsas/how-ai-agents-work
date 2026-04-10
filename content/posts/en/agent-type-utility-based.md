---
lang: en
title: AI Agent Type - Utility-Based Agents
slug: agent-type-utility-based
date: 2026-04-10
section: agent-type
category: Agent Types
tags: [API, OpenAI, Cloude]
summary: Agents that score outcomes and pick the action with the best utility trade-off.
status: published
---

# Utility-Based Agents

Utility-based agents rank options by preference, cost, risk, or reward and then choose the highest utility action.

Unlike goal-based agents (which ask "does this reach the goal?"), utility-based agents ask "which option gives the best overall value?"

## How it works (architecture)

1. Define utility function (score formula).
2. Generate candidate actions.
3. Estimate utility for each candidate.
4. Choose highest expected utility.
5. Update weights based on outcomes.

## Example utility function

`utility = 0.5 * quality + 0.3 * speed + 0.2 * cost_efficiency - risk_penalty`

You can tune weights for each business context.

## Best use cases

- Trade-off optimization (speed vs quality, cost vs reliability)
- Prioritization under constraints
- Decision systems with measurable objectives
- Budget-aware model routing
- Ad ranking and recommendation ranking

## Trade-offs

- Utility design is hard
- Wrong metrics produce wrong behavior
- Requires good telemetry and monitoring

## Real-world company and service examples

- OpenAI / Anthropic model routing in production stacks - choose model tier per request based on cost, latency, and quality targets.  
  Approximate API examples: OpenAI often from **$0.20/$1.25** up to **$2.50/$15** per 1M tokens; Anthropic often from **$1/$5** to **$3/$15** for common tiers.
- Cloud contact center AI - route conversations by value/risk (self-serve vs human escalation).  
  Approximate pricing: usually seat + usage bundles, frequently **$30-$150+ per seat/month** depending on platform.
- Commerce recommendation systems - maximize conversion while controlling margin and return risk.  
  Cost profile: usually infrastructure + model usage; highly variable by traffic.

## Utility dimensions you should track

- Response quality score
- Time-to-complete
- Total cost per successful task
- Human escalation rate
- Error / rollback rate

## Common failure modes

- Optimizing one metric while damaging another (for example, lowest cost but poor user outcomes).
- Utility gaming (agent learns shortcuts that inflate score but hurt business value).
- Missing penalties for compliance or brand risk.

## Implementation checklist

- Start with 3-5 utility dimensions only.
- Normalize scores to comparable ranges.
- Add hard constraints before scoring (policy, legal, safety).
- Recalibrate weights monthly with real production data.
