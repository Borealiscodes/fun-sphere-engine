# Fun‑Sphere Engine — Wave‑C File #7
# Hybrid Uplift: Reversible Quest Scaffold
# Author: Borealis S. Hedling (2026-10-25)

class QuestStep:
    """
    Represents a single reversible step in a Fun‑Sphere quest.
    Each step corresponds to:
        - an operator name
        - a description
        - optional metadata

    Actual operator objects live in engine/operators.py.
    """

    def __init__(self, operator: str, description: str = "", metadata: dict = None):
        self.operator = operator
        self.description = description
        self.metadata = metadata or {}

    def as_dict(self) -> dict:
        return {
            "operator": self.operator,
            "description": self.description,
            "metadata": self.metadata
        }


class ReversibleQuest:
    """
    Represents a reversible quest composed of operator steps.
    A reversible quest must satisfy:
        - forward operator sequence
        - backward operator sequence (reverse order)
        - structural purity (no physics/UI/runtime logic)
    """

    def __init__(self, name: str, description: str = "", steps: list = None, metadata: dict = None):
        self.name = name
        self.description = description
        self.steps = steps or []
        self.metadata = metadata or {}

    def add_step(self, step: QuestStep):
        self.steps.append(step)

    def forward_sequence(self) -> list:
        """
        Return the forward operator sequence.
        """
        return [step.operator for step in self.steps]

    def reverse_sequence(self) -> list:
        """
        Return the reverse operator sequence.
        """
        return [step.operator for step in reversed(self.steps)]

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "steps": [step.as_dict() for step in self.steps],
            "metadata": self.metadata
        }


class QuestRegistry:
    """
    Registry for reversible quests.
    Structurally pure, Phase‑C compliant, no physics/UI/runtime contamination.
    """

    def __init__(self):
        self.quests = {}

    def add(self, quest: ReversibleQuest):
        self.quests[quest.name] = quest

    def get(self, name: str) -> ReversibleQuest:
        return self.quests.get(name)

    def list(self) -> list:
        return list(self.quests.keys())

    def as_dict(self) -> dict:
        return {name: quest.as_dict() for name, quest in self.quests.items()}
