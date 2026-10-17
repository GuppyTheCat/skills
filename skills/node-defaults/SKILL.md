---
name: node-defaults
description: >-
  Node defaults. Use when creating a project that is or might be Node or
  TypeScript, when the user asks to align a repo to those defaults, or when
  telegram-bots points here.
---

# Node defaults

Decisions for a new Node project. Versions and file contents come from each tool's official docs on the day you apply them.

## When it applies

- **New project.** The user is creating a project that is Node or TypeScript, or they said "new project" and have not named a runtime.
- **Align.** The user explicitly asked to align this repo to these defaults.

On any other task, keep the toolchain the repository already has. This skill is finished.

`telegram-bots` points here for a new bot project. The same two branches decide whether the stack changes.

## New project

When the user has not named a runtime, ask whether this is a Node program. Wait for the answer. A "no" ends this skill.

## Stack

Look each item up while applying it. Record the result in the project.

- **TypeScript.** Latest stable, the npm `latest` dist-tag. Use the `tsconfig` the current Node + TypeScript docs recommend for this kind of project.
- **Node.js.** Current LTS, from https://nodejs.org/en/about/releases. Record it where the current Node and pnpm docs say a project records its runtime.
- **pnpm.** The package manager. Follow https://pnpm.io/installation, including the `packageManager` field. The pnpm lockfile is the project's lockfile.
- **ESLint.** Follow https://eslint.org/docs/latest/use/getting-started, including the current TypeScript instructions.
- **Prettier.** Follow https://prettier.io/docs/install. Leave formatting to Prettier: use the current `eslint-config-prettier` setup so ESLint and Prettier do not both format.

Done when `pnpm install` succeeds and the TypeScript build succeeds.

## Docker

Ask once: do they need Docker and Docker Compose for this project? Skip the question when this conversation already answered it. Wait for the answer.

- **Yes.** Add a Dockerfile and a Compose file that run this application. Follow https://docs.docker.com/guides/nodejs/ for the file shape. That guide shows npm. Use pnpm in the image.
- **No.** Add no Docker files.

Done when the files match the answer.

## Align

Run **Stack** and **Docker** on the existing repository.

Done on the same criteria as those sections.
