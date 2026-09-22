# SDKs & Integrations

Client libraries, language bindings, and framework adapters that let an application call a Jev-like / System One decision model — including community SDKs that speak the same typed-decision API regardless of which model or gateway is behind it. These wrap a model; they do not implement one.

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
