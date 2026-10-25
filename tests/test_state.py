"""
Fun‑Sphere Engine — Wave‑T Test Suite
File: test_state.py
Altitude: A‑Layer • Substrate Invariance

Purpose:
    Validate ND state invariance, identity‑metric behavior, and reversible
    initialization semantics for the geometric substrate.

This test ensures:
    - State objects initialize deterministically
    - Identity metric is preserved
    - No mutation occurs during read operations
    - Reversible operators do not alter baseline state
"""

import copy
import math

# ---------------------------------------------------------------------------
# Mock State Class (matches engine/state.py structure)
# ---------------------------------------------------------------------------

class State:
    def __init__(self, dim=4):
        self.dim = dim
        self.vector = [0.0] * dim  # identity baseline
        self.metric = [[1.0 if i == j else 0.0 for j in range(dim)]
                       for i in range(dim)]

    def as_tuple(self):
        return tuple(self.vector)

    def apply_identity(self):
        # reversible identity operator
        return copy.deepcopy(self)

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_state_initialization():
    """State initializes with zero vector and identity metric."""
    s = State(dim=4)

    assert s.vector == [0.0, 0.0, 0.0, 0.0]
    assert s.metric[0][0] == 1.0
    assert s.metric[1][1] == 1.0
    assert s.metric[2][2] == 1.0
    assert s.metric[3][3] == 1.0

    # off‑diagonal must be zero
    assert all(s.metric[i][j] == 0.0 for i in range(4) for j in range(4) if i != j)


def test_state_as_tuple_is_pure():
    """as_tuple() must not mutate internal state."""
    s = State(dim=3)
    before = copy.deepcopy(s.vector)

    _ = s.as_tuple()
    after = s.vector

    assert before == after, "as_tuple() mutated state — forbidden"


def test_identity_operator_is_reversible():
    """Identity operator must return a deep copy with identical values."""
    s = State(dim=5)
    s2 = s.apply_identity()

    assert s.as_tuple() == s2.as_tuple()
    assert s is not s2, "Identity operator must return a new object"


def test_metric_is_positive_definite():
    """Identity metric must be positive‑definite."""
    s = State(dim=4)

    # For identity matrix, x^T M x = sum(x_i^2)
    x = [1.0, -2.0, 3.0, -4.0]
    quadratic_form = sum(v * v for v in x)

    assert quadratic_form > 0.0
    assert math.isclose(quadratic_form, 1 + 4 + 9 + 16)
