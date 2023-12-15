import cv2

img = cv2.imread("Lenna.png")

print("Resim boyutu: ", img.shape)

cv2.imshow("Orijinal: ", img)

imgResized = cv2.resize(img, (800, 800))
print("Resized image shape: ", imgResized.shape)
cv2.imshow("img Resized", imgResized)

# kırp

imgCropped = img[:200, :300]  # height - width

cv2.imshow("Kirpilmiş", imgCropped)
