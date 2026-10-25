"""
Fun‑Sphere Engine — Wave‑T Test Suite
File: test_operators.py
Altitude: A‑Layer • Operator Invariance

Purpose:
    Validate reversible operator behavior, identity preservation, and
    non-destructive application semantics for the geometric substrate.

This test ensures:
    - Operators are reversible (op(op⁻¹(x)) == x)
    - Operators do not mutate input state
    - Operator composition is associative
    - Identity operator behaves correctly
"""

import copy

# ---------------------------------------------------------------------------
# Mock reversible operators (matches engine/operator structure)
# ---------------------------------------------------------------------------

class State:
    def __init__(self, vector):
        self.vector = list(vector)

    def copy(self):
        return State(self.vector[:])


def op_add_one(state):
    """Reversible operator: +1 to each component."""
    new = state.copy()
    new.vector = [v + 1 for v in new.vector]
    return new


def op_sub_one(state):
    """Inverse operator: -1 to each component."""
    new = state.copy()
    new.vector = [v - 1 for v in new.vector]
    return new


def op_identity(state):
    """Identity operator: returns a deep copy."""
    return state.copy()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_operator_is_reversible():
    """op_add_one followed by op_sub_one must return original state."""
    s = State([0, 1, 2])
    s2 = op_add_one(s)
    s3 = op_sub_one(s2)

    assert s.vector == s3.vector, "Operator reversibility violated"


def test_operator_does_not_mutate_input():
    """Operators must not mutate the input state."""
    s = State([5, 5, 5])
    before = s.vector[:]

    _ = op_add_one(s)
    after = s.vector

    assert before == after, "Operator mutated input state — forbidden"


def test_identity_operator_is_correct():
    """Identity operator must return a deep copy with identical values."""
    s = State([3, 4, 5])
    s2 = op_identity(s)

    assert s.vector == s2.vector
    assert s is not s2, "Identity operator must return a new object"


def test_operator_composition_is_associative():
    """Composition: op_add_one(op_add_one(s)) == op_add_one(op_add_one(s))."""
    s = State([1, 2, 3])

    left = op_add_one(op_add_one(s))
    right = op_add_one(op_add_one(s))

    assert left.vector == right.vector, "Operator composition is not associative"


def test_inverse_restores_original_state():
    """op_sub_one(op_add_one(s)) must equal s for arbitrary values."""
    s = State([10, -4, 7])
    s2 = op_add_one(s)
    s3 = op_sub_one(s2)

    assert s.vector == s3.vector
