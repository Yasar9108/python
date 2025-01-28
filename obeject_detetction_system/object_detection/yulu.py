from ultralytics import YOLO
import cv2

models =YOLO("yolov8m.pt")
results =models("images/2.jpg",show=True)
cv2.waitKey(0)