---
name: telegram-bots
description: >-
  Telegram bots. Use when creating a Telegram bot or a grammY bot.
---

# Telegram bots

A new bot project follows `node-defaults` before the sections below. Adding a bot to an existing repository keeps that repository's toolchain.

## grammY

Use grammY. Install it from the current grammY Node getting-started.

Done when the bot process starts on that project's toolchain.

## Proxy

Every bot accepts an optional SOCKS proxy.

- Read the URL from `TELEGRAM_SOCKS_PROXY`.
- When the variable is unset or empty, connect directly and pass no proxy agent.
- When the value has no scheme, use it as a `socks5h` URL so DNS goes through the proxy.
- Install `socks-proxy-agent` and attach it as https://grammy.dev/advanced/proxy describes for Node, including the agent timeout and the `compress` note on that page.

Document the name in `.env.example`.

Done when an unset variable connects directly, and a value with no scheme is a `socks5h` URL.

## Allowlist

Tell the user that BotFather can restrict who uses the bot: **Restrict bot usage**, then **Allowed users**. With that on, only they and the users they select can interact with the bot.

Ask whether they also want that restriction in code. Wait for the answer.

- **No.** Add no allowlist.
- **Yes.** Read `ALLOWLIST_USER_IDS` from the environment: a comma-separated list of numeric Telegram user ids. Document the name in `.env.example`.
  - Missing or empty: exit with a non-zero status before the bot starts.
  - A sender id that is not in the list: ignore the update and send no message.

Done when a missing variable exits before startup, and a sender outside the list gets no reply.
