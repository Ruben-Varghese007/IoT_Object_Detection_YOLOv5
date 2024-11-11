import streamlit as st
import torch
from PIL import Image
import numpy as np
import os

# Load the model
@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', 
                           path='Path_to_your/Object Detection - IoT/yolov5/runs/train/exp2/weights/best.pt', 
                           force_reload=True)  # Set force_reload=True to ensure it reloads the model
    return model

# Function to run detection on the uploaded image
def detect_image(model, image):
    img = Image.open(image)  # Open the image using PIL
    img = np.array(img)  # Convert to NumPy array
    
    # Run the YOLOv5 model
    results = model(img)

    # Results: boxes, labels, confidences
    return results

# Main function for Streamlit app
def main():
    st.title("Object Detection App")

    # Sidebar for image upload
    uploaded_image = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Load the YOLOv5 model
    model = load_model()

    if uploaded_image:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        
        # Run detection
        results = detect_image(model, uploaded_image)

        # Display results
        st.subheader("Detection Results")
        st.image(np.squeeze(results.render()), caption="Detected Image", use_column_width=True)
        
        # Display the detected objects
        st.write(results.pandas().xyxy[0])  # Display the bounding box coordinates and labels

if __name__ == "__main__":
    main()
