from pyimagesearch.shape_detector import ShapeDetector
import imutils
import argparse
import cv2
"""ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())"""
image = cv2.imread("C:/Users/nakul/Desktop/NAKUL/try1paint.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

for c in cnts:
	M = cv2.moments(c)
	if M["m00"] != 0:
		cX = int((M["m10"] / M["m00"])*ratio)
		cY = int((M["m01"] / M["m00"])*ratio)
	else:
		cX, cY = 0, 0

	shape = sd.detect(c)
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

	cv2.imshow("Image", image)
	cv2.waitKey(0)