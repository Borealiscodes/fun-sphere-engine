# Fun‑Sphere Engine — Wave‑A File #1
# Minimal Geometric Spine: ND Manifold State Vector
# Author: Borealis S. Hedling (2026-10-25)

import numpy as np

class FunSphereState:
    """
    ND complex state vector representing the Fun‑Sphere manifold.
    This is the foundational substrate for all reversible operator flow,
    holonomy detection, Laplacian diffusion, and narrative curvature.
    """

    def __init__(self, dims: int = 9):
        self.dims = dims
        self.vector = self._init_state()

    def _init_state(self) -> np.ndarray:
        """
        Initialize the ND complex state vector with trace‑class‑1 normalization.
        """
        v = np.ones(self.dims, dtype=np.complex128)
        return self._normalize(v)

    def _normalize(self, v: np.ndarray) -> np.ndarray:
        """
        Normalize the vector such that sum(|x_i|) = 1.
        This ensures trace‑class stability across all operator flows.
        """
        magnitude = np.sum(np.abs(v))
        if magnitude == 0:
            return v
        return v / magnitude

    def reset(self):
        """
        Reset the state vector to its initial normalized baseline.
        """
        self.vector = self._init_state()

    def update(self, new_vector: np.ndarray):
        """
        Update the state vector with a reversible, normalized replacement.
        No information may be destroyed; caller must ensure reversibility.
        """
        self.vector = self._normalize(new_vector)

    def as_vector(self) -> np.ndarray:
        """
        Return the current ND complex state vector.
        """
        return self.vector
