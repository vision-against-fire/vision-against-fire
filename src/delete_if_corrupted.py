from PIL import Image
import os

def delete_corrupted_images(source_folder):
    """Delete image files that cannot be opened with Pillow."""
    total = len(os.listdir(source_folder))
    count = 0
    for filename in os.listdir(source_folder):
        count += 1
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            file_path = os.path.join(source_folder, filename)
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Verify if it's an image
            except (IOError, SyntaxError):
                print(f"Deleting corrupted image: {file_path}")
                os.remove(file_path)
        print(f"Processed {count}/{total} images.")


source_folder = '/Users/cho/Downloads/Fire/augstd/nonfire'
delete_corrupted_images(source_folder)
