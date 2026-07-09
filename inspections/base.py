from core.result import InspectionsResult
from abc import ABC, abstractmethod

class BaseInspection(ABC):
    """
    Base class for every inspection.

    Every inspection must implement the run() method.
    """

    @abstractmethod
    def run(self, detections) -> InspectionsResult:
        """Run the inspection and return the result."""
        pass
