# The Probability Gap — Course Outline (FROZEN with SPEC.md, Oct 1)

Title: *The Probability Gap: Quant Interview Foundations from Zero* (locked Oct 1)
Platform: Payhip (5%, locked Oct 1) · Price: $19 full / $14 early access (launch split: Week-6 decision)
Free teaser: none — preview only; launch post carries the demo burden.

## Product shape
- **PDF course** (~95–115 pp, LaTeX): 7 chapters + appendix
- **7 Jupyter notebooks**: derivations, plots, Monte Carlo confirmations
- **pytest verification suite** (~60–70 tests): every analytic answer checked against simulation; exact combinatorial checks via `itertools`/`sympy` where closed-form exists; seeded fixtures; MC tolerance-aware asserts (error ~ 1/√n)
- **Drill appendix + printable tracker** (folded in from the old plan; first cut if behind)

Every worked problem solved **two ways**: analytic derivation + simulation. This is the moat; never cut.

## Chapters

### Ch1 — Counting from scratch (~12 pp · 1 notebook · ~10 tests)
Multiplication rule; permutations vs combinations (when to divide by k!); stars & bars; complement and symmetry counting.
Worked (4): committee with constraints · at-least-one-shared-birthday among n · hat-check/derangements (E arrives in Ch3, counting here) · two-dice-sum symmetry.
Probes: "what if order doesn't matter?", "when does complement counting win?"

### Ch2 — Conditional probability & Bayes (~14 pp · 1 notebook · ~12 tests)
Conditioning as re-scoping the sample space; law of total probability; Bayes; base rates; independence vs disjointness; the tree diagram as a thinking tool.
Worked (4): 100 coins / one two-headed / 10 heads (≈91.2%) · disease-test base-rate trap (~16.7%) · three-coin-types next-flip (5/6) · Monty Hall derived from scratch, not memorized.
Probes: "test applied twice?", "redraw the tree with biased priors."

### Ch3 — Expectation: the workhorse (~16 pp · 1 notebook · ~12 tests)
Random variables, discrete → continuous; linearity of E and the indicator trick; variance/covariance basics; tail-sum formula E[X] = Σ P(X ≥ k); LOTUS.
Worked (5): hat-check expected fixed points = 1 (indicators, no counting) · dice-pair sums · coupon collector light (n = 2, 3, then general) · expected number of records in a sequence · warm-up to the sum-until-1 problem.

### Ch4 — The distribution toolkit (~14 pp · 1 notebook · ~10 tests)
Bernoulli, binomial, geometric, Poisson; uniform, exponential, normal; memorylessness twice (geometric & exponential); Poisson process intuition, lightly; when each appears in interviews.
Worked (4): rolls-until-first-6 three ways (tail sum, geometric, recursion) · bus-stop waiting time · birthday-count → Poisson approximation · why E[X²] ≠ E[X]².

### Ch5 — Interview expected-value problem families (~18 pp · 1 notebook · ~12 tests) ← the heart
The six moves, formalized: condition on first step · linearity + indicators · symmetry/exchangeability · recursion on states (first-step analysis) · backward induction · complement.
Worked (6): E[flips until HH] = 6 (recursion) · E[flips until HT] = 4 (the shocker — same setup, different answer, why) · stop-or-roll dice game (backward induction) · "roll until sum > 12" · records/best-prize problem · a fair-game pricing question.
Every problem: analytic + Monte Carlo side by side.

### Ch6 — Random walks & gambler's ruin (~14 pp · 1 notebook · ~10 tests)
Random walk from scratch; first-step analysis as a linear system; ruin probabilities; expected durations; drift = p − q; optional stopping stated honestly (when it's safe, when it's abused).
Worked (4): fair-coin ruin probability · biased-walk expected hitting time (10/0.2 = 50) · gambler's target sizing · why the martingale doubling system fails (E stays 0, ruin prob → 1) — the honest debunk.

### Ch7 — Continuous thinking & simulation sanity checks (~12 pp · 1 notebook · ~8 tests)
Discrete → continuous done carefully; order statistics (max/min of uniforms, expected range); spacings; integrals replacing sums; the meta-skill: a 20-line Monte Carlo as an interview sanity check — and its honest limits.
Worked (3): E[max of two uniforms] = 2/3 · sum-of-uniforms-until-1 = e (closed out properly) · points-on-a-circle semicircle (if it fits; else → drills).

### Appendix A — Drill protocol + tracker (~6 pp)
Practice-aloud protocol; 3-week spaced schedule; probe-response templates; printable log (CSV/XLSX generator script — the old Bucket 2, shrunk to fit).

## Pre-agreed cut rules (invoked in this order, never renegotiated mid-slip)
1. A1: tracker appendix → one-page protocol sheet
2. A2: Ch7 dissolves into Ch5/6 (keep its two best problems)
3. A3: worked problems per chapter 6 → 4
**Never cut:** verification suite · two-ways-per-problem · Ch5 (the heart).

## Honest build budget
| Piece | Hours |
|---|---|
| LaTeX prose + derivations | ~26 |
| Notebooks + verification suite | ~10 |
| Packaging, cover, product page | ~6 |
| Buffer | ~8 |
| **Total** | **~50 h ≈ 7–9 weeks at 5–8 h/wk** |

This is above the earlier 25–30 h estimate — tutorial depth at honest size. The buffer absorbs one bad week, not two. Hence the cut rules.

## Schedule (13-week window, Oct 1 → Dec 30)
- W1–2: Ch1–2 · W3: Ch3 · W4: Ch4 · W5–6: Ch5 · W7: Ch6 · W8: Ch7 + appendix
- W9: verification polish + packaging · W10 (~Dec 8): launch · W11–13: measure
- **Deadline tension, flagged honestly:** full-course launch ~Dec 8 leaves ~3 weeks inside the 90-day metric window. Mitigation option: **early-access split** — package Ch1–4 + suite as paid early access, launch post ~Nov 8 at $14 (price rises to $19 at full launch); the Nov post is *the* launch post, Dec 15 final chapters ship as an update + a short "shipped" comment on the same post. First sales can land a month earlier; one-post discipline roughly preserved. DECISION PENDING.

## Legal line (standing)
Teach the folk canon (coins, dice, ruin — nobody's property) in original prose with original dressings. No verbatim Green Book/Crack problems or solution text.