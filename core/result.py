from datetime import datetime


class InspectionsResult:
    def __init__(self, name, passed, details=None):
        self.name = name
        self.passed = passed
        self.details = details or {}
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (
            f"{self.name}: {self.result_text}\n"
            f"Details: {self.details}"
        )

    @property
    def result_text(self):
        return "PASS" if self.passed else "FAIL"
