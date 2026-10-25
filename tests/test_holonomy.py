"""
Fun‑Sphere Engine — Wave‑T Test Suite
File: test_holonomy.py
Altitude: A‑Layer • Holonomy Curvature

Purpose:
    Validate holonomy loop correctness, frame‑shift invariance, and reversible
    curvature semantics for the geometric substrate.

This test ensures:
    - Holonomy loops return to the same base point
    - Frame shift is consistent and deterministic
    - Holonomy is zero for flat operator sequences
    - Curvature accumulates correctly for non‑commuting operators
"""

import copy

# ---------------------------------------------------------------------------
# Mock operators for holonomy tests
# ---------------------------------------------------------------------------

class State:
    def __init__(self, vector):
        self.vector = list(vector)

    def copy(self):
        return State(self.vector[:])


def op_A(state):
    """Operator A: +1 to each component."""
    new = state.copy()
    new.vector = [v + 1 for v in new.vector]
    return new


def op_B(state):
    """Operator B: +2 to each component."""
    new = state.copy()
    new.vector = [v + 2 for v in new.vector]
    return new


def op_A_inv(state):
    """Inverse of A."""
    new = state.copy()
    new.vector = [v - 1 for v in new.vector]
    return new


def op_B_inv(state):
    """Inverse of B."""
    new = state.copy()
    new.vector = [v - 2 for v in new.vector]
    return new


# ---------------------------------------------------------------------------
# Holonomy helper
# ---------------------------------------------------------------------------

def holonomy_loop(state, ops):
    """
    Apply a sequence of operators and then their inverses in reverse order.
    Returns:
        final_state, frame_shift
    """
    s = state.copy()

    # forward pass
    for op in ops:
        s = op(s)

    # backward pass (apply inverses in reverse order)
    inverse_map = {op_A: op_A_inv, op_B: op_B_inv}
    for op in reversed(ops):
        s = inverse_map[op](s)

    # frame shift = difference between original and final
    shift = [s.vector[i] - state.vector[i] for i in range(len(state.vector))]
    return s, shift


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_holonomy_flat_sequence():
    """Holonomy must be zero for commuting operators."""
    s = State([0, 0, 0])
    final, shift = holonomy_loop(s, [op_A, op_A])

    assert final.vector == s.vector
    assert shift == [0, 0, 0], "Flat holonomy produced non-zero curvature"


def test_holonomy_non_commuting_sequence():
    """Non-commuting operators produce non-zero holonomy curvature."""
    s = State([0, 0, 0])
    final, shift = holonomy_loop(s, [op_A, op_B])

    # Expected curvature: op_A then op_B vs op_B then op_A differ by +1
    assert shift != [0, 0, 0], "Non-commuting operators produced zero holonomy"


def test_holonomy_returns_to_base_point():
    """Holonomy loops must return to the same base point."""
    s = State([5, -3, 2])
    final, shift = holonomy_loop(s, [op_A, op_B, op_A])

    assert final.vector == s.vector, "Holonomy loop did not return to base point"


def test_holonomy_is_deterministic():
    """Holonomy curvature must be deterministic for identical sequences."""
    s = State([0, 0, 0])

    _, shift1 = holonomy_loop(s, [op_A, op_B])
    _, shift2 = holonomy_loop(s, [op_A, op_B])

    assert shift1 == shift2, "Holonomy curvature is not deterministic"
