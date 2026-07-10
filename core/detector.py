"""

AI Test Bench

Component:
Detector

Purpose:
Loads the AI model and performs object detection
"""

from ultralytics import YOLO
from core.detection import Detection

class Detector:

    def __init__(self, model_path):

        print("Loading AI model....")

        self.model = YOLO(model_path)

        print("Model loaded.")

    def detect(self, frame):
        yolo_results = self.model(frame, verbose=False)

        detections = []

        for result in yolo_results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()

                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                class_name = self.model.names[class_id]

                detections.append(
                        Detection(
                            class_name=class_name,
                            confidence=confidence,
                            x1=x1,
                            y1=y1,
                            x2=x2,
                            y2=y2
                        )
                )

        return detections
