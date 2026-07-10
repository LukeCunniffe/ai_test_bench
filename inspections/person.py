from inspections.base import BaseInspection
from core.result import InspectionsResult

class PersonInspection(BaseInspection):

    def run(self, detections):
        people_detected = sum(
                1
                for detection in detections
                if detection.class_name == "person"
        )

        passed = people_detected > 0


        return InspectionsResult(
                name="Person Detection",
                passed=passed,
                details={
                    "people_detected": people_detected
                }
        )
