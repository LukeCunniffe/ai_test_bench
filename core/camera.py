import cv2

class Camera:

    def __init__(self, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)

        if not self.camera.isOpened():
            raise RuntimeError("Unable to open camera.")

    def capture(self):

        success, frame = self.camera.read()

        if not success:
            raise RuntimeError("Unable to capture frame.")

        return frame

    def release(self):
        self.camera.release()
