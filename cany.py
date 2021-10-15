import cv2

image = cv2.imread('try1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# show the original and blurred images
cv2.imshow("Original", image)
# cv2.imshow("Blurred", blurred)

wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)
# show the output Canny edge maps
# cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
# cv2.imshow("Tight Edge Map", tight)
cv2.waitKey(0)