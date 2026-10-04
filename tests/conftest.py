"""Shared fixtures for The Probability Gap verification suite.

Reproducibility rules (per SPEC.md):
- One master seed for the whole project.
- Each test derives its own RNG from (SESSION_SEED, child_seed): streams are
  independent across tests AND identical across runs — no order dependence.
- Monte Carlo asserts must be tolerance-aware (error shrinks like 1/sqrt(n)).
"""
import numpy as np
import pytest

SESSION_SEED = 20261001  # project epoch: Oct 1, 2026


@pytest.fixture
def rng_factory():
    """Deterministic per-test RNG factory.

    Usage: rng = rng_factory(7) -> same stream for child seed 7 in every run.
    """
    def _make(child_seed: int = 0) -> np.random.Generator:
        return np.random.default_rng((SESSION_SEED, child_seed))

    return _make