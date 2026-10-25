# Fun‑Sphere Engine — Wave‑A File #3
# Minimal Geometric Spine: Laplacian Builder
# Author: Borealis S. Hedling (2026-10-25)

import numpy as np

class LaplacianBuilder:
    """
    Constructs the ND Laplacian operator for the Fun‑Sphere manifold.
    The Laplacian encodes diffusion, curvature response, and topology-driven flow.
    This module remains mathematically sterile and contains no world/UI/runtime logic.
    """

    def __init__(self, dims: int = 9):
        self.dims = dims
        self.matrix = self._build_laplacian()

    def _build_laplacian(self) -> np.ndarray:
        """
        Build a simple ND Laplacian using the discrete second-difference operator.
        This is a placeholder substrate; higher-order geometric Laplacians can be
        introduced in later phases without breaking Phase‑A purity.
        """
        L = np.zeros((self.dims, self.dims), dtype=np.complex128)

        for i in range(self.dims):
            L[i, i] = -2
            if i > 0:
                L[i, i - 1] = 1
            if i < self.dims - 1:
                L[i, i + 1] = 1

        return L

    def as_matrix(self) -> np.ndarray:
        """
        Return the Laplacian matrix.
        """
        return self.matrix

    def apply(self, state_vector: np.ndarray) -> np.ndarray:
        """
        Apply the Laplacian to the state vector.
        Caller is responsible for normalization and reversibility.
        """
        return np.dot(self.matrix, state_vector)
