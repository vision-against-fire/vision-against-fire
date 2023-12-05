from PIL import Image
import numpy as np
import os

def standardize_image(img_path):
    """Resize an image to 200x200 and normalize its pixel values."""
    with Image.open(img_path) as img:
        # Resize image
        img = img.resize((200, 200))

        # Convert to NumPy array for normalization
        img_array = np.array(img, dtype=np.float32)

        # Normalize the image array to [0, 1]
        normalized_img_array = img_array / 255.0

        return normalized_img_array

def standardize_images(source_folder, dest_folder):
    """Standardize all images in a folder and save them."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    total = len(os.listdir(source_folder))
    count = 0
    for filename in os.listdir(source_folder):
        count += 1
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                img_path = os.path.join(source_folder, filename)
                standardized_img_array = standardize_image(img_path)

                # Save the standardized image
                standardized_img = Image.fromarray((standardized_img_array * 255).astype('uint8'))
                standardized_img.save(os.path.join(dest_folder, filename))
                os.remove(img_path)
                print('Standardized {}/{} images.'.format(count, total))
            except:
                print('Failed to standardize image {}'.format(filename))

# Example usage
source_folder = '/Users/cho/Downloads/Fire/3. Augmented/aug_nonfire' # Replace with your source folder path
dest_folder = '/Users/cho/Downloads/Fire/std_nonfire' # Replace with your destination folder path
standardize_images(source_folder, dest_folder)
