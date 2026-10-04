"""Bucket 1.1 smoke test: toolchain present + reproducibility backbone works."""
import numpy as np


def test_numpy_available():
    assert np.__version__


def test_rng_factory_deterministic(rng_factory):
    """Same child seed -> identical stream in every run (reproducibility backbone)."""
    a = rng_factory(7).uniform(size=8)
    b = rng_factory(7).uniform(size=8)
    np.testing.assert_array_equal(a, b)


def test_rng_streams_independent(rng_factory):
    """Different child seeds -> different streams (no accidental correlation)."""
    a = rng_factory(7).uniform(size=8)
    c = rng_factory(8).uniform(size=8)
    assert not np.array_equal(a, c)


def test_sympy_reference_values():
    """Known reference value: 5-card poker hands = C(52,5) = 2,598,960."""
    from sympy import binomial

    assert binomial(52, 5) == 2_598_960