import os
import shutil
import random

def distribute_files(source_folder, dest1_folder, dest2_folder, probability_to_dest1=0.80):
    """Distribute files from source to two destinations based on a probability."""
    if not os.path.exists(dest1_folder):
        os.makedirs(dest1_folder)
    if not os.path.exists(dest2_folder):
        os.makedirs(dest2_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if random.random() < probability_to_dest1:
            shutil.move(file_path, os.path.join(dest1_folder, filename))
        else:
            shutil.move(file_path, os.path.join(dest2_folder, filename))

source1_folder = '/Users/cho/Downloads/Fire/4. Renamed copy/fire'  # Replace with your source folder path
dest11_folder = '/Users/cho/Downloads/Fire/4. Renamed copy/train_fire'    # Replace with your first destination folder path
dest12_folder = '/Users/cho/Downloads/Fire/4. Renamed copy/test_fire'    # Replace with your second destination folder path
distribute_files(source1_folder, dest11_folder, dest12_folder)

source2_folder = '/Users/cho/Downloads/Fire/4. Renamed copy/nonfire'  # Replace with your source folder path
dest21_folder = '/Users/cho/Downloads/Fire/4. Renamed copy/train_nonfire'    # Replace with your first destination folder path
dest22_folder = '/Users/cho/Downloads/Fire/4. Renamed copy/test_nonfire'    # Replace with your second destination folder path
distribute_files(source2_folder, dest21_folder, dest22_folder)
