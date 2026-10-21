# PaperLens

**A paper reading assistant with summary and context-aware term explanation.**

Computer B group project. This repository currently contains the scaffold only; module implementations will be added by the team.

## Team

| Member | Module |
|---|---|
| A | PDF parsing, cleaning, page mapping, quality gate |
| B | LLM client, prompts, summary, citation checks |
| C | Term context, retrieval, explanation, optional search |
| D | Flask UI, selection, integration, demo |

## Repository layout

```text
app.py                 Flask entry point
paperlens/
  pdf/                 PDF parsing and quality gate
  ai/                  LLM client, summary, schemas
  terms/               Context, retrieval, explanation, search
  web/                 Routes, templates, static files
  common/              Shared models, errors, cache
prompts/               Versioned prompt files
tests/                 Unit and integration tests
docs/                  Proposal, architecture, API, data model, AI log
data/                  Local uploads and cache (ignored by Git)
.github/               CI, PR template, issue template
```

## Status

- [ ] Dependencies added to `requirements.txt`
- [ ] Shared interfaces defined in `docs/data-model.md`
- [ ] PDF parsing implemented
- [ ] Summary pipeline implemented
- [ ] Term explanation implemented
- [ ] Flask UI and selection implemented
- [ ] Tests and demo completed

## AI usage

AI-assisted work is recorded in [`docs/ai-usage.md`](docs/ai-usage.md). Every AI-generated change must be reviewed and tested by the module owner before merging.
