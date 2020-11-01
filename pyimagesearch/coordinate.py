import cv2
from pyimagesearch.points import Points
class Coordinate:
    def __init__(self):
        pass
    def coordinates(self, c):
        approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True)
        n = approx.ravel()
        i = 0
        for j in n:
            if (i % 2 == 0):
                x = n[i]
                y = n[i + 1]

                # String containing the co-ordinates.
                string = str(x) + " " + str(y)

                if (i == 0):
                    # text on topmost co-ordinate.
                    val = Points(x,y)
                   # coo = val.first(x,y)

        return val
