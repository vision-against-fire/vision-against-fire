from PIL import Image
import os
import hashlib

def get_image_hash(img_path):
    """Generate a hash for an image."""
    with Image.open(img_path) as img:
        # Convert image to bytes
        img_bytes = img.tobytes()
        # Use SHA-1 hash function
        hash_obj = hashlib.sha1(img_bytes)
        return hash_obj.hexdigest()

def remove_duplicate_images(folder):
    """Remove duplicate images from a folder based on hash comparison."""
    image_hashes = {}
    images = os.listdir(folder)
    images = [img for img in images if img.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    total = len(images)
    count = 0

    for image in images:
        count += 1
        img_path = os.path.join(folder, image)
        img_hash = get_image_hash(img_path)

        if img_hash in image_hashes:
            # Duplicate found, remove it
            os.remove(img_path)
            print(f"Duplicate removed: {img_path}")
        else:
            image_hashes[img_hash] = img_path
        print(f"Processed {count}/{total} images.", end="\r")

# Example usage
folder = '/Users/cho/Downloads/Fire/augstd/fire'  # Replace with your folder path
remove_duplicate_images(folder)
