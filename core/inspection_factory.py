from inspections.person import PersonInspection

INSPECTIONS = {
        "person": PersonInspection
}

class InspectionFactory:
    @staticmethod
    def create(name):
        if name not in INSPECTIONS:
            raise ValueError(f"Unknown inspection type: {name}")

        return INSPECTIONS[name]()
