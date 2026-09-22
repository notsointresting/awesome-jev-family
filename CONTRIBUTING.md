# Contributing

Thanks for helping keep this list accurate. This project is a **field guide to Jev-like / System One decision models** — the models themselves, their ports and runtimes, the SDKs that speak their API, and the studies that measure them. It is not a list of applications built on top of a decision model; those belong in [awesome-jev](https://github.com/yibie/awesome-jev).

## What belongs here

An entry must meet **all** of the following:

- The source is public and citable (a repo, package page, Hugging Face model, or a written analysis).
- It is a **decision model in the System One family**, meaning one of:
  - a **from-scratch replica** or open model with the typed-decision shape,
  - a **fine-tune** of an open base into that shape,
  - a **runtime / port** that serves such a model on new hardware or behind a compatible API,
  - an **SDK / adapter** that speaks the typed-decision API,
  - an **independent benchmark or calibration study** of one or more such models,
  - or a **substantive discussion / analysis** of the model family.
- The typed-decision shape is visible: a typed question (`choice` / `score` / `noul`) answered with a probability — not a generic classifier, router, or LLM prompt-and-parse wrapper with no decision-model involvement.
- The one-sentence summary says what it is, how it works, and its value.

## What does not belong here

- Applications that merely *use* a decision model to do something (route tickets, moderate chat, drive a browser). Submit those to [awesome-jev](https://github.com/yibie/awesome-jev).
- Generic zero-shot classifiers or NLI models with no typed-decision interface.
- Hype threads with no working artifact, weights, or reproducible result.
- Private, inaccessible, or unclassifiable sources.

## Inclusion is not endorsement

Inclusion means only that the entry satisfies the rules above. We do **not** verify model quality, calibration honesty, license fitness, or that anything runs. Reported numbers (latency, accuracy, ECE) are **quoted from the source and not re-measured here**. Many entries are unproven — treat them as leads. Read the [Curation is not endorsement](README.md#curation-is-not-endorsement) checklist before adopting one.

**Removal is as valid a contribution as addition.** If an entry is broken, misclassified, or misrepresents its numbers, open an issue or PR.

## How to submit

1. Pick the **one** category that matches what the project *is*, not what it can do:
   - `categories/open-alternatives-replicas.md` — a new model (replica, fine-tune, from-scratch).
   - `categories/ports-runtimes.md` — a runtime that serves an existing checkpoint (MLX, GliFormer, self-hosted server, edge export).
   - `categories/sdks-integrations.md` — a client library, language binding, or framework/DB adapter.
   - `categories/benchmarks-calibration.md` — an independent evaluation or calibration study.
   - `categories/related-discussions.md` — an analysis, write-up, or notable thread about the family.
2. Add a single line to that category file, in the required format:

   ```
   - [Name](URL) - Category: one-sentence description of what it is and how it works.
   ```

   Keep it to one sentence. Quote any numbers ("13.4 ms median", "0.081 ECE") from the source and let the source carry them — do not invent or round beyond what the page says.
3. Regenerate the README aggregate:

   ```
   python scripts/build_readme.py
   ```

   This rebuilds the coverage counts and the full list between the `<!-- BEGIN:... -->` markers. Do not hand-edit those blocks.
4. Open a pull request. Keep one entry per PR when practical; it makes review and removal easier.

## Style

- One line per entry. The description is a single scannable sentence.
- Lead with the domain or kind (e.g. `Open alternative:`, `Local runtime:`, `Python ecosystem:`) so the list skims well.
- Prefer the canonical source (the model's own repo or model card) over a mirror or aggregator.
- Alphabetical order is not required; group related entries where it reads better.

## A note on bulk submissions

Several repositories published together by one author — sharing a scaffold and a thin commit history — can satisfy every rule and still be unproven. Volume is not evidence of quality. Such entries are welcome as *leads*, but the summary should be honest about what exists (weights? a runnable check? a sourced number?) rather than restating a promise.
