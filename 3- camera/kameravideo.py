import cv2

# capture

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)

# fourcc= çerçeveleri sıkıştırmak için kullanılan 4 karakterli codec kodu, 20 = saniyedeki kare hızı

writer = cv2.VideoWriter(
    "Video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)

    # save
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
