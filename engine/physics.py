# Fun‑Sphere Engine — Wave‑A File #5
# Minimal Geometric Spine: Reversible Physics Flow
# Author: Borealis S. Hedling (2026-10-25)

import numpy as np
from .state import FunSphereState
from .operators import OperatorBundle, OperatorRegistry
from .laplacian import LaplacianBuilder
from .holonomy import HolonomyDetector

class PhysicsEngine:
    """
    Core reversible physics engine for the Fun‑Sphere ND manifold.
    Integrates:
        - state vector
        - reversible operators
        - ND Laplacian
        - holonomy detector

    This module remains mathematically sterile and contains no world/UI/runtime logic.
    """

    def __init__(self, dims: int = 9):
        self.state = FunSphereState(dims=dims)
        self.registry = OperatorRegistry()
        self.laplacian = LaplacianBuilder(dims=dims)
        self.holonomy = HolonomyDetector()

    def apply_operator(self, name: str):
        """
        Apply a registered reversible operator to the state vector.
        Caller is responsible for ensuring operator reversibility.
        """
        op = self.registry.get(name)
        if op is None:
            raise ValueError(f"Operator '{name}' not found.")
        new_vector = op.apply(self.state.as_vector())
        self.state.update(new_vector)

    def diffuse(self):
        """
        Apply Laplacian diffusion to the state vector.
        Caller is responsible for normalization and reversibility.
        """
        new_vector = self.laplacian.apply(self.state.as_vector())
        self.state.update(new_vector)

    def compute_holonomy(self, operator_sequence: list):
        """
        Compute holonomy for a sequence of reversible operators.
        """
        ops = [self.registry.get(name) for name in operator_sequence]
        hol = self.holonomy.compute(self.state.as_vector(), ops)
        return hol

    def holonomy_magnitude(self, operator_sequence: list) -> float:
        """
        Compute the magnitude of holonomy for a sequence of operators.
        """
        hol = self.compute_holonomy(operator_sequence)
        return self.holonomy.magnitude(hol)
