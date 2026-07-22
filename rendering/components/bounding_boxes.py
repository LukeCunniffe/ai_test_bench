import cv2

from rendering.colours import GREEN
from rendering.constants import BOX_THICKNESS

class BoundingBoxRenderer:

    def draw(self, frame, detections):

        for detection in detections:

            top_left = (
                    detection.x1,
                    detection.y1
            )

            bottom_right = (
                    detection.x2,
                    detection.y2
            )

            cv2.rectangle(
                    frame,
                    top_left,
                    bottom_right,
                    GREEN,
                    BOX_THICKNESS
            )

            label = (
                    f"{detection.class_name} "
                    f"{detection.confidence:.2f}"
            )

            label_y = max(
                    detection.y1 - 10,
                    20
            )

            cv2.putText(
                    frame,
                    label,
                    (detection.x1, label_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    GREEN,
                    2
            )
