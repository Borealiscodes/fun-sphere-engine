# Fun‑Sphere Engine — Wave‑A File #2
# Minimal Geometric Spine: Reversible Operator Registry
# Author: Borealis S. Hedling (2026-10-25)

import numpy as np

class OperatorBundle:
    """
    Represents a reversible operator acting on the Fun‑Sphere ND state vector.
    Operators must preserve information and maintain trace‑class stability.
    """

    def __init__(self, matrix: np.ndarray):
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Operator matrix must be square.")
        self.matrix = matrix.astype(np.complex128)

    def apply(self, state_vector: np.ndarray) -> np.ndarray:
        """
        Apply the operator to the state vector.
        Caller is responsible for ensuring reversibility and normalization.
        """
        return np.dot(self.matrix, state_vector)


class OperatorRegistry:
    """
    Registry of reversible operators available to the Fun‑Sphere Engine.
    This module remains mathematically sterile and contains no world/UI logic.
    """

    def __init__(self):
        self.operators = {}

    def add(self, name: str, operator: OperatorBundle):
        """
        Add a reversible operator to the registry.
        """
        self.operators[name] = operator

    def get(self, name: str) -> OperatorBundle:
        """
        Retrieve an operator by name.
        """
        return self.operators.get(name)

    def list(self):
        """
        List all registered operator names.
        """
        return list(self.operators.keys())
