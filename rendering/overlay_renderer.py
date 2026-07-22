import cv2
from rendering.components.bounding_boxes import BoundingBoxRenderer
from rendering.colours import WHITE, GREEN
from rendering.components.header import HeaderRenderer
from rendering.constants import (
        RESULTS_X,
        RESULTS_Y,
        RESULT_SPACING,
        DETAIL_SPACING,
        CONTROLS_X,
        CONTROLS_BOTTOM_MARGIN,
        BOX_THICKNESS,
        RESULT_FONT_SCALE,
        DETAIL_FONT_SCALE,
        CONTROL_FONT_SCALE,
)

class OverlayRenderer:

    def __init__(self):
        self.header = HeaderRenderer()
        self.boxes = BoundingBoxRenderer()

    def render(self, frame, detections, results, fps):
        annotated_frame = frame.copy()

        self.boxes.draw(
                annotated_frame,
                detections
        )

        self.header.draw(
                annotated_frame,
                fps
        )

        self._draw_results(
                annotated_frame,
                results
        )

        self._draw_controls(
                annotated_frame
        )

        return annotated_frame

    def _draw_results(self, frame, results):
        y_position = 75


        for result in results:
            status = "PASS" if result.passed else "FAIL"

            cv2.putText(
                    frame,
                    f"{result.name}: {status}",
                    (20, y_position),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    WHITE,
                    BOX_THICKNESS
            )

            y_position += 30

            for key, value in result.details.items():
                label = key.replace("_", " ").title()

                cv2.putText(
                        frame,
                        f"{label}: {value}",
                        (40, y_position),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        BOX_THICKNESS,
                        1
                )

                y_position += 25

    def _draw_controls(self, frame):
        height = frame.shape[0]

        cv2.putText(
                frame,
                "[S] Save Inspection    [Q] Quit",
                (20, height - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                WHITE,
                1
        )
