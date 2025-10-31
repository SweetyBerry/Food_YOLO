import os
import shutil

def copy_to_mix_all(data_dir):
    mix_all_dir = os.path.join(data_dir, "mix_all")
    
    # Ensure the mix_all directory exists
    os.makedirs(mix_all_dir, exist_ok=True)
    
    # Iterate through all directories in data_dir
    for dir_name in os.listdir(data_dir):
        dir_path = os.path.join(data_dir, dir_name)
        
        # Skip the mix_all directory
        if dir_name == "mix_all" or not os.path.isdir(dir_path):
            continue
        
        # Copy all files from the current directory to mix_all
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            
            # Only copy files (skip subdirectories)
            if os.path.isfile(file_path):
                dest_path = os.path.join(mix_all_dir, file_name)
                # Handle duplicate file names by renaming
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(file_name)
                    counter = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(mix_all_dir, f"{base}_{counter}{ext}")
                        counter += 1
                shutil.copy(file_path, dest_path)
                print(f"Copied {file_path} to {dest_path}")

# Example usage
data_directory = "dataset/images/train"
copy_to_mix_all(data_directory)
