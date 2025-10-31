# 🥗 Food_YOLO

This repository is the **Final Project** of the course  
*EFFICIENT AI MODEL DESIGN FOR MACHINE LEARNING AND INFERENCE*.

It implements a **YOLOv8-based food detection model**, trained to identify various food items efficiently for real-time inference.

---

## Model Weights

You can download the trained weights here:  
**[Google Drive – Food_YOLO Weights](https://drive.google.com/drive/folders/1wOXNcKV0T5EsvAtxDWtZud3jPGWgrZcc?usp=sharing)**

After downloading, place the `.pt` files under: \custom_yolov8\weights

---

## Dataset

You can download the dataset here:  
**[Google Drive – Food_YOLO Dataset](https://drive.google.com/drive/folders/1bbSo0qModXpOUyQzk6uvYJ1nGf6d_9dD?usp=sharing)**

After downloading, unzip the zip files to: \custom_yolov8

---

## Usage

You can use the model either **via Python API** or **command-line interface (CLI)**.

---

### **1. Python API**

```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model (or your custom weights)
model = YOLO("yolov8n.pt")  # or "custom_yolov8/weights/food_yolov8.pt"

# Display model information (optional)
model.info()

# Train the model on your dataset
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference on an image
results = model("path/to/food_image.jpg")

# Display or save results
results.show()       # visualize
results.save()       # save output
```

### **2. Command Line (CLI)**
```bash
# Train the YOLOv8 model on your dataset
yolo train model=yolov8n.pt data=coco8.yaml epochs=100 imgsz=640

# Run inference on an image
yolo predict model=yolov8n.pt source=path/to/food_image.jpg
```

## Notes

* Requires Python ≥ 3.8
* Install dependencies:
```bash
pip install ultralytics
```
* Replace yolov8n.pt with your custom Food_YOLO weights if needed.
* Recommended to run on GPU for faster inference.

## Reference

* Ultralytics YOLOv8 Documentation
* Course: Efficient AI Model Design for Machine Learning and Inference
* [Taiwanese Food 101 Dataset](https://www.kaggle.com/datasets/kuantinglai/taiwanese-food-101)
