# Fun‑Sphere Engine — Wave‑C File #3
# Hybrid Uplift: Faction Registry (Operator-Family Layer)
# Author: Borealis S. Hedling (2026-10-25)

class Faction:
    """
    Represents a faction in the Fun‑Sphere world.
    Factions correspond to families of operators, spectral tendencies,
    and narrative curvature signatures. This file remains structurally pure.
    """

    def __init__(self, name: str, description: str = "", operators: list = None, metadata: dict = None):
        self.name = name
        self.description = description
        self.operators = operators or []
        self.metadata = metadata or {}

    def add_operator(self, operator_name: str):
        """
        Add an operator name associated with this faction.
        (Actual operator objects live in engine/operators.py)
        """
        self.operators.append(operator_name)

    def as_dict(self) -> dict:
        """
        Export faction as a dictionary.
        """
        return {
            "name": self.name,
            "description": self.description,
            "operators": self.operators,
            "metadata": self.metadata
        }


class FactionRegistry:
    """
    Registry for all Fun‑Sphere factions.
    This module contains no physics/UI/runtime logic and remains modular.
    """

    def __init__(self):
        self.factions = {}

    def add(self, faction: Faction):
        """
        Add a faction to the registry.
        """
        self.factions[faction.name] = faction

    def get(self, name: str) -> Faction:
        """
        Retrieve a faction by name.
        """
        return self.factions.get(name)

    def list(self) -> list:
        """
        List all faction names.
        """
        return list(self.factions.keys())

    def as_dict(self) -> dict:
        """
        Export all factions as a dictionary.
        """
        return {name: faction.as_dict() for name, faction in self.factions.items()}
