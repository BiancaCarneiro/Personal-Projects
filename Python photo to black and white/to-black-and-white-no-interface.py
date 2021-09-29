import cv2

def to_gray(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray

def to_sketch(img):
    # lets create a sketch
    # Steps:
    # 1: Convert to grey -> DONE
    img_gray = to_gray(img)
    # 2: Invert Image
    img_invert = cv2.bitwise_not(img_gray)
    # 3: Blur image
    img_blur = cv2.GaussianBlur(img_invert, (111,111),0)
    # 4: Invert Blurred image
    img_blurinvert = cv2.bitwise_not(img_blur)
    # 5: bit-wise division -> Final step
    img_sketch = cv2.divide(img_gray, img_blurinvert, scale=256.0)
    return img_sketch



if __name__ == "__main__":
    image = "pictures\pic3.jpg"
    img = cv2.imread(image)
    cv2.imshow("Original", img)
    img_gray = to_gray(img)
    cv2.imshow("Black and white", img_gray)
    #cv2.imwrite('black-and-white.jpg',img_gray)
    img_sketch = to_sketch(img)
    cv2.imshow("Sketch", img_sketch)

    cv2.waitKey(0)
    cv2.destroyAllWindows()