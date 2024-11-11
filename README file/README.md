# To create virtual environment
virtualenv myenv
myenv\Scripts\activate

# 1 Activate Virtual Environment
myenv\Scripts\activate

# 2 To Deactivate Virtual Environment 
deactivate

# 3 Install requirements.txt file 
pip install -r requirements.txt

# 4 To Download Dataset from Google (take from pinterest & other sources)
run the file -> download_dataset.py

# 5 Dataset Used - iot_dataset
# Recommend - Acquire own dataset rather than download_dataset due to less accuracy

# NOTE: Change - "Path_to_your" to your respective paths of the files

# 6 Train the Model - CPU (Run on GPU - given below)
cd yolov5
python train.py --img 640 --batch 16 --epochs 50 --data ../iot_dataset/data.yaml --weights yolov5s.pt --cache

Note:
--img: Image size (adjust this if needed)
--batch: Batch size (adjust according to your system’s capacity)
--epochs: Number of epochs
--data: Path to the data.yaml file
--weights: Pretrained weights (using yolov5s.pt here for transfer learning)
--cache: Use caching for faster training

# GPU - To run on GPU
python train.py --img 640 --batch 16 --epochs 50 --data ../iot_dataset/data.yaml --weights yolov5s.pt --cache --device 0

# Used one - To prevent Memory Error
python train.py --img 640 --batch 8 --epochs 50 --data ../iot_dataset/data.yaml --weights yolov5s.pt --cache disk --device 0

# If the above doesn't work use this one
python train.py --img 640 --batch 8 --epochs 50 --data ../iot_dataset/data.yaml --weights yolov5s.pt --cache disk --device 0 --accumulate 2

# Save the model with custom name
-> LINUX
cp runs/train/exp/weights/best.pt path_to_save/model_name.pt 

-> Windows 
Copy-Item "Path_to_your/Object Detection - IoT/yolov5/runs/train/exp/weights/best.pt" -Destination "Path_to_your/Object Detection - IoT/saved_models/iot_detect_best.pt"


# Validation
python val.py --weights runs/train/exp/weights/best.pt --data ../iot_dataset/data.yaml --img 640 --iou 0.65

# Validation on GPU
python val.py --weights runs/train/exp/weights/best.pt --data ../iot_dataset/data.yaml --img 640 --iou 0.65 --device 0

-> exp2 - more optimized model

# 7 Test the Model
python detect.py --weights runs/train/exp/weights/best.pt --source ../iot_dataset/test/images --img 640 --conf 0.5

# Test on GPU
python detect.py --weights runs/train/exp/weights/best.pt --source ../iot_dataset/test/images --img 640 --conf 0.5 --device 0

-> for cpu - add "--device cpu" instead of "--device 0"

-> exp2 - more optimized model

# Test Results - Results saved to runs\detect\exp

# 8 - Deploy - For Mobile Applications

Deploying the Saved Model - To export your model

## Step 1: Export YOLOv5 to ONNX and TFLITE
python export.py --weights runs/train/expX/weights/best.pt --img 640 --include onnx tflite

python export.py --weights runs/train/exp/weights/best.pt --img 640 --batch 1 --device 0 --include onnx tflite

## Step 2: Convert ONNX to TensorFlow Lite Use the ONNX-TensorFlow converter (not required)
onnx-tf convert -i best.onnx -o best_model.pb

## Step 3: Then convert the .pb file to TensorFlow Lite format (not required)
tflite_convert --saved_model_dir=best_model.pb --output_file=best_model.tflite

-> Note : This will generate the .onnx or .tflite models, which you can integrate into a mobile app.

# Used format - TorchScript - for Mobile Application Deployment

## To convert the pretrained model weights to torchscript format
python export.py --weights runs/train/exp2/weights/best.pt --include torchscript --img 640 --optimize

## To convert the pretrained model weights to torchscript format (GPU)
python export.py --weights runs/train/exp2/weights/best.pt --include torchscript --img 640 --optimize --device 0

## Results saved to Path_to_your\Object Detection - IoT\yolov5\runs\train\exp\weights

# 9 Test model on custom images
python detect.py --weights runs/train/exp/weights/best.pt --source path_to_test_images/ --img 640 --conf 0.5

# 10 Build the Mobile Application for Deployment
Coming Soon...

# Note: 
- Use Datasets with larger number of images for better results in better performance.
- Application used for annotation - Roboflow
