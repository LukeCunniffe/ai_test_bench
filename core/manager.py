class InspectionsManager:
    def __init__(self, inspection):
        self.inspection = inspection

    def run_all(self, detection):
        results = []

        for inspection in self.inspection:
            result = inspection.run(detection)
            results.append(result)

        return results

    def overall_passed(self, results):
        return all(result.passed for result in results)
