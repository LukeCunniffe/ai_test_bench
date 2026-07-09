class InspectionReport:
    def __init__(self, app_name, version, results):
        self.app_name = app_name
        self.version = version
        self.results = results

    def overall_passed(self):
        return all(result.passed for result in self.results)

    def print_report(self):
        print()
        print("=" * 40)
        print("AI Test Bench Report")
        print("=" * 40)
        print(f"Application : {self.app_name}")
        print(f"Version : {self.version}")
        print("-" * 40)


        for result in self.results:
            symbol = "✓" if result.passed else "✗"
            status = "PASS" if result.passed else "FAIL"

            print(f"{symbol} {result.name}: {status}")
            
            for key, value in result.details.items():
                label = key.replace("_", " ").title()
                print(f"    {label}: {value}")

        print("-" * 40)

        overall_status = "PASS" if self.overall_passed() else "FAIL"
        print(f"Overall result: {overall_status}")
        print("=" * 40)
