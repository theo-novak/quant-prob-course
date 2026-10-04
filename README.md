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