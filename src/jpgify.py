from PIL import Image
import os

def convert_to_jpg(source_folder):
    """Convert all image files in the folder to .jpg format, skip if already .jpg."""
    total = len(os.listdir(source_folder))
    count = 0
    for filename in os.listdir(source_folder):
        count += 1
        if filename.lower().endswith(('.png', '.jpeg', '.bmp', '.gif')):  # Add other formats as needed
            file_path = os.path.join(source_folder, filename)
            # Open the image
            with Image.open(file_path) as img:
                # Remove extension and add .jpg
                new_filename = os.path.splitext(filename)[0] + '.jpg'
                new_file_path = os.path.join(source_folder, new_filename)
                # Convert and save as .jpg
                img.convert('RGB').save(new_file_path, 'JPEG')
                print(f"Converted {filename} to {new_filename}")
        print(f"Processed {count}/{total} images.", end="\r")


source_folder = '/Users/cho/Downloads/Fire/4. Renamed/nonfire'
convert_to_jpg(source_folder)

source_folder = '/Users/cho/Downloads/Fire/4. Renamed/fire'
convert_to_jpg(source_folder)
