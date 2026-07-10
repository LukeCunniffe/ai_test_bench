import cv2

class Camera:

    def __init__(self, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)

        if not self.camera.isOpened():
            raise RuntimeError("Unable to open camera.")

    def capture(self):

        success, frame = self.camera.read()

        if not success:
            return None

        return frame

    def show(self, frame):
        cv2.imshow("AI Test Bench", frame)

    def get_key(self):
        return cv2.waitKey(1) & 0xFF

    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()
