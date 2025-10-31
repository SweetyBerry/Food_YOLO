import os

# List of directories in the desired order
directories = [
    "bawan", "beef_noodles", "beef_soup", "braised_pork_over_rice", "brown_sugar_cake",
    "bubble_tea", "caozaiguo", "coffin_toast", "cold_noodles", "deep-fried_chicken_cutlets",
    "egg_pancake_roll", "fried_eel_noodles", "fried_instant_noodles", "grilled_corn",
    "grilled_taiwanese_sausage", "hung_rui_chen_sandwich", "kung-pao_chicken", "mochi",
    "mung_bean_smoothie_milk", "nougat", "oyster_fritter", "oyster_omelet", "pepper_pork_bun",
    "pineapple_cake", "potsticker", "preserved_egg_tofu", "rice_dumpling",
    "rice_with_soy-stewed_pork", "roasted_sweet_potato", "sanxia_golden_croissants",
    "scallion_pancake", "sesame_oil_chicken_soup", "shrimp_rice", "sishen_soup", "sliced_pork_bun",
    "spicy_duck_blood", "stewed_pig_s_knuckles", "stinky_tofu", "sun_cake", "sweet_and_sour_pork_ribs",
    "taiwanese_sausage_in_rice_bun", "three-cup_chicken", "tube-shaped_migao", "turkey_rice",
    "turnip_cake", "twist_roll", "wheel_pie", "xiaolongbao", "yolk_pastry"
]

# Base directory where all the class directories are located
base_directory = "dataset/labels/train"

# Iterate through the directories and update the files
for i, subdir in enumerate(directories):
    # Path to the YOLOv5_labels directory for the current class
    subdir_path = os.path.join(base_directory, subdir, "YOLOv5_labels")
    new_number = i  # Set the new number (0 to 48)
    
    if os.path.exists(subdir_path):
        for filename in os.listdir(subdir_path):
            if filename.endswith(".txt"):  # Process only .txt files
                file_path = os.path.join(subdir_path, filename)
                
                # Read the content of the file
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                
                # Modify the first number in each line
                updated_lines = []
                for line in lines:
                    parts = line.split()
                    if parts:  # Ensure the line is not empty
                        parts[0] = str(new_number)  # Replace the first number
                        updated_lines.append(" ".join(parts) + "\n")
                
                # Write the modified content back to the file
                with open(file_path, 'w') as file:
                    file.writelines(updated_lines)

        
        print(f"Files in {subdir} have been updated with the new number {new_number}.")
    else:
        print(f"Directory {subdir_path} does not exist.")


""" 
bawan
beef_noodles
beef_soup
braised_pork_over_rice
brown_sugar_cake
bubble_tea
caozaiguo
coffin_toast
cold_noodles
deep-fried_chicken_cutlets
egg_pancake_roll
fried_eel_noodles
fried_instant_noodles
grilled_corn
grilled_taiwanese_sausage
hung_rui_chen_sandwich
kung-pao_chicken
mochi
mung_bean_smoothie_milk
nougat
oyster_fritter
oyster_omelet
pepper_pork_bun
pineapple_cake
potsticker
preserved_egg_tofu
rice_dumpling
rice_with_soy-stewed_pork
roasted_sweet_potato
sanxia_golden_croissants
scallion_pancake
sesame_oil_chicken_soup
shrimp_rice
sishen_soup
sliced_pork_bun
spicy_duck_blood
stewed_pig_s_knuckles
stinky_tofu
sun_cake
sweet_and_sour_pork_ribs
taiwanese_sausage_in_rice_bun
three-cup_chicken
tube-shaped_migao
turkey_rice
turnip_cake
twist_roll
wheel_pie
xiaolongbao
yolk_pastry"""
