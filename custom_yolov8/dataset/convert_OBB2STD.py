import os
from tqdm import tqdm
from PIL import Image

def convert_yolo_obb_to_yolo(label_dir, img_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Loop through all label files
    for label_file in tqdm(os.listdir(label_dir)):
        if label_file.endswith('.txt'):
            label_path = os.path.join(label_dir, label_file)
            img_path = os.path.join(img_dir, label_file.replace('.txt', '.jpg'))  # Adjust extension if needed
            
            if not os.path.exists(img_path):
                print(f"Image file not found for {label_file}, skipping...")
                continue
            
            # Get image dimensions
            img = Image.open(img_path)
            img_width, img_height = img.size
            
            # Open label file
            with open(label_path, 'r') as f:
                lines = f.readlines()
            
            # Convert each line
            converted_lines = []
            for line in lines:
                data = line.strip().split()
                if data[0] == "YOLO_OBB":
                    continue  # Skip header if present
                class_id = data[0]
                x_center = float(data[1]) / img_width
                y_center = float(data[2]) / img_height
                width = float(data[3]) / img_width
                height = float(data[4]) / img_height
                
                # Create standard YOLO format line
                converted_line = f"{class_id} {x_center:.4f} {y_center:.4f} {width:.4f} {height:.4f}"
                converted_lines.append(converted_line)
            
            # Write converted labels to new file
            output_label_path = os.path.join(output_dir, label_file)
            with open(output_label_path, 'w') as f:
                f.write('\n'.join(converted_lines))
            
            print(f"Converted: {label_file}")

# Directories
label_dir = "dataset/labels/train/oyster_omelet/YOLOv5_labels"
img_dir = "dataset/images/train/oyster_omelet"
output_dir = "dataset/labels/train/oyster_omelet"

# Convert labels
convert_yolo_obb_to_yolo(label_dir, img_dir, output_dir)