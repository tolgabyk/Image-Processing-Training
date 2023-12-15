import cv2

# içe aktarma

img = cv2.imread("messi.jpg", 0)

# gorsellestir

cv2.imshow("Ilk Resim", img)

k = cv2.waitKey(0) & 0xFF

if k == 27:  # esc
    cv2.destroyAllWindows()

elif k == ord("s"):
    cv2.imwrite("messi_grey.png", img)
    cv2.destroyAllWindows()
