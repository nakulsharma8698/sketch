import cv2
class ShapeDetector:
    def __init__(self):
        self.arr = []
        pass
    def detect(self, c):
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        #circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

        if len(approx) == 2:
            shape = "text"
            
        elif len(approx) == 3:
            shape = "DropDowncBox"

        elif len(approx) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape = "square"+str(len(approx)) if ar >= 0.95 and ar <= 1.05 else "Input Field"

        elif len(approx) == 5:
            shape = "pentagon"
        elif len(approx) == 6:
            shape = "Image"
            
        else:
            shape = "Submit Button"
        self.arr.append(shape)
        return shape