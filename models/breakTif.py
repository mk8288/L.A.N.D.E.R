import numpy as np
from PIL import Image
import os

def split_image(image_path, output_folder, parts):
    """
    Split the given image into a specified number of parts.

    Parameters:
        image_path (str): Path to the image file.
        output_folder (str): Folder to save the split images.
        parts (int): Number of parts to split the image into.
    """
    # Load the image
    img = Image.open(image_path)
    
    # Calculate the size of each part
    img_width, img_height = img.size
    num_cols = int(np.sqrt(parts))
    num_rows = (parts + num_cols - 1) // num_cols  # Ceiling division

    part_width = img_width // num_cols
    part_height = img_height // num_rows

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Split the image
    count = 0
    for row in range(num_rows):
        for col in range(num_cols):
            left = col * part_width
            upper = row * part_height
            right = min(left + part_width, img_width)
            lower = min(upper + part_height, img_height)

            # Define the bounding box for each part
            bbox = (left, upper, right, lower)
            part = img.crop(bbox)

            # Save the part
            part.save(os.path.join(output_folder, f'part_{count + 1}.tif'))
            count += 1

            if count >= parts:
                break
        if count >= parts:
            break

def main(image_path, output_folder):
    # Number of parts to split the image into
    parts = 50
    split_image(image_path, output_folder, parts)

if __name__ == "__main__":
    # Replace 'path_to_your_image.tif' with the actual image path
    main('content/moonTest.tif', 'output_images')

