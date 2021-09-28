import cv2

image = "pic1"
img_exr = ".jpg"

img = cv2.imread(image+img_exr)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", img)
cv2.imshow("Black and white", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()