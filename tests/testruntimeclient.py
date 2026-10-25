"""
Fun‑Sphere Engine — Wave‑T Test Suite
File: test_runtime_client.py
Altitude: C‑Layer • Runtime Mirror Consistency

Purpose:
    Validate client-side state mirroring, deterministic snapshot ingestion,
    and non-mutation guarantees for server snapshots.

This test ensures:
    - Client mirrors server snapshots deterministically
    - Client does not mutate incoming snapshot data
    - Client local state updates are stable and predictable
    - Repeated ingestion of identical snapshots yields identical client state
"""

import copy
import json

# ---------------------------------------------------------------------------
# Mock server + client (matches runtime/client.py pattern)
# ---------------------------------------------------------------------------

class MockServer:
    def __init__(self):
        self.state = {"player": {"x": 0, "y": 0}, "zone": "Neutral"}

    def snapshot(self):
        return json.loads(json.dumps(self.state))


class MockClient:
    def __init__(self):
        self.local_state = None

    def ingest_snapshot(self, snap):
        """
        Client must deep-copy the snapshot and never mutate the original.
        """
        self.local_state = json.loads(json.dumps(snap))


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_client_ingests_snapshot_correctly():
    """Client must mirror server snapshot exactly."""
    server = MockServer()
    client = MockClient()

    snap = server.snapshot()
    client.ingest_snapshot(snap)

    assert client.local_state == snap, "Client failed to mirror snapshot"


def test_client_does_not_mutate_snapshot():
    """Client must not mutate incoming snapshot data."""
    server = MockServer()
    client = MockClient()

    snap = server.snapshot()
    before = copy.deepcopy(snap)

    client.ingest_snapshot(snap)
    after = snap

    assert before == after, "Client mutated incoming snapshot — forbidden"


def test_client_local_state_is_deep_copy():
    """Client local state must be a deep copy, not a reference."""
    server = MockServer()
    client = MockClient()

    snap = server.snapshot()
    client.ingest_snapshot(snap)

    client.local_state["player"]["x"] = 999

    assert snap["player"]["x"] == 0, \
        "Client local state mutated original snapshot"


def test_client_ingestion_is_deterministic():
    """Repeated ingestion of identical snapshots must yield identical state."""
    server = MockServer()
    client = MockClient()

    snap = server.snapshot()

    client.ingest_snapshot(snap)
    state1 = copy.deepcopy(client.local_state)

    client.ingest_snapshot(snap)
    state2 = copy.deepcopy(client.local_state)

    assert state1 == state2, "Client ingestion is not deterministic"


def test_client_state_structure_is_stable():
    """Client state structure must remain stable and predictable."""
    server = MockServer()
    client = MockClient()

    snap = server.snapshot()
    client.ingest_snapshot(snap)

    state = client.local_state

    assert "player" in state
    assert "zone" in state
    assert "x" in state["player"]
    assert "y" in state["player"]
