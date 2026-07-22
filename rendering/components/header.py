import cv2

from rendering.colours import WHITE
from rendering.constants import (
        HEADER_X,
        HEADER_Y,
        HEADER_FONT_SCALE,
)

class HeaderRenderer:

    def draw(self, frame, fps):
        cv2.putText(
                frame,
                "AI TEST BENCH",
                (HEADER_X, HEADER_Y),
                cv2.FONT_HERSHEY_SIMPLEX,
                HEADER_FONT_SCALE,
                WHITE,
                2,
        )

        fps_text = f"FPS: {fps:.1f}"

        text_size, _ = cv2.getTextSize(
                fps_text,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                2,
        )

        frame_width = frame.shape[1]

        cv2.putText(
                frame,
                fps_text,
                (frame_width - text_size[0] - 20, HEADER_Y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                WHITE,
                2
        )
