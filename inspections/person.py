from inspections.base import BaseInspection
from core.result import InspectionsResult

class PersonInspection(BaseInspection):

    def run(self, detections) -> InspectionsResult:

        people = 0

        for result in detections:
            for box in result.boxes:
                if int(box.cls) == 0:
                    people += 1


        return InspectionsResult(
                name="Person Detection",
                passed=people > 0,
                details={
                    "people_detected": people
                }
        )
