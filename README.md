# Receipts: evidence-first PM skills for AI agents

**Make product claims show their receipts.**

Six agent skills for Claude Code, Codex, and Cursor that make PRDs, metrics, experiment readouts, AI evaluations, and launch copy say where each claim comes from and what each number does not prove.

AI agents are fast at writing product docs. They are also fast at writing "97% reliable", "users love it", and "proven to increase conversion" with nothing behind it. Receipts adds the habit good PMs already have: before a claim ships, it has to point at something real.

## The skills

| Skill | Use it when | What it does |
|---|---|---|
| [`claim-receipts`](skills/claim-receipts/SKILL.md) | Before publishing any copy with numbers or outcomes | Labels every claim `SOURCED`, `MEASURED-WITH-SCOPE`, `ASSUMPTION`, or `UNSUPPORTED`, and rewrites the weak ones without inventing support |
| [`metric-receipts`](skills/metric-receipts/SKILL.md) | Defining success metrics or reporting results | Pairs each metric with the decision it informs and what it does not prove; flags proxy inflation |
| [`ai-eval-receipts`](skills/ai-eval-receipts/SKILL.md) | Shipping an LLM or AI feature | Readiness gates for completion, sufficiency, and agreement; abstention rules; the model's boundary in the workflow |
| [`experiment-receipts`](skills/experiment-receipts/SKILL.md) | Planning or reading out an A/B test | Decision-first plan, precise metric, sample size as an assumption, guardrails, privacy-scoped events, verified vs simulated |
| [`prd-receipts`](skills/prd-receipts/SKILL.md) | Turning interviews or requests into a PRD | Keeps observed, inferred, and assumed apart; every requirement points at evidence |
| [`plain-copy`](skills/plain-copy/SKILL.md) | Copy "sounds like ChatGPT" | Removes filler, em dashes, and inflated verbs without adding claims |

## Install

Clone, then copy the skills into your agent's skills folder:

```bash
git clone https://github.com/aliraza2025/receipts.git
cd receipts
./install.sh claude   # ~/.claude/skills
./install.sh codex    # ~/.codex/skills
./install.sh cursor   # ~/.cursor/skills
./install.sh all
```

Or install into one project only: `./install.sh cursor --project path/to/repo` (writes to `.cursor/skills/`, `.claude/skills/`, or `.agents/skills/` for Codex).

Then ask your agent things like:

- "Run claim-receipts on README.md"
- "Write a metric-receipts card for our activation metric"
- "Use ai-eval-receipts to plan the launch gates for the summarizer"
- "experiment-receipts: plan a test of guided vs single-page signup, baseline 40%"

## Before and after

> **Before:** "CrediClip analyzed 780 videos with 97% reliability."
>
> **After `claim-receipts`:** "In one 780-link YouTube batch, every job completed, but 759 of 780 results were flagged as low evidence."

The second sentence is less flattering and far more useful. It tells a reader, a hiring manager, or your own team exactly what the system did and where it still falls short.

## Where these come from

I'm [Ali Raza](https://alirazaai.page/), a Bay Area product manager and AI builder. Each skill is the written-down version of a method I used on real work:

- **ai-eval-receipts and metric-receipts** come from [CrediClip](https://alirazaai.page/crediclip), an AI credibility product for short-form video. A 100-video readiness benchmark showed a working queue but missing evidence, which moved the roadmap to ingestion. More in [What 780 completed video jobs taught me about AI product quality](https://alirazaai.page/notes/crediclip-ai-product-quality).
- **experiment-receipts** comes from [Raasta](https://alirazaai.page/notes/raasta-product-experiment), an intake experiment with a planning-only sample size, guardrails, and a narrow event contract.
- **prd-receipts** comes from gathering requirements with an owner and office staff for a [quoting tool built on 11,000+ service jobs](https://alirazaai.page/notes/estimator-data-plane).
- **claim-receipts** is how I run my own portfolio: every claim has an entry on a [Sources page](https://alirazaai.page/sources).

## How this differs from big PM skill libraries

Broad libraries such as [phuryn/pm-skills](https://github.com/phuryn/pm-skills) and [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) cover the whole PM toolkit, and they are great for that. Receipts does one narrow thing: it checks whether what your docs say is supported. It works alongside them.

## Validate

```bash
python3 scripts/validate.py
```

Checks frontmatter, name rules, description length, file size, and that no skill contains an em dash. CI runs it on every push.

## Contributing

Issues and pull requests are welcome, especially worked examples from real (non-confidential) projects. Every example must be either real and sourced, or clearly labeled as illustrative. That is the whole point of the repo.

## License

[MIT](LICENSE) · Built by [Ali Raza](https://alirazaai.page/) · [Work with me](https://alirazaai.page/services)
