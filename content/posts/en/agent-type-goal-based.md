---
lang: en
title: AI Agent Type - Goal-Based Agents
slug: agent-type-goal-based
date: 2026-04-10
section: agent-type
category: Agent Types
tags: [OpenAI, API, ChatGPT]
summary: Agents that evaluate actions based on whether they move toward a defined goal.
status: published
---

# Goal-Based Agents

Goal-based agents do not just react. They choose actions that help reach a target state.

This is the "planner" mindset: define a goal, evaluate possible next steps, and execute the best path.

## How it works (architecture)

1. Define goal and constraints.
2. Generate plan candidates.
3. Select next action toward goal.
4. Execute and observe outcome.
5. Re-plan until goal is reached or aborted.

## Typical examples of goals

- "Create a market brief in 30 minutes with sources."
- "Automate invoice matching with less than 1% error."
- "Book meetings with qualified leads this week."

## Best use cases

- Task completion workflows
- Planning across multiple steps
- Structured assistant behavior
- Research and synthesis pipelines
- Agentic coding and refactor workflows

## Trade-offs

- Needs clear goal definition
- Planning cost can grow quickly
- Poor goals create confidently wrong behavior

## Real-world company and service examples

- OpenAI - goal-driven assistants built with the Responses API + tools (web search, files, code execution, external APIs).  
  Approximate API range: **$0.20/$1.25** to **$2.50/$15** per 1M input/output tokens for many standard model tiers.
- Anthropic Claude - planning workflows with tool use for research, drafting, and operations support.  
  Approximate API range: often **$1/$5** to **$3/$15** per 1M input/output tokens for common tiers.
- Microsoft Copilot / GitHub Copilot style task completion flows (goal = "produce result, not just answer").  
  Approximate pricing: commonly **$10-$39 per user/month** depending on product tier.

## Practical pricing references (consumer + API)

- ChatGPT Plus: about **$20/month** (web app subscription; API billed separately).
- Claude Pro: about **$20/month** monthly, or around **$17/month** annual equivalent in some regions.
- API cost can be lower than subscriptions for light usage, but higher for heavy automated workloads.

## How to make goal-based agents reliable

- Write explicit success criteria ("done means X").
- Enforce budget caps (tokens, time, tool calls).
- Add checkpoints after every major step.
- Require citations/evidence for factual tasks.
- Add human approval for high-risk actions.

## When to avoid

Avoid pure goal-based setups when:
- You need strict optimization under multiple conflicting objectives (use utility-based).
- Environment changes continuously and model must adapt from feedback (add learning components).
