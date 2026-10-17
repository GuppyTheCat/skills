# skills

Personal agent skills.

Layout: `skills/<name>/SKILL.md`.

## Skills

- **node-defaults** — Node defaults. Use when creating a project that is or might be Node or TypeScript, when the user asks to align a repo to those defaults, or when telegram-bots points here.
- **telegram-bots** — Telegram bots. Use when creating a Telegram bot or a grammY bot.
- **russian-prose** — Natural Russian prose. Use when writing any Russian text in any repository: notes, replies, README, commits, PRs.
- **implement-with-subagents** — Execute a written implementation plan by dispatching one subagent per task. Subagents inherit the session model unless the user assigns another model or models. Use when the user says implement with subagents, same model, inherit model, inherited model, or names a model for subagents, or runs /implement-with-subagents.

## Install

All skills:

```bash
npx skills add GuppyTheCat/skills
```

One skill, project-local:

```bash
npx skills add GuppyTheCat/skills --skill <name>
```

On the author's machine, `~/.agents/skills/blackmage` links to `skills/` directly.
