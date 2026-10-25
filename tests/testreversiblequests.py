"""
Fun‑Sphere Engine — Wave‑T Test Suite
File: test_reversible_quests.py
Altitude: C‑Layer • Reversible Narrative Physics

Purpose:
    Validate reversible quest sequences, operator-path correctness, and
    deterministic forward/backward traversal semantics.

This test ensures:
    - Quests apply deterministic operator sequences
    - Reversing a quest restores original state
    - Quest steps do not mutate input state
    - Quest logs are stable and predictable
"""

import copy

# ---------------------------------------------------------------------------
# Mock reversible quest system (matches quests/reversible.py pattern)
# ---------------------------------------------------------------------------

class State:
    def __init__(self, value):
        self.value = value

    def copy(self):
        return State(self.value)


def step_plus_one(state):
    new = state.copy()
    new.value += 1
    return new


def step_times_two(state):
    new = state.copy()
    new.value *= 2
    return new


def step_plus_one_inv(state):
    new = state.copy()
    new.value -= 1
    return new


def step_times_two_inv(state):
    new = state.copy()
    new.value //= 2
    return new


INVERSE_MAP = {
    step_plus_one: step_plus_one_inv,
    step_times_two: step_times_two_inv,
}


class Quest:
    def __init__(self, steps):
        self.steps = steps
        self.log = []

    def run(self, state):
        s = state.copy()
        for step in self.steps:
            s = step(s)
            self.log.append(step.__name__)
        return s

    def reverse(self, state):
        s = state.copy()
        for step in reversed(self.steps):
            inv = INVERSE_MAP[step]
            s = inv(s)
        return s


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_quest_forward_is_deterministic():
    """Forward quest execution must be deterministic."""
    q = Quest([step_plus_one, step_times_two])
    s = State(3)

    out1 = q.run(s)
    out2 = q.run(s)

    assert out1.value == out2.value, "Quest forward execution is not deterministic"


def test_quest_reverse_restores_original_state():
    """Reversing a quest must restore the original state."""
    q = Quest([step_plus_one, step_times_two])
    s = State(4)

    forward = q.run(s)
    backward = q.reverse(forward)

    assert backward.value == s.value, "Quest reverse failed to restore original state"


def test_quest_does_not_mutate_input_state():
    """Quest execution must not mutate the input state."""
    q = Quest([step_plus_one])
    s = State(10)
    before = s.value

    _ = q.run(s)
    after = s.value

    assert before == after, "Quest mutated input state — forbidden"


def test_quest_log_is_stable():
    """Quest log must be stable and predictable."""
    q = Quest([step_plus_one, step_times_two])
    s = State(1)

    q.run(s)

    assert q.log == ["step_plus_one", "step_times_two"], \
        "Quest log is unstable or incorrect"


def test_reverse_is_deterministic():
    """Reverse execution must be deterministic."""
    q = Quest([step_plus_one, step_times_two])
    s = State(5)

    forward = q.run(s)

    back1 = q.reverse(forward)
    back2 = q.reverse(forward)

    assert back1.value == back2.value, "Quest reverse execution is not deterministic"
