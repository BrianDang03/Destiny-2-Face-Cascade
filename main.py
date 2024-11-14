from destiny_2_face_detection import detect_destiny_face
from resize_images import resize_and_replace_images
from grayscale_converter import convert_images_to_gray

def main():

    source_folder_n = "assets/negative_sample"  # Replace with the path to your source folder
    target_folder_n = "destiny_face_cascade/n"  # Replace with the path to your target folder
    convert_images_to_gray(source_folder_n, target_folder_n)

    source_folder_p = "assets/positive_sample"  # Replace with the path to your source folder
    target_folder_p = "destiny_face_cascade/p"  # Replace with the path to your target folder
    convert_images_to_gray(source_folder_p, target_folder_p)

    source_folder_p = "destiny_face_cascade/p"  # Replace with your source folder path
    target_size_p = (400, 400)                 # Desired size as (width, height)
    resize_and_replace_images(source_folder_p, target_size_p)

    detect_destiny_face("assets/Destiny_Face_Cascade_Test.mp4")

main()