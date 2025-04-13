import torch
import cv2
from pathlib import Path

# Load YOLOv5 model (you can also choose yolov5m, yolov5l, yolov5x)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Read input image from command-line
image_path = "D:/one pixel attack site/output/attack1.png"
img = cv2.imread(image_path)

# Perform detection
results = model(img)

# Extract predictions
labels, cords = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

# Print detected object names
detected_names = results.names
print("Detected objects:")
for label in labels:
    print("-", detected_names[int(label)])

# Optional: Show the image with bounding boxes
results.show()  # Opens image with boxes