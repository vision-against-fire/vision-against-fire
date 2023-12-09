from PIL import Image, ImageEnhance, ImageFilter
import os
import numpy as np
import random

def add_gaussian_noise(image):
    """Add Gaussian noise to an image."""
    row, col, ch = image.shape
    mean = 0
    var = 0.1
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy_image = np.clip(image + gauss, 0, 255)
    return noisy_image.astype('uint8')

def color_jitter(image):
    """Randomly change the brightness, contrast, and saturation."""
    enhancer_types = [ImageEnhance.Brightness, ImageEnhance.Contrast, ImageEnhance.Color]
    for enhancer_type in enhancer_types:
        enhancer = enhancer_type(image)
        factor = random.uniform(0.7, 1.3) # Randomly change factor
        image = enhancer.enhance(factor)
    return image

def augment_image(img_path, dest_folder, filename):
    """Apply augmentations to an image and save them."""
    with Image.open(img_path) as img:
        # Keeping the image size 200x200
        img = img.resize((200, 200))

        # Zooming in a bit
        zoomed = img.crop((25, 25, 175, 175)).resize(img.size)
        zoomed.save(os.path.join(dest_folder, f"zoomed_{filename}"))

        # Adjusting the brightness
        brightness_enhancer = ImageEnhance.Brightness(img)
        brighter = brightness_enhancer.enhance(1.5) # 1.5 times brighter
        brighter.save(os.path.join(dest_folder, f"brighter_{filename}"))

        # Flip the image horizontally
        flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
        flipped.save(os.path.join(dest_folder, f"flipped_{filename}"))

        # Adding Gaussian noise
        noisy_image = add_gaussian_noise(np.array(img))
        noisy_pil = Image.fromarray(noisy_image)
        noisy_pil.save(os.path.join(dest_folder, f"noisy_{filename}"))

        # Color jittering
        jittered = color_jitter(img)
        jittered.save(os.path.join(dest_folder, f"jittered_{filename}"))

def augment_images(source_folder, dest_folder):
    """Augment all images in a folder."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(source_folder, filename)
            augment_image(img_path, dest_folder, filename)

# Example usage
source_folder = 'SOURCE' # Replace with your source folder path
dest_folder = 'DEST' # Replace with your destination folder path
augment_images(source_folder, dest_folder)
