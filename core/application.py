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
from rendering.overlay_renderer import OverlayRenderer
import time

class Application:

    def __init__(self):

        print("Starting AI Test Bench . . . ")

        self.config = Config()

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

        self.renderer = OverlayRenderer()

        self.camera = Camera(
                self.config.camera_index
        )

    def run(self):
        print("Starting live inspection. . .")
        print("Press 's' to save an inspection.")
        print("Press 'q' to quit.")
        
        previous_time = time.time()

        try:
            while True:
                frame = self.camera.capture()

                if frame is None:
                    print("Warning: unable to capture frame. Exiting live inspection.")
                    break

                detections = self.detector.detect(frame)
                results = self.manager.run_all(detections)
                
                current_time = time.time()
                elapsed_time = current_time - previous_time

                fps = 1 / elapsed_time if elapsed_time > 0 else 0

                previous_time = current_time

                annotated_frame = self.renderer.render(
                        frame,
                        detections,
                        results,
                        fps
                )

                self.camera.show(annotated_frame)

                key = self.camera.get_key()

                if key == ord("s"):
                    self.complete_inspection(results)

                elif key == ord("q"):
                    break
        
        finally:
            self.camera.release()

    def complete_inspection(self, results):
        report = InspectionReport(
                self.config.app_name,
                self.config.version,
                results
        )

        overall_result = (
                "PASS" if report.overall_passed() else "FAIL"
        )

        self.database.save(overall_result)
        report.print_report()
