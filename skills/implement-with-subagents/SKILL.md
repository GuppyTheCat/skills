---
name: implement-with-subagents
description: >-
  Execute a written implementation plan by dispatching one subagent per task.
  Subagents inherit the session model unless the user assigns another model
  or models. Use when the user says implement with subagents, same model,
  inherit model, inherited model, or names a model for subagents, or runs
  /implement-with-subagents.
---

# Implement with subagents

Read and follow the `subagent-driven-development` skill for the plan the user attached or named. That skill owns task briefs, reviews, the progress ledger, and commits.

## Model

The default `model` for every subagent is `inherit`: implementer, reviewer, fixer, and any subagent a task spawns.

When the user assigns one model to subagents, map that name to a slug in the session's available subagent models and use it on every dispatch.

When the user assigns different models to different roles or tasks, use each assignment only on the dispatches they named. Every dispatch they left unnamed stays `inherit`.

"Same model", "inherit model", and "inherited model" mean `inherit`.

## Done

Every task in the plan is complete under `subagent-driven-development`, and every dispatch in this run used the model from the Model section.
