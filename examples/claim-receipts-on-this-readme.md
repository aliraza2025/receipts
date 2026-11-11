# Example: claim-receipts run on this repo's own README

Before launch, an AI agent (Cursor) ran `claim-receipts` on the README of this repository, using the repo, the CI workflow, and the linked portfolio pages as the only sources. The output is below, lightly trimmed. The fixes it suggested were applied in the same commit that added this file.

## Claim receipts: README.md

| # | Claim (quoted) | Label | Receipt or gap | Suggested rewrite |
|---|---|---|---|---|
| 1 | "Six agent skills for Claude Code, Codex, and Cursor" | MEASURED-WITH-SCOPE | `skills/` has six folders. `install.sh` was tested into each agent's skills folder, and `npx skills add` was tested for Claude Code. Whether each agent triggers a skill automatically was not tested. | Keep, and add an install note: "Install tested for all three. How and when each agent picks up a skill varies." |
| 2 | "they are also fast at writing '97% reliable', 'users love it' ... with nothing behind it" | ASSUMPTION | An opinion about AI writing, framed as one. | Keep. |
| 3 | "In one 780-link YouTube batch, every job completed, but 759 of 780 results were flagged as low evidence." | SOURCED | [CrediClip AI product quality note](https://alirazaai.page/notes/crediclip-ai-product-quality) | Keep. |
| 4 | "A 100-video readiness benchmark showed a working queue but missing evidence, which moved the roadmap to ingestion." | SOURCED | Same note: queue reliability 97% (pass), insufficient evidence 97.8% (fail), effort redirected to ingestion. | Keep. |
| 5 | "a quoting tool built on 11,000+ service jobs" | SOURCED | [Estimator data plane note](https://alirazaai.page/notes/estimator-data-plane) | Keep. |
| 6 | "every claim has an entry on a Sources page" | UNSUPPORTED | The [Sources page](https://alirazaai.page/sources) lists primary sources by topic and asks readers to report unbacked claims. It does not have one entry per claim. | "my portfolio lists the primary sources behind what it says about my work on a Sources page, and asks readers to report anything unbacked" |
| 7 | "Broad libraries such as phuryn/pm-skills and deanpeters/Product-Manager-Skills cover the whole PM toolkit" | SOURCED | Both repositories describe themselves as broad PM skill collections. | Keep. |
| 8 | "CI runs it on every push." | SOURCED | `.github/workflows/validate.yml` triggers on `push` and `pull_request`. | Keep. |

**Summary:** 8 claims checked. 5 sourced, 1 needs scope, 1 assumption, 1 unsupported.

**What changed:** claim 6 was rewritten and an install note was added for claim 1. The one claim the README made about its own author was the one that overstated.
