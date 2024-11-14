import cv2
import os

def convert_images_to_gray(source_folder, target_folder):
    
    # Iterate over all files in the source folder
    for filename in os.listdir(source_folder):
        # Define full path of source and target files
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, filename)

        # Check if the file is an image and if the converted file already exists
        if os.path.isfile(source_path) and not os.path.exists(target_path):
            try:
                # Read the image in BGR format
                image = cv2.imread(source_path)
                
                # If the image was read correctly, convert it to grayscale
                if image is not None:
                    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    
                    # Save the grayscale image to the target folder
                    cv2.imwrite(target_path, gray_image)
                    print(f"Converted and saved: {filename}")
                else:
                    print(f"Skipping file (not an image): {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        else:
            print(f"Skipping already converted or non-image file: {filename}")