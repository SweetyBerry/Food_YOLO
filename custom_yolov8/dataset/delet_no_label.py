import os
from tqdm import tqdm

# Directories for images and labels
image_dir = "dataset/images/train/mix_all"
label_dir = "dataset/labels/train/mix_all"

# List all label filenames without extension
label_files = {os.path.splitext(f)[0] for f in os.listdir(label_dir) if f.endswith(".txt")}

# Iterate through image files
for img_file in os.listdir(image_dir):
    # Get the file name without extension
    img_name, img_ext = os.path.splitext(img_file)
    
    # Check if it is an image file and has no corresponding label
    if img_ext.lower() in ['.jpg', '.png'] and img_name not in label_files:
        # Delete the image file
        os.remove(os.path.join(image_dir, img_file))
        print(f"Deleted: {img_file}")

print("Cleaning complete!")

