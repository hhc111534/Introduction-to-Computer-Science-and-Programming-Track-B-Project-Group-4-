# PaperLens — Codex / AI Coding Instructions

## Project

PaperLens is a Flask web app for reading academic papers. A user uploads a text-layer PDF, receives a structured summary, selects a term, and receives an explanation grounded in the paper with optional web sources.

Stack: Python 3.10+, Flask, PyMuPDF, OpenAI-compatible API, Pydantic, pytest.

## Read first

Before changing code, read:

- `docs/architecture.md`
- `docs/data-model.md`
- `docs/TEAM_ROLES.md`
- `docs/FILE_GUIDE.md`
- `docs/codex.md` for Codex setup

## Module ownership

- `paperlens/pdf/` → A: PDF extraction, cleaning, page mapping, text-layer quality.
- `paperlens/ai/` → B: LLM client, prompts, summary, citation validation.
- `paperlens/terms/` → C: context, retrieval, term explanation, optional search.
- `paperlens/web/` and `app.py` → D: Flask routes, UI, selection, integration.
- `paperlens/common/` → shared; do not change without review.
- `docs/` → shared; proposal and interface docs need the relevant owner's review.

Work only in the module named in the task. Do not refactor other modules.

## Commands

- Install: `pip install -r requirements.txt -r requirements-dev.txt` (after dependencies are added).
- Test: `pytest -q`.
- Run: `python app.py` (after the Flask entry point is implemented).
- Check diff: `git diff`.

If a command is not implemented yet, do not invent dependencies or scripts. Ask the module owner.

## Working rules

- Create a feature branch; never commit directly to `main`.
- Keep changes small and scoped to one task.
- Add or update tests for every behavior change.
- Do not modify `paperlens/common/models.py`, `docs/data-model.md`, or `docs/api.md` without review.
- Do not commit `.env`, API keys, user PDFs, `data/uploads/`, `data/cache/`, or generated databases.
- Never print or expose secrets in logs, prompts, diffs, or test output.
- Record AI-assisted work in `docs/ai-usage.md`.
- Update `docs/logs-members.md` after a work session.
- Every generated change must be understandable and explainable by its owner.

## Codex-specific rules

- Use the project `.codex/config.toml`; do not change it without D's review.
- Use `workspace-write` and `on-request`; never use `--yolo` or `danger-full-access`.
- Network is off by default. Ask before enabling it.
- Before editing, summarize which files you will change and why.
- After editing, report changed files, tests run, and unresolved risks.
- Do not paste private papers, API keys, or personal data into the conversation.

## Code Review Rules

Flag these issues:

- Missing page citations in summaries or explanations.
- External URLs not returned by the search provider.
- API keys, tokens, or personal data in code, logs, or fixtures.
- Changes to shared interfaces without review.
- Tests that call real APIs instead of mocks.
- Claims that the paper does not support.
