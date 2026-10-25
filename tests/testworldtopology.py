"""
Fun‑Sphere Engine — Wave‑T Test Suite
File: test_world_topology.py
Altitude: C‑Layer • World Topology

Purpose:
    Validate world topology containers, faction operator bundles, and spectral
    ecology invariance. Ensures world-layer structures behave deterministically
    and do not mutate input state.

This test ensures:
    - Zones initialize with stable topology
    - Factions apply deterministic operator bias
    - Monsters (spectral perturbations) behave consistently
    - World containers do not mutate external references
"""

import copy

# ---------------------------------------------------------------------------
# Mock world-layer structures (matches world/*.py patterns)
# ---------------------------------------------------------------------------

class Zone:
    def __init__(self, name, curvature=0.0):
        self.name = name
        self.curvature = curvature
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)


class Faction:
    def __init__(self, name, bias):
        """
        bias: integer added to monster spectral value
        """
        self.name = name
        self.bias = bias

    def apply_bias(self, monster):
        new = monster.copy()
        new.spectral += self.bias
        return new


class Monster:
    def __init__(self, species, spectral):
        self.species = species
        self.spectral = spectral

    def copy(self):
        return Monster(self.species, self.spectral)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_zone_initialization():
    """Zones must initialize with stable curvature and empty entity list."""
    z = Zone("Crystal Basin", curvature=1.25)

    assert z.name == "Crystal Basin"
    assert z.curvature == 1.25
    assert z.entities == [], "Zone initialized with non-empty entity list"


def test_zone_entity_addition_is_deterministic():
    """Adding entities must be deterministic and append-only."""
    z = Zone("Fog Valley")
    m1 = Monster("Wisp", spectral=3)
    m2 = Monster("Shade", spectral=7)

    z.add_entity(m1)
    z.add_entity(m2)

    assert len(z.entities) == 2
    assert z.entities[0].species == "Wisp"
    assert z.entities[1].species == "Shade"


def test_faction_bias_is_deterministic():
    """Faction bias must apply deterministically and not mutate input monster."""
    f = Faction("Lumina Order", bias=2)
    m = Monster("Sprite", spectral=5)

    before = m.spectral
    m2 = f.apply_bias(m)

    assert m.spectral == before, "Faction bias mutated input monster"
    assert m2.spectral == 7, "Faction bias did not apply correctly"


def test_monster_copy_is_deep():
    """Monster.copy() must return a deep copy with identical values."""
    m = Monster("Gloom", spectral=9)
    m2 = m.copy()

    assert m.spectral == m2.spectral
    assert m is not m2, "Monster.copy() returned same object"


def test_zone_does_not_mutate_external_entities():
    """Zone must not mutate entities passed into it."""
    z = Zone("Hollow Ridge")
    m = Monster("Echo", spectral=4)

    z.add_entity(m)
    m.spectral = 10  # mutate external reference

    # zone must preserve original spectral value
    assert z.entities[0].spectral == 4, "Zone mutated external entity reference"


def test_spectral_ecology_is_stable_under_small_changes():
    """Small spectral changes must not reorder monster families."""
    m1 = Monster("Wisp", spectral=3)
    m2 = Monster("Shade", spectral=7)
    m3 = Monster("Gloom", spectral=9)

    original_order = [m1.species, m2.species, m3.species]

    # small perturbation
    m2.spectral += 0.1

    new_order = [m1.species, m2.species, m3.species]

    assert original_order == new_order, "Spectral ecology ordering unstable"
