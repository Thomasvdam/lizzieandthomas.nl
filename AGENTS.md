# Repository guide

This is a small static GitHub Pages site. Keep it simple: no framework, build step, package manager, or external animation dependency is needed. `index.html` contains the page, styles, and small interaction; `images/` contains the cat photos; `CNAME` sets the custom domain.

## Working conventions

- Preserve the playful character of the site and make changes work on narrow screens.
- Keep meaningful text and controls accessible. Decorative elements should be hidden from assistive technology, and motion should respect `prefers-reduced-motion`.
- Use relative paths for local assets so a local preview works.
- Preserve unrelated work.

## Validation

Run `./scripts/check` from the repository root. It checks local asset references, basic HTML structure, shell syntax, and Git whitespace. Preview the page in a browser at desktop and mobile widths and exercise the confetti button; static checks cannot verify the layout.

## Conversation workflow

This repository uses the personal `conversation-workflow` skill and `~/.local/bin/codex-workflow`. Project validation is `./scripts/check`. The shared setup is maintained in the [Thomasvdam/codex-workflow](https://github.com/Thomasvdam/codex-workflow) repository.

The primary agent owns branch management, commits, validation, and PR delivery. Delegated agents, when used, preserve unrelated work and do not run competing branch, commit, push, hook, or PR lifecycle operations.
