import torch
import cv2

def detect_obstacles():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return []
    _, frame = cap.read()
    cap.release()
    results = model(frame)
    return results.pandas().xyxy[0][results.pandas().xyxy[0]['confidence'] > 0.5]['name'].unique().tolist()
