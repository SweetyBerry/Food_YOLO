from pylabel import importer
import os

# Define the path to the directory containing the Pascal VOC annotations
path_to_annotations = "dataset/labels/train/sun_cake"

# Get all XML files in the directory
xml_files = [f for f in os.listdir(path_to_annotations) if f.endswith('.xml')]

if not xml_files:
    print("No XML files found in the specified directory.")
else:
    # Import Pascal VOC dataset
    dataset = importer.ImportVOC(path=path_to_annotations)

    # Export the dataset to YOLOv5 format
    yolo_path = os.path.join(path_to_annotations, "YOLOv5_labels")  # Define output folder
    os.makedirs(yolo_path, exist_ok=True)  # Create the folder if it doesn't exist
    dataset.export.ExportToYoloV5(output_path=yolo_path)

    print(f"YOLOv5 labels successfully exported to: {yolo_path}")