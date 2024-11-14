import cv2
import os

def resize_and_replace_images(source_folder, target_size):
    """
    Resizes all images in a folder to the specified dimensions, overwriting the originals.
    
    Parameters:
    - source_folder: Path to the folder containing the images to be resized.
    - target_size: Tuple of (width, height) representing the desired image size.
    """
    # Iterate over all files in the source folder
    for filename in os.listdir(source_folder):
        # Full path to the source image
        source_path = os.path.join(source_folder, filename)
        
        # Skip if it's not a file
        if not os.path.isfile(source_path):
            continue

        try:
            # Read the image
            image = cv2.imread(source_path)

            # Check if the file is a valid image
            if image is not None:
                # Resize the image
                resized_image = cv2.resize(image, target_size)
                
                # Overwrite the original image with the resized version
                cv2.imwrite(source_path, resized_image)
                print(f"Resized and replaced: {filename}")
            else:
                print(f"Skipping non-image file: {filename}")
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")