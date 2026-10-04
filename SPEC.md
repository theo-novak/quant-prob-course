# SPEC.md — The Probability Gap (Bucket 0 frozen: Oct 1, 2026)

## Identity
- **Product:** *The Probability Gap: Quant Interview Foundations from Zero*
- **What:** tutorial-style, learn-from-scratch probability course for quant interview prep
- **Artifacts:** ~100 pp LaTeX PDF (7 chapters + drill appendix) · 7 Jupyter notebooks · pytest verification suite (~60–70 tests, seeded, MC tolerance-aware)
- **Moat:** every worked problem solved two ways — analytic derivation + Monte Carlo verification. Never cut.

## Goal & success metric (from kickoff interview, Oct 1)
- **Core decision this drives:** the next-career-chapter question — evidence of a complete ship-and-sell loop
- **Success:** ≥$20 net from ≥2 non-friend buyers by **Dec 30, 2026**
- **Constraints:** <$20 total spend · 5–8 h/wk in 25–45 min guilt-free sessions · cold start, no audience

## Verified decision log
| # | Decision | Date |
|---|---|---|
| 1 | Product: quant interview pack (over SC optimizer, trader journal, micro-API) | Oct 1 |
| 2 | Style: learn-from-scratch tutorial (over distilled reference) | Oct 1 |
| 3 | Repo: **private** — credentials never in chat; `gh auth login` device flow when remote is needed | Oct 1 |
| 4 | Lane: probability & EV foundations — nobody owns the "fundamentals taught for interviews" layer | Oct 1 |
| 5 | Outline as written: 7 chapters, cut rules, ~50 h budget | Oct 1 |
| 6 | Platform: **Payhip** (5% + processing, UK, VAT handled, Stripe payout) | Oct 1 |
| 7 | Name: **The Probability Gap: Quant Interview Foundations from Zero** | Oct 1 |
| 8 | **No free sample** — product-page preview only. The launch post itself carries the demonstration burden (HH vs HT worked in the post as pure value) | Oct 1 |
| 9 | Launch structure: **DEFERRED to Week-6 checkpoint (~Nov 12)** — early access Nov 8 @ $14 vs single full launch Dec 8 @ $19, decided on real progress data | Oct 1 |
| 10 | Prices: $19 full / $14 early access (if split) | Oct 1 |
| 11 | **Parked at Theo's request** after Ch1 draft (1.2); resume gate = Ch1 voice verdict; goal line unchanged; resume map in `STATUS.md` | Oct 4 |

## Anti-drift protocol
- Cut rules invoke in order, never renegotiated mid-slip: **A1** appendix → protocol sheet · **A2** Ch7 dissolves into Ch5/6 · **A3** 6→4 worked problems/chapter. **Never cut:** verification suite · two-ways-per-problem · Ch5.
- Any scope change requires explicit sign-off, logged in the table above.
- Every bucket checkpoint: restate the goal line, confirm no drift before proceeding.

## Legal line
Folk canon only (coins, dice, ruin — common property), original prose, original problem dressings. No verbatim Zhou/Crack content, no solution text.

## Distribution
One launch post (r/quant primary; honest-numbers framing), LinkedIn + theonovak.com as support. No paid ads, no content calendar.

## Budget & schedule (~50 h total)
W1–2 Ch1–2 · W3 Ch3 · W4 Ch4 · W5–6 Ch5 · W7 Ch6 · W8 Ch7 + appendix · W9 verification polish + packaging · W10+ launch & measure. Buffer ~8 h.

## Repo layout (planned)
```
/projects/quant-prob-course/
  SPEC.md · OUTLINE.md
  /latex        main.tex, chapters/
  /notebooks    ch1.ipynb … ch7.ipynb
  /tests        conftest.py, test_ch1.py … test_ch7.py
  /tools        tracker generator, cover build
  /marketing    launch post draft, product page copy
```