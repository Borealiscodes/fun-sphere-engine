# Fun‑Sphere Engine — Wave‑C File #4
# Hybrid Uplift: Spectral Monster Registry
# Author: Borealis S. Hedling (2026-10-25)

class Monster:
    """
    Represents a spectral entity in the Fun‑Sphere world.
    Monsters correspond to perturbation signatures, operator interactions,
    and spectral ecology dynamics. This file remains structurally pure.
    """

    def __init__(self, name: str, description: str = "",
                 faction: str = None, spectral_signature: dict = None,
                 metadata: dict = None):
        self.name = name
        self.description = description
        self.faction = faction
        self.spectral_signature = spectral_signature or {}
        self.metadata = metadata or {}

    def as_dict(self) -> dict:
        """
        Export monster as a dictionary.
        """
        return {
            "name": self.name,
            "description": self.description,
            "faction": self.faction,
            "spectral_signature": self.spectral_signature,
            "metadata": self.metadata
        }


class MonsterRegistry:
    """
    Registry for all Fun‑Sphere spectral monsters.
    This module contains no physics/UI/runtime logic and remains modular.
    """

    def __init__(self):
        self.monsters = {}

    def add(self, monster: Monster):
        """
        Add a monster to the registry.
        """
        self.monsters[monster.name] = monster

    def get(self, name: str) -> Monster:
        """
        Retrieve a monster by name.
        """
        return self.monsters.get(name)

    def list(self) -> list:
        """
        List all monster names.
        """
        return list(self.monsters.keys())

    def as_dict(self) -> dict:
        """
        Export all monsters as a dictionary.
        """
        return {name: monster.as_dict() for name, monster in self.monsters.items()}
