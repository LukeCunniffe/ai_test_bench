class Detection:

    def __init__(
            self,
            class_name,
            confidence,
            x1,
            y1,
            x2,
            y2
    ):
        self.class_name = class_name
        self.confidence = confidence
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
