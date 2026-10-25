# Fun‑Sphere Engine — Wave‑A File #4
# Minimal Geometric Spine: Holonomy Detector
# Author: Borealis S. Hedling (2026-10-25)

import numpy as np

class HolonomyDetector:
    """
    Computes holonomy for the Fun‑Sphere ND manifold.
    Holonomy measures how much a state vector changes after traversing
    a closed loop under a sequence of reversible operators.

    This module remains mathematically sterile and contains no world/UI/runtime logic.
    """

    def __init__(self):
        pass

    def compute(self, state_vector: np.ndarray, operators: list) -> np.ndarray:
        """
        Apply a sequence of reversible operators to the state vector,
        then compare the final state to the initial state.

        Holonomy is defined as:
            H = final_state - initial_state

        Caller is responsible for normalization and reversibility.
        """
        initial = state_vector.copy()
        current = state_vector.copy()

        for op in operators:
            current = op.apply(current)

        return current - initial

    def magnitude(self, holonomy_vector: np.ndarray) -> float:
        """
        Compute the magnitude of holonomy as the L2 norm.
        """
        return float(np.linalg.norm(holonomy_vector))

    def is_nontrivial(self, holonomy_vector: np.ndarray, threshold: float = 1e-6) -> bool:
        """
        Determine whether holonomy is nontrivial.
        """
        return self.magnitude(holonomy_vector) > threshold
