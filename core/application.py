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
from core.person_inspection import PersonInspection

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

        self.manager = InspectionsManager([
                PersonInspection
        ])

    def run(self):

        frame = self.camera.capture()

        detections = self.detector.detect(frame)

        results = self.manager.run_all(detections)

        overall_passed = self.manager.overall_passed(results)

        overall_result = "PASS" if overall_passed else "FAIL"

        self.database.save(overall_result)

        print()

        print("=" * 40)
        print(self.config.app_name)
        print(f"Version {self.config.version}")
        print("=" * 40)

        for result in results:
            print(result)

        print()
        print(f"Overall result: {overall_result}")

        self.camera.release()
