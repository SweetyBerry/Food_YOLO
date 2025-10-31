import os
import shutil

def copy_labels_to_mix_all(label_dir):
    # Path to the mix_all directory
    mix_all_dir = os.path.join(label_dir, "mix_all")
    
    # Ensure the mix_all directory exists
    os.makedirs(mix_all_dir, exist_ok=True)
    
    # Iterate through all class directories in label_dir
    for class_dir in os.listdir(label_dir):
        class_path = os.path.join(label_dir, class_dir)
        
        # Skip the mix_all directory and non-directory items
        if class_dir == "mix_all" or not os.path.isdir(class_path):
            continue
        
        # Path to the YOLOv5_labels subdirectory
        yolo_labels_path = os.path.join(class_path, "YOLOv5_labels")
        
        # Skip if YOLOv5_labels doesn't exist or is not a directory
        if not os.path.isdir(yolo_labels_path):
            continue
        
        # Copy all label files from YOLOv5_labels to mix_all
        for label_file in os.listdir(yolo_labels_path):
            label_file_path = os.path.join(yolo_labels_path, label_file)
            
            # Only copy files (skip directories)
            if os.path.isfile(label_file_path):
                dest_path = os.path.join(mix_all_dir, label_file)
                
                # Handle duplicate file names by renaming
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(label_file)
                    counter = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(mix_all_dir, f"{base}_{counter}{ext}")
                        counter += 1
                
                shutil.copy(label_file_path, dest_path)
                print(f"Copied {label_file_path} to {dest_path}")

# Example usage
label_directory = "dataset/labels/train"
copy_labels_to_mix_all(label_directory)
