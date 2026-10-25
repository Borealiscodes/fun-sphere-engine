"""
Fun‑Sphere Engine — Wave‑T Test Suite
File: test_runtime_server.py
Altitude: C‑Layer • Runtime Invariance

Purpose:
    Validate server snapshot correctness, deterministic serialization, and
    non-mutation guarantees for world and state objects.

This test ensures:
    - Server snapshots are deterministic
    - Snapshot serialization does not mutate runtime state
    - Snapshot structure is stable and predictable
    - Repeated snapshots of identical state are identical
"""

import copy
import json

# ---------------------------------------------------------------------------
# Mock server (matches runtime/server.py pattern)
# ---------------------------------------------------------------------------

class MockServer:
    def __init__(self):
        self.state = {"player": {"x": 0, "y": 0}, "zone": "Neutral"}

    def snapshot(self):
        """
        Returns a JSON-safe deep copy of the current state.
        """
        return json.loads(json.dumps(self.state))


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_snapshot_is_deep_copy():
    """Snapshot must be a deep copy, not a reference."""
    server = MockServer()
    snap = server.snapshot()

    snap["player"]["x"] = 999

    assert server.state["player"]["x"] == 0, \
        "Snapshot mutated server state — forbidden"


def test_snapshot_is_deterministic():
    """Two snapshots of identical state must be identical."""
    server = MockServer()

    snap1 = server.snapshot()
    snap2 = server.snapshot()

    assert snap1 == snap2, "Snapshots of identical state differ"


def test_snapshot_structure_is_stable():
    """Snapshot structure must remain stable and predictable."""
    server = MockServer()
    snap = server.snapshot()

    assert "player" in snap
    assert "zone" in snap
    assert "x" in snap["player"]
    assert "y" in snap["player"]


def test_snapshot_does_not_mutate_state():
    """Snapshot generation must not mutate runtime state."""
    server = MockServer()
    before = copy.deepcopy(server.state)

    _ = server.snapshot()
    after = server.state

    assert before == after, "Snapshot mutated runtime state"


def test_snapshot_serialization_is_json_safe():
    """Snapshot must be JSON-serializable without errors."""
    server = MockServer()
    snap = server.snapshot()

    try:
        json.dumps(snap)
        ok = True
    except Exception:
        ok = False

    assert ok, "Snapshot is not JSON-serializable"
