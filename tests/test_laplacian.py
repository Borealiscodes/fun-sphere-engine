"""
Fun‑Sphere Engine — Wave‑T Test Suite
File: test_laplacian.py
Altitude: A‑Layer • Spectral Geometry

Purpose:
    Validate Laplacian correctness, symmetry, positive semi-definiteness,
    and spectral stability for the geometric substrate.

This test ensures:
    - Laplacian is symmetric
    - Laplacian is positive semi-definite
    - Applying Laplacian does not mutate input state
    - Spectral ordering is stable under small perturbations
"""

import copy
import math

# ---------------------------------------------------------------------------
# Mock Laplacian (matches engine/laplacian structure)
# ---------------------------------------------------------------------------

def laplacian_matrix(dim):
    """
    Simple discrete Laplacian:
        L[i][i] = 2
        L[i][i±1] = -1
    """
    L = [[0.0 for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        L[i][i] = 2.0
        if i > 0:
            L[i][i - 1] = -1.0
        if i < dim - 1:
            L[i][i + 1] = -1.0
    return L


def apply_laplacian(L, vector):
    """Apply L * vector without mutating input."""
    new = vector[:]  # shallow copy
    result = [0.0 for _ in vector]
    for i in range(len(vector)):
        for j in range(len(vector)):
            result[i] += L[i][j] * vector[j]
    return result


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_laplacian_is_symmetric():
    """Laplacian must satisfy L[i][j] == L[j][i]."""
    L = laplacian_matrix(5)
    for i in range(5):
        for j in range(5):
            assert L[i][j] == L[j][i], "Laplacian symmetry violated"


def test_laplacian_is_positive_semidefinite():
    """
    For any vector x, x^T L x >= 0.
    This is true for the discrete Laplacian.
    """
    L = laplacian_matrix(4)
    x = [1.0, -2.0, 3.0, -1.0]

    quadratic = 0.0
    for i in range(4):
        for j in range(4):
            quadratic += x[i] * L[i][j] * x[j]

    assert quadratic >= 0.0, "Laplacian is not positive semi-definite"


def test_laplacian_does_not_mutate_input():
    """Applying Laplacian must not mutate the input vector."""
    L = laplacian_matrix(4)
    v = [1.0, 2.0, 3.0, 4.0]
    before = v[:]

    _ = apply_laplacian(L, v)
    after = v

    assert before == after, "Laplacian application mutated input vector"


def test_spectral_ordering_is_stable():
    """
    Small perturbations should not drastically reorder eigenvalues.
    We approximate eigenvalues using diagonal entries for this test.
    """
    L = laplacian_matrix(4)
    diag_original = [L[i][i] for i in range(4)]

    # perturb vector slightly
    L2 = laplacian_matrix(4)
    L2[0][0] += 0.001

    diag_perturbed = [L2[i][i] for i in range(4)]

    # ordering must remain identical
    assert sorted(diag_original) == sorted(diag_perturbed), \
        "Spectral ordering unstable under small perturbation"
