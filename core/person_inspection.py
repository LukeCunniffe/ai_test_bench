from core.result import InspectionsResult


class PersonInspection:

    def run(self, detections):

        people = 0

        for result in detections:
            for box in result.boxes:

                if int(box.cls) == 0:
                    people += 1

        passed = people > 0

        return InspectionsResult (
                name="Person Detection",
                passed=passed,
                details={
                    "people_detected": people
                }
        )
