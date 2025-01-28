from ultralytics import YOLO
import cv2
import cvzone
import math
import pyttsx3

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set the speaking rate
engine.setProperty('volume', 0.8)  # Set the volume (0.0 to 1.0)

# AI Helper Function to Speak Detected Objects
def speak_object(class_name, confidence):
    message = f"I detected a {class_name} with {int(confidence * 100)} percent confidence."
    engine.say(message)
    engine.runAndWait()

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(3, 700)  # Set width
cap.set(4, 620)  # Set height

# Load YOLO model
model = YOLO("yolov8n.pt")

# Class names
classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", 
    "truck", "boat", "traffic light", "fire hydrant", "stop sign", 
    "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", 
    "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", 
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", 
    "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", 
    "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", 
    "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", 
    "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", 
    "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", 
    "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", 
    "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", 
    "scissors", "teddy bear", "hair drier", "toothbrush"
]

# Confidence threshold for speaking detected objects
CONFIDENCE_THRESHOLD = 0.6

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read from camera.")
        break

    # Run YOLO inference
    results = model(img, stream=True)

    # Process results
    for r in results:
        if not hasattr(r, "boxes"):
            continue  # Skip if no detections

        boxes = r.boxes
        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            # Draw corner rectangle
            cvzone.cornerRect(img, (x1, y1, w, h), l=30, t=5, rt=1)

            # Confidence
            conf = round(float(box.conf[0]), 2)

            # Class ID
            cls = int(box.cls[0])
            class_name = classNames[cls] if cls < len(classNames) else "Unknown"

            # Draw text
            cvzone.putTextRect(
                img, 
                f"{class_name} {conf}", 
                (max(0, x1), max(35, y1)), 
                scale=2, thickness=2, offset=10
            )

            # AI Function: Speak detected objects above confidence threshold
            if conf > CONFIDENCE_THRESHOLD:
                speak_object(class_name, conf)

    # Display the image
    cv2.imshow("Detection", img)

    # Break loop on 'q' key press
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
