import cv2
from rendering.colours import WHITE, GREEN
from rendering.constants import (
        HEADER_X,
        HEADER_Y,
        RESULTS_X,
        RESULTS_Y,
        RESULT_SPACING,
        DETAIL_SPACING,
        CONTROLS_X,
        CONTROLS_BOTTOM_MARGIN,
        BOX_THICKNESS,
        HEADER_FONT_SCALE,
        RESULT_FONT_SCALE,
        DETAIL_FONT_SCALE,
        CONTROL_FONT_SCALE,
)

class OverlayRenderer:

    def render(self, frame, detections, results, fps):
        annotated_frame = frame.copy()

        self.draw_detections(
                annotated_frame,
                detections
        )

        self._draw_header(
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

    def _draw_header(self, frame, fps):
        cv2.putText(
                frame,
                "AI Test Bench",
                (HEADER_X, HEADER_Y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                WHITE,
                BOX_THICKNESS
        )

        fps_text = f"FPS: {fps:.1f}"

        text_size, _ = cv2.getTextSize(
                fps_text,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                BOX_THICKNESS
        )

        frame_width = frame.shape[1]

        cv2.putText(
                frame,
                fps_text,
                (frame_width - text_size[0] - 20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                WHITE,
                BOX_THICKNESS
        )

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

    def draw_detections(self, frame, detections):

        for detection in detections:

            cv2.rectangle(
                    frame,
                    (detection.x1, detection.y1),
                    (detection.x2, detection.y2),
                    GREEN,
                    BOX_THICKNESS
            )

            label = (
                    f"{detection.class_name} "
                    f"{detection.confidence:.2f}"
            )

            cv2.putText(
                    frame,
                    label,
                    (detection.x1, detection.y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    GREEN,
                    BOX_THICKNESS
            )
