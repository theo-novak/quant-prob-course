# The Probability Gap
*Quant Interview Foundations from Zero* — private content-build repo.

Frozen spec & decision log: `SPEC.md`. Chapter outline: `OUTLINE.md`.

## Build & test
```
uv sync                  # create/refresh .venv from pyproject (uv.lock pinned)
uv run pytest            # verification suite
tectonic latex/main.tex  # build the PDF
```

## Rules of the repo
- Every worked problem: analytic derivation + Monte Carlo verification. Never cut.
- Every test deterministic: RNGs derive from `SESSION_SEED` in `tests/conftest.py`.
- Cut rules and scope decisions live in `SPEC.md` — no mid-slip renegotiation.

## Repository map

| path | what it is | status |
|---|---|---|
| `SPEC.md` | frozen decision log: goal, success metric, 11 logged decisions, anti-drift cut rules (A1–A3), legal line | done |
| `OUTLINE.md` | 7-chapter outline with page/test budgets, worked-problem lists, honest build hours | frozen with spec |
| `STATUS.md` | resume map — where the work parked (Oct 4, 2026) and the one gate (Ch1 voice verdict) before more prose is written | current |
| `latex/main.tex` | book skeleton: theorem environments (Worked Problem / Interview Probe / Note), title, TOC | done |
| `latex/chapters/ch1.tex` | Ch1 "Counting from Scratch" (~12 pp): multiplication rule, perms/combs, complement & symmetry, stars & bars, 4 worked problems, drills | drafted, awaiting voice verdict |
| `tests/conftest.py` | reproducibility backbone: one master seed, per-test RNG factory — same stream every run | done |
| `tests/test_smoke.py` | toolchain + determinism smoke tests (rng streams, sympy reference value) | green (4/4) |
| `pyproject.toml`, `uv.lock` | pinned build environment for the eventual 60–70 test suite | done |
| `latex/main.pdf` | compiled build of the book-in-progress | regenerable |