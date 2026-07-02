"""

AI Test Bench

Component:
Detector

Purpose:
Loads the AI model and performs object detection
"""

from ultralytics import YOLO

class Detector:

    def __init__(self, model_path):

        print("Loading AI model....")

        self.model = YOLO(model_path)

        print("Model loaded.")

    def detect(self, frame):

        return self.model(frame)
