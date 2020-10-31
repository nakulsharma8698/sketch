from pyimagesearch.shape_detector import ShapeDetector
import imutils
import argparse
import cv2
"""ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())"""
image = cv2.imread("C:\\Users\\skullcandy\\Desktop\\try1paint.png")
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
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

	cv2.imshow("Image", image)
	cv2.waitKey(0)
print(sd.arr[::-1])
code = ""
st = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
footer {
  text-align: center;
  padding: 3px;
  background-color: DarkSalmon;
  color: white;
}
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}
</style>
</head>
<body>
<div class="topnav">
  <a class="active" href="#home">Home</a>
  <a href="#news">News</a>
  <a href="#contact">Contact</a>
  <a href="#about">About</a>
</div>
"""
en = """
<footer>&copy; Copyright 2020 Sketch2Code</footer>
</body>
</html>"""
f = open("code.html","w+")
for i in sd.arr[::-1]:
	if i =='Input field':
		code +="""<label for="myfile">Select a file:</label>
<input type="file" id="myfile" name="myfile">"""
	elif i == "text":
		code+="""
		<p><b>This is Demo Text</b></p>
		"""
	elif i =='Submit Button':
		code+="""<form action="/action_page.php" method="get" id="nameform">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
</form>

<p>The button below is outside the form element, but still part of the form.</p>

<button type="submit" form="nameform" value="Submit">Submit</button>"""

	elif i == 'Image':
		code+="""<img src="C:\\Users\\skullcandy\\Desktop\\222.jpg" alt="Italian Trulli">"""
	elif i == "DropDowncBox":
		code+="""<label for="cars">Choose a car:</label>

<select name="cars" id="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>"""

print(code)
f.write(st+code+en)
f.close()


