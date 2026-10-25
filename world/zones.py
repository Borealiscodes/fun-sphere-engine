# Fun‑Sphere Engine — Wave‑C File #2
# Hybrid Uplift: Holonomy-Aware Zone Registry
# Author: Borealis S. Hedling (2026-10-25)

class Zone:
    """
    Represents a world zone in the Fun‑Sphere Engine.
    Zones are holonomy-aware containers that will later integrate
    curvature response, spectral ecology, and reversible narrative flow.
    """

    def __init__(self, name: str, description: str = "", metadata: dict = None):
        self.name = name
        self.description = description
        self.metadata = metadata or {}

    def as_dict(self) -> dict:
        """
        Return a dictionary representation of the zone.
        """
        return {
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata
        }


class ZoneRegistry:
    """
    Registry for all Fun‑Sphere world zones.
    This module remains structurally pure and contains no physics/UI/runtime logic.
    """

    def __init__(self):
        self.zones = {}

    def add(self, zone: Zone):
        """
        Add a zone to the registry.
        """
        self.zones[zone.name] = zone

    def get(self, name: str) -> Zone:
        """
        Retrieve a zone by name.
        """
        return self.zones.get(name)

    def list(self) -> list:
        """
        List all zone names.
        """
        return list(self.zones.keys())

    def as_dict(self) -> dict:
        """
        Export all zones as a dictionary.
        """
        return {name: zone.as_dict() for name, zone in self.zones.items()}
