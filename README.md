# awesome-jev-family

A curated awesome list of decision models that are **similar to, alternatives to, or reimplementations of** [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — TypeSafe AI's System One model for typed decisions. Where [awesome-jev](https://github.com/yibie/awesome-jev) tracks who is *building with* Jev, this list tracks the **models themselves**: open replicas, ports to new runtimes, community SDKs, and the benchmarks that measure them.

This README is the homepage aggregate of the current category files, so the latest accepted entries are visible here without drilling into subpages.

A System One decision model is not a chat model. It takes unstructured state plus a **typed question** and returns a **typed decision** — a `choice`, a `score`, or a `noul` (probability of true) — each with a confidence, usually in a single forward pass with no generated text. Models like [Laya](https://github.com/NandhaKishorM/laya), [kev](https://github.com/jaredpalmer/kev), and [laya-mlx](https://github.com/mizorewww/laya-mlx) chase the same shape from different angles: a multilingual RLCD-trained encoder, a trainable Qwen3.5 family, a native Apple Silicon port. This list is a high-signal field guide to that family.

> [!WARNING]
> **A listing is not an endorsement.** This project applies *inclusion* rules only — public, citable, and genuinely a Jev-like decision model, port, SDK, or measurement thereof, with a one-sentence summary. It does **not** review model quality, calibration honesty, license fitness, or whether a project runs at all. Reported numbers (latency, accuracy, ECE) are quoted from each project's own page and are **not independently verified here**.

## Why this list

Replicas and ports of the System One shape are scattered across launch threads, Hugging Face collections, and one-off benchmark gists. This list answers two questions quickly:

- Which Jev-like models can I actually download, run, or point an SDK at today?
- How do they compare on speed, calibration, and license?

## Inclusion criteria

An entry should meet all of the following:

- The source is public and citable.
- It is a **decision model in the System One family** — a from-scratch replica, a fine-tune of an open base into the typed-decision shape, a runtime/port that serves such a model, an SDK/adapter that speaks the typed-decision API, or an independent benchmark/calibration study of one.
- The source shows the typed-decision shape: a typed question (`choice` / `score` / `noul`) answered with a probability, not a generic classifier or an LLM prompt-and-parse wrapper with no decision-model involvement.
- The summary explains what it is, how it works, and its value in one sentence.

We do **not** include:

- Applications that merely *use* a decision model — those belong in [awesome-jev](https://github.com/yibie/awesome-jev).
- Generic classifiers, routers, or NLI models with no typed-decision interface.
- Pure hype threads with no working artifact, weights, or reproducible result.
- Sources that are private, inaccessible, or too vague to classify.

## Curation is not endorsement

Inclusion means one thing: the entry satisfies the rules above. Many entries here are **unproven** — a replica published days after the architecture write-up, a port with a small parity-test fixture, a benchmark run once on one GPU. Treat them as leads, not validated tools. Before adopting one, check it yourself:

| Check | Why it matters |
| --- | --- |
| Are the weights actually downloadable and licensed? | Some "open" models ship a README and a promise. Confirm the checkpoint, its license, and its base model. |
| Is there a runnable check? | A test, an example with expected output, or a public demo. No check means no evidence it works. |
| Do the numbers have a source? | Latency, accuracy, and ECE figures should trace to the linked page. We quote them; we do not re-measure them. |
| Is the calibration fitted in-distribution? | Most of these models fit a temperature on their own dev set. Confidence can still be dishonest on your data. |

Found something wrong? Open an issue or a pull request — **removal is as valid a contribution as addition.** See [CONTRIBUTING.md](CONTRIBUTING.md).

## Current coverage

<!-- BEGIN:COVERAGE -->
**78 entries across 5 categories.**

- [Open Alternatives & Replicas](#open-alternatives-replicas) — 21 entries
- [Ports & Local Runtimes](#ports-local-runtimes) — 7 entries
- [SDKs & Integrations](#sdks-integrations) — 23 entries
- [Benchmarks & Calibration](#benchmarks-calibration) — 14 entries
- [Related Practices & Discussions](#related-practices-discussions) — 13 entries
<!-- END:COVERAGE -->

Each entry lives in exactly one category, chosen by what the project *is* (a model, a runtime, an SDK, or a study) rather than what it can do.

## Full list

<!-- BEGIN:FULL_LIST -->
### Open Alternatives & Replicas

Source file: [`categories/open-alternatives-replicas.md`](categories/open-alternatives-replicas.md)

- [Laya](https://github.com/NandhaKishorM/laya) - Open alternative: multilingual non-autoregressive System One engine that answers `choice`, `score`, and `noul` questions over 100+ languages in a single ~33 ms forward pass, trained with RLCD proper-scoring-rule rewards, shipping three Apache-2.0 checkpoints (`laya` 421M English, `laya-multilingual` 322M, `laya-typed-decisions` 421M) and a Router that picks the checkpoint per request from sub-millisecond script detection.
- [kev](https://github.com/jaredpalmer/kev) - Trainable replica: family of small Jev-like decision models (0.8B, 4B, 9B) built on Qwen3.5 LoRA adapters plus a pointer head, exposing the same `POST /v1/systemone` API so TypeSafe's SDK points at a local server, with frozen eval suites, calibrated temperatures, and a fine-tune-your-own recipe on CUDA, ROCm, or Apple Silicon.
- [Nimble](https://github.com/bespokelabsai/nimble) - Open recipe + model: Bespoke Labs' data/model/recipe for an open decision model — a Qwen3.5-9B LoRA fine-tune (`Bespoke-Nimble-9B`) trained with contrastive data curation (flip one fact so the label flips) on the answer tokens only, scoring candidate logits with no generated JSON, and reporting 90.1% reference-label agreement on 324 held-out examples against Jev's 93.2% and the base model's 66.4%; not distilled from Jev.
- [SemIf](https://github.com/TheoLeeCJ/SemIf) - Open interface (formerly OpenJev): reproduces the typed-decision *interface pattern* on frozen open models (Qwen3.5-4B and up) by reading declared option logits in one forward pass with no answer token, runs in the browser via WebGPU and on CUDA/MLX/MPS/llama.cpp, and commits row-level fixtures, prompts, and calibration; reports 0.845 modal agreement with Jev on a 102-row public subset (Jev 0.883).
- [decider](https://github.com/Mapika/decider) - Open models: reproduces the System One shape with a Qwen3.5-2B fine-tune that emits typed decisions with calibrated probabilities in one pass.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - Open replica: a 0.6B parallel decision model that returns full probability distributions with no output-token decoding, shipped with its training pipeline, weights, and dataset.
- [openjev](https://github.com/zhihz/openjev) - Open research: independent local preview that answers bilingual probability questions from context, questions, and candidate answers, inspired by the System One shape.
- [von](https://github.com/wfzyx/von) - Open alternative: a 395M non-autoregressive System One model that answers typed questions with calibrated probabilities in under 15 ms, positioned as a local drop-in replacement.
- [Luce](https://github.com/scienthoon/luce) - Open recipe: describe the decision task in a sentence, an LLM teacher writes the training data, and a LoRA plus decision head on Qwen3-4B-Base answers choice/score/boolean questions with calibrated probabilities in one forward pass, trainable on a 12 GB card with reported accuracy and ECE against Jev on identical test items.
- [OpenDecision](https://github.com/deepanwadhwa/OpenDecision) - Open alternative: a local semantic decision engine that describes itself as the open-source equivalent, answering `Choice`, `Noul`, and `Score` questions from structured state and documents without a hosted call.
- [poorjev](https://github.com/rupeshpoojary9/poorjev) - Local reproduction: implements the typed `Choice`/`Score`/`Noul` interface on commodity zero-shot NLI models and makes the confidence honest with temperature scaling and conformal abstention, shipping a reproducible offline calibration eval (ECE 0.170 to 0.071, cross-validated).
- [minojev](https://github.com/zeredy879/minojev) - Open replica: a 547k-parameter model that answers runtime-defined `Choice` (2-255 candidates), `Boolean`, and `Score` questions with dev-calibrated distributions in one forward pass and zero output tokens, trained from scratch on CPU with committed datasets, predictions, and ECE results.
- [mini-jev](https://github.com/r-ms/mini-jev) - Local reproduction: implements the typed-decision interface on top of a local LLM.
- [jevlike](https://github.com/vinnylarouge/jevlike) - Training library: build a small model that chooses among a changing list of text options and returns one probability per option in a single pass.
- [jevbetter](https://github.com/olanotolu/jevbetter) - Improved scorer: a stronger one-pass scorer over a variable list of text options, using a hashed n-gram encoder, rival-aware attention, and gated heads.
- [CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms) - Specialist decision model: a 706,048-parameter, 2.8 MB option scorer that rates FILL / CHECK / CLICK / SKIP for each form field in one parallel pass, reporting 99.7% on its own form-filling eval — a specialist on home turf rather than a general win.
- [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) - Open decision engine: a calibrated 151M non-autoregressive model that reports beating both TypeSafe Jev and Laya on typed-decision benchmarks, shipped with its own test suite.
- [JevForge](https://github.com/zwliJay/jev-forge) - Open research: an end-to-end stack for auditable data construction, Qwen3.5-0.8B training, fixed Mind2Web and OOD evaluation, local serving, and a preliminary RLCD baseline.
- [Parallel Constrained Decoding (Qwen2.5-1B-RLCD)](https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding) - Open research: RLCD-trained Qwen2.5-1B demo exploring open-source parallel constrained decoding as an alternative.
- [PlayJev](https://github.com/OmniJev/PlayJev) - Vision decisions: open 0.8B vision-language model that reads one 448 px game frame and returns a probability over the moves the game lists in a single forward pass with no generated text, across ten browser games.
- [Visual-JEV](https://github.com/jiangxiluning/Visual-Jev) - Multimodal replica: a native multimodal System One model based on Qwen3.5-4B that supports direct image input without requiring modality conversion.

### Ports & Local Runtimes

Source file: [`categories/ports-runtimes.md`](categories/ports-runtimes.md)

- [laya-mlx](https://github.com/mizorewww/laya-mlx) - Local runtime: independent MLX port of the Laya checkpoints that runs typed decisions natively on Apple Silicon — 13.4 ms median end-to-end per short English decision, 7.4 ms with the multilingual checkpoint, and zero output tokens, with no PyTorch, Transformers runtime, or cloud API; ships pre-converted FP16 checkpoints and reports 63/63 selected-answer parity with upstream in both FP32 and FP16.
- [jev-local](https://github.com/us/jev-local) - Local reproduction: `POST /v1/systemone` server answering typed `Choice`/`Score`/`Noul` questions with confidence from open weights, verified as an official-SDK drop-in with temperature-fit calibration.
- [LitJev](https://github.com/zhengxuyu/litjev) - Local reproduction: turns any Qwen model into a fast decision model, serving the same `/v1/systemone` schema (Choice, Score, Noul) with no training and no generated answer text.
- [FastJev](https://github.com/chengyongru/fastjev) - Local runtime: self-hosted Python SDK and System One-compatible API for runtime-defined `Choice`, `Boolean`, and `Score` decisions on pinned open models across Torch, vLLM, MLX, llama.cpp, and WebGPU, with committed row-level benchmarks and checksums.
- [jeff](https://github.com/logan-markewich/jeff) - Self-hosted runtime: self-hosted drop-in replacement powered by GliFormer, exposing native Choice, Score, and Noul decision endpoints without cloud API dependencies.
- [Jev-compatible public API](https://x.com/ekzhang1/status/2100651678110515383) - Open research: a public System One-shaped API backed by an open Qwen3.6-35B-A3B model so anyone can try the typed-decision interface.
- [jevlike-esp32](https://github.com/david-cermak/jevlike-esp32) - Edge deployment: exports a jevlike scorer as ESP32 firmware with a C scorer and a host-side check, putting one-pass decisions on a microcontroller.

### SDKs & Integrations

Source file: [`categories/sdks-integrations.md`](categories/sdks-integrations.md)

- [zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai) - Scala ecosystem: ZIO client for TypeSafe AI with a typed DSL over System One decisions.
- [TypeSafe AI Swift SDK](https://github.com/alterhq/typesafe-sdk-swift) - Swift ecosystem: dependency-free Swift 6 client for Choice, Score, and Noul questions with strict concurrency, configurable authentication and retries, and offline transport tests.
- [laravel-typesafe-jev](https://github.com/Butochnikov/laravel-typesafe-jev) - PHP ecosystem: unofficial Laravel integration with typed responses, async requests, scoped dependency injection, and testing fakes.
- [jevclient](https://pypi.org/project/jevclient/) - Python ecosystem: async client published on PyPI.
- [jev-go](https://github.com/Stumble/jev-go) - Go ecosystem: community Go SDK.
- [jev (Elixir)](https://github.com/dannote/jev) - Elixir ecosystem: GenServer client that replies with the model's answer so callers can pattern match on it directly.
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) - Ruby ecosystem: client for decision models so Ruby applications can put typed questions directly to the model.
- [s1_ruby](https://github.com/innocentdiaz/s1_ruby) - Ruby ecosystem: makes System One measurement, and the collapse that follows it, a Ruby primitive, with a TypeSafe provider behind its own spec suite.
- [hunch](https://github.com/carldaws/hunch) - Ruby ecosystem: turns judgment calls into control flow — `if Hunch.likely?("fraudulent", given: order)` reads like plain Ruby but branches on a typed answer, with `pick` for Choice, `rate` for Score, and graded predicates.
- [kojev](https://github.com/ItisNoMatter/kojev) - Kotlin ecosystem: Kotlin Multiplatform (JVM, Android, iOS) client that answers Choice and Score questions as the caller's own enums, with one typed way to read answers, no default thresholds, and offline MockEngine tests.
- [jev-spring-boot-starter](https://github.com/danvega/jev-spring-boot-starter) - Java ecosystem: Spring Boot 4 starter that puts the model behind Spring MVC and RestClient.
- [huncho](https://github.com/edgardcham/huncho) - TypeScript ecosystem: dependency-free SDK that turns `Noul`, `Choice`, and `Score` answers into named decisions with enter/exit thresholds (hysteresis), nested decision trees settled in one call, a JSONL journal, and Brier/reliability calibration.
- [discern](https://github.com/doeixd/discern) - TypeScript ecosystem: Effect library where a `Choice`, `Noul`, or `Score` answer becomes a typed branch under caller-supplied thresholds, anything below them takes an `Uncertain` case the compiler forces you to handle.
- [ask-jev](https://github.com/logicrw/ask-jev) - Python ecosystem: zero-dependency CLI that routes small semantic judgments — Choice, Noul, Score, batch questions, and verbatim passage extraction — for AI agents and CLI pipelines.
- [jev-cli](https://github.com/tumf/jev-cli) - Developer tooling: small dependency-free CLI.
- [jevkit](https://github.com/ariel-frischer/jevkit) - Developer tooling: Rust CLI that validates `Choice`/`Score`/`Noul` question sets with 13 offline lint rules before any call, then sends the canonical wire payload and prints parsed, confidence-bearing JSON answers.
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) - Python ecosystem: TypeSafe AI's official open-source drop-in adapter for running and benchmarking System One decision evaluations across OpenAI- and Anthropic-compatible LLM APIs.
- [neurolink](https://github.com/juspay/neurolink) - Provider abstraction: Juspay's TypeScript interface over forty AI providers, with `decide` as a first-class inference type alongside generate and stream.
- [sqlite-jev](https://github.com/mgaitan/sqlite-jev) - SQLite ecosystem: loadable C extension and Python package that expose Noul, Choice, and Score judgments as SQL functions and batched virtual-table queries.
- [duckdb-jev](https://github.com/prasanthj/duckdb-jev) - DuckDB ecosystem: native extension that applies Noul, Choice, Score, and multi-question decisions directly to structured SQL rows.
- [jevql](https://github.com/kylemclaren/jevql) - Data tooling: psql-shaped CLI and Go/TypeScript/Python SDKs that run plain SQL on vanilla Postgres and then ask Noul, Choice, or Score questions about each surviving row.
- [decide-mcp](https://github.com/dakdevs/decide-mcp) - MCP ecosystem: configurable decision server with percentage scores and bias-profile routing.
- [jev-mcp (blakestone-x)](https://github.com/blakestone-x/jev-mcp) - MCP ecosystem: MCP server exposing classify, score, check, match, and screen as tools for any agent, with confidence on every answer.

### Benchmarks & Calibration

Source file: [`categories/benchmarks-calibration.md`](categories/benchmarks-calibration.md)

- [Five open Jev replicas worth trying](https://x.com/xiaomovps/status/2100923960493818177) - Roundup (Chinese): compares Laya 421M, Decider-2B, NanoJev 0.6B, Reflex, and System-One 4B as the most promising open decision models, two of which are Mac-friendly.
- [jevcal](https://github.com/abhixhek/jevcal) - Model evaluation: fits a per-question confidence threshold to a target accuracy on your own labeled data, verifies it on a held-out split, reports how much traffic still has to escalate to an LLM, and fails CI when a model update breaks the locked thresholds.
- [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) - Model evaluation: independent calibration test on 900 rule-generated support tickets plus three public benchmarks, publishing every raw response, ECE against a simulated noise floor, temperature refit, and the per-type sign of miscalibration.
- [jev-acento](https://github.com/marcosmartinez/jev-acento) - Language evaluation: pre-registered paired audit on Spanish over 3,200 human-labelled items, finding a Spanish `state` costs accuracy and roughly doubles ECE on XNLI and PAWS-X, shipping a CLI to rerun the same comparison on your own labelled data.
- [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) - Model evaluation: measures whether a SQL ORDER BY over a decision probability is defensible under a pre-registered gate, and shows a DuckDB extension's default row-batching fails the ranking gate that one row per request passes.
- [Jevals.com](https://jevals.com/) - Model evaluation: independent leaderboard that asks Jev and six LLMs the same Noul, Choice, and Score questions and grades every answer against human labels (PubMedQA, Banking77, HelpSteer2), publishing every per-decision probability as CC BY 4.0 data.
- [ASSAY-001](https://github.com/jourdanlabs/assay-001) - Independent pre-registered check of calibration and type safety on Banking77 / CLINC150, with a split verdict and full logs.
- [jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval) - Third-party check: compares a decision model against GPT-4o-mini and Claude Sonnet 4.5 under identical conditions on the same judgment task.
- [jev-test](https://github.com/souvikr/jev-test) - Model benchmarking: reproducible test harness evaluating Noul, Choice, and Score decisions via OpenRouter's Decisions API, comparing latency and accuracy against LLM prompt-and-parse baselines.
- [pytest-jev](https://github.com/allebee/pytest-jev) - LLM app testing: a pytest plugin that asks one Noul per plain-English claim about a reply and adds Choice and Score checks, matching a Claude verdict much faster and cheaper on its example tests.
- [Jev Playground](https://github.com/hegargarcia/jev-playground) - Model evaluation: benchmarks a decision model against Luna, Haiku, and Gemini at choosing validated legal moves in explicit-state games, scoring decision quality and consistency.
- [decision-model-benchmark](https://github.com/nibzard/decision-model-benchmark) - Model benchmarking: an independent decision-model benchmark whose published p50 latency figures are cited across the family's comparison tables.
- [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) - Model benchmarking: a third-party benchmark suite whose measured latency numbers are reused as the reference point in several cross-model comparisons.
- [Can Jev Be a Better Agent Evaluator?](https://www.langchain.com/blog/jev-agent-evals-langsmith) - Agent evaluation: LangChain compares a decision model against LLM judges on accuracy, repeatability, latency, and cost, concluding the decision model is the cheaper and more consistent judge for online evals.

### Related Practices & Discussions

Source file: [`categories/related-discussions.md`](categories/related-discussions.md)

- [Jev's Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked) - Technical analysis: inferred the internals from roughly 10,000 API calls, concluding the model keeps LLM knowledge but removes token generation entirely — the write-up several replicas cite as their design basis.
- [It is the inference technique, not the training](https://x.com/anderslie/status/2100388704644919662) - X: argues the speed comes from parallel decoding rather than model training, and that an inference engine can expose a System One-like API over any open-weight model.
- [MLP on Qwen 4B mimicking Jev](https://x.com/justALEXWORTEGA/status/2100341039986798930) - X: builder reports that a small MLP trained on top of Qwen 4B already reproduces the decision behaviour.
- [Running a local Typesafe Jev](https://x.com/wmoto_ai/status/2100454049359577516) - X (Japanese): attempt at running a decision model locally, with speed noted as still improvable.
- [Arbitrary classification as a type-safe primitive](https://x.com/cocktailpeanut/status/2100277062309179521) - X: argues the real novelty is not classification but that the model makes arbitrary classification a runtime-defined, type-safe programmable primitive.
- [I reviewed 287 open-source Jev projects](https://reddit.com/r/LLMDevs/comments/1wko2e5/i_reviewed_287_opensource_jev_projects_here_are/) - Reddit: a reviewer works through 287 repositories and narrows them to 20 that actually explain the model, a useful counterweight to star-count browsing.
- [Introducing CUA-S1](https://x.com/trycua/status/2101014004927729737) - X: Cua open-sources a family of small, specialised System One models for computer use, starting with form filling and asking what the next specialist should learn.
- [One 50 ms pass versus 23 turns](https://x.com/be_arsh/status/2101026864341164110) - X: the sharpest framing of the specialist case — a 706K-parameter model fills a whole form in one 50 ms pass, while an LLM agent needs 23 turns and 39.6 seconds for the same form.
- [Ask HN: What do you think of Noul, a new decision primitive](https://news.ycombinator.com/item?id=49760225) - Hacker News: a proposal to treat `Noul` — the probability-of-true answer type — as a general software primitive rather than tied to one model.
- [TypeSafe AI's Jev Is Not an LLM - and That May Be the Point](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/) - News analysis: treats the model's refusal to generate text as the feature rather than a limitation.
- [WTF is Jev, ELI5](https://x.com/mvanhorn/status/2100761338918363550) - X: frames the shape as "AI multiple choice, not AI essay writing," one of the clearer plain-language explanations.
- [A deep dive into Jev](https://flaviocopes.com/jev/) - Blog: a veteran technical writer's walkthrough of the System One idea, useful as the explanation to hand someone who has only seen LLM marketing.
- [Awesome TypeSafe Jev](https://github.com/AbdelStark/awesome-typesafe-jev) - Curated list: a source-backed field guide with SDKs and live demos, one of the larger community indexes.
<!-- END:FULL_LIST -->

## Submission format

Use exactly one line per entry:

```
- [Name](URL) - Category: one-sentence description of what it is and how it works.
```

## How to contribute

1. Pick the category that matches what the project **is**: a model, a runtime/port, an SDK, a benchmark, or a discussion.
2. Add a single-line entry in the required format to the **category file**, not directly to the README aggregate.
3. Run `python scripts/build_readme.py` to regenerate the coverage counts and full list.
4. Keep the summary concrete and scannable, and quote any numbers from the source.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT
