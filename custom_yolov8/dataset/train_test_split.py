import os
import random
import shutil

# Directories
train_image_dir = "dataset/images/train/mix_all"
train_label_dir = "dataset/labels/train/mix_all"
val_image_dir = "dataset/images/val/mix_all"
val_label_dir = "dataset/labels/val/mix_all"

# Ensure validation directories exist
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Get a list of all image files in the train image directory
image_files = [f for f in os.listdir(train_image_dir) if os.path.splitext(f)[1].lower() in ['.jpg', '.png']]

random.shuffle(image_files)
val_size = int(len(image_files) * 0.17)
val_images = image_files[:val_size]

# Move selected images and their corresponding labels
for img_file in val_images:
    img_name, _ = os.path.splitext(img_file)
    # Paths for the image and label files
    img_path = os.path.join(train_image_dir, img_file)
    label_path = os.path.join(train_label_dir, img_name + ".txt")
    
    # Move the image file
    shutil.move(img_path, os.path.join(val_image_dir, img_file))
    
    # Move the label file if it exists
    if os.path.exists(label_path):
        shutil.move(label_path, os.path.join(val_label_dir, img_name + ".txt"))

print("Splitting complete!")

