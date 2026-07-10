import cv2

class OverlayRenderer:

    def render(self, frame, detections, results):
        annotated_frame = frame.copy()

        self.draw_detections(
                annotated_frame,
                detections
        )

        self._draw_header(annotated_frame)

        self._draw_results(
                annotated_frame,
                results
        )

        self._draw_controls(
                annotated_frame
        )

        return annotated_frame

    def _draw_header(self, frame):
        cv2.putText(
                frame,
                "AI Test Bench",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
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
                    (255, 255, 255),
                    2
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
                        (255, 255, 255),
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
                (255, 255, 255),
                1
        )

    def draw_detections(self, frame, detections):

        for detection in detections:

            cv2.rectangle(
                    frame,
                    (detection.x1, detection.y1),
                    (detection.x2, detection.y2),
                    (0, 255, 0),
                    2
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
                    (0, 255, 0),
                    2
            )
