from core.person_inspection import PersonInspection

INSPECTIONS = {
        "person": PersonInspection
}

class InspectionFactory:
    @staticmethod
    def create(name):
        if name not in INSPECTIONS:
            raise ValueError(f"Unknown inspection type: {name}")

        inspection_class = INSPECTIONS[name]
        return inspection_class()
