import torch
import cv2
import numpy as np
import time
import streamlit as st

# Load your trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='saved_models/iot_object_detection_best.pt', force_reload=True) 

# Set confidence threshold
model.conf = 0.5  # confidence threshold (0-1)

# Function to detect objects using webcam
def run_detection():
    # Initialize webcam
    cap = cv2.VideoCapture(0)  # 0 for default camera, or use another number for an external camera
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Convert the frame to the expected format (RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Perform inference on the frame
        results = model(frame_rgb)

        # Get the detection results as a pandas DataFrame
        detections = results.pandas().xyxy[0]
        
        # Draw the bounding boxes and labels on the frame
        for index, row in detections.iterrows():
            # Get bounding box coordinates
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            # Get confidence score and label
            label = f"{row['name']} {row['confidence']:.2f}"

            # Draw the bounding box and label on the frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Display the frame with detections
        cv2.imshow('Webcam Object Detection', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Run object detection when this script is executed
if __name__ == "__main__":
    st.title("IoT Device Detection Using Webcam")
    st.write("Press the button to start webcam detection")
    
    if st.button('Start Webcam Detection'):
        run_detection()
