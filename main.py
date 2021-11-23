import cv2

# Read Image
f = input("File name: ")
img = cv2.imread("img\\"+f+".png")

# Convert to Gray Image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Invert Image
inverted_img = 255 - gray_img

# Blurred Image
blurred = cv2.GaussianBlur(inverted_img,(21,21),0)
inverted_blur = 255 - blurred
pencil_sketch = cv2.divide(gray_img,inverted_blur,scale=256.0)

# Show Image
cv2.imshow(f"Orignal Image {f}",img)
cv2.imshow(f"Pencil Sketch Image",pencil_sketch)
cv2.waitKey(0)

cv2.pencilSketch()