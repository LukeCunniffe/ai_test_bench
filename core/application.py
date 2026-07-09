"""

AI Test Bench

Component:
Application

Purpose:
Initialise the application and coordinates allmajor components
"""

from core.camera import Camera
from core.config import Config
from core.database import Database
from core.detector import Detector
from core.manager import InspectionsManager
from core.inspection_factory import InspectionFactory
from core.inspection_report import InspectionReport

class Application:

    def __init__(self):

        print("Starting AI Test Bench . . . ")

        self.config = Config()

        self.camera = Camera(
                self.config.camera_index
        )

        self.detector = Detector(
                self.config.model_path
        )

        self.database = Database(
                self.config.database_path
        )

        inspections = []

        for inspection_name in self.config.enabled_inspections:
            inspections.append(
                    InspectionFactory.create(inspection_name)
            )
        
        self.manager = InspectionsManager(inspections)

    def run(self):

        frame = self.camera.capture()

        detections = self.detector.detect(frame)

        results = self.manager.run_all(detections)

        report = InspectionReport(
                self.config.app_name,
                self.config.version,
                results
        )

        overall_result = "PASS" if report.overall_passed() else "FAIL"

        self.database.save(overall_result)

        report.print_report()

        self.camera.release()
