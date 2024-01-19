import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture("/Users/pintojav/Library/CloudStorage/OneDrive-adidas/MASTER_CLASSES_OSCAR-JAIME/CLASS_HOW_ADD_NEW_FIELD_CONNECTOOR_KAFKA.mp4")

ret = True

while ret:
    ret, frame = cap.read()
    results = model.track(frame, persist=True)

    frame = frame[0].plot()

    cv2.imshow('frame', frame_)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

