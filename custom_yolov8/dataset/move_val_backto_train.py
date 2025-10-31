import os
import shutil

# Define directories
train_image_dir = "dataset/images/train/mix_all"
train_label_dir = "dataset/labels/train/mix_all"
val_image_dir = "dataset/images/val/mix_all"
val_label_dir = "dataset/labels/val/mix_all"

# Move files from val_image_dir to train_image_dir
for file_name in os.listdir(val_image_dir):
    source = os.path.join(val_image_dir, file_name)
    destination = os.path.join(train_image_dir, file_name)
    if os.path.isfile(source):  # Ensure it's a file
        shutil.move(source, destination)

# Move files from val_label_dir to train_label_dir
for file_name in os.listdir(val_label_dir):
    source = os.path.join(val_label_dir, file_name)
    destination = os.path.join(train_label_dir, file_name)
    if os.path.isfile(source):  # Ensure it's a file
        shutil.move(source, destination)

print("Files moved successfully!")