import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

def get_camera_model(image_path):
    """
    Extracts the camera model from the EXIF data of an image.

    :param image_path: Path to the image file.
    :return: Camera model as a string, or None if not found.
    """
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == 'Model':
                        return value
    except Exception as e:
        print(f"Error reading {image_path}: {e}")
    return None

def organize_photos_by_camera(source_dir, destination_dir):
    """
    Organizes photos in the source directory into subdirectories based on the camera model.

    :param source_dir: Directory containing the photos to be organized.
    :param destination_dir: Directory where organized photos will be placed.
    """
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(source_dir, filename)
            camera_model = get_camera_model(file_path)
            if camera_model:
                camera_dir = os.path.join(destination_dir, camera_model)
                if not os.path.exists(camera_dir):
                    os.makedirs(camera_dir)
                shutil.move(file_path, os.path.join(camera_dir, filename))
                print(f"Moved {filename} to {camera_dir}")
            else:
                print(f"Could not determine camera model for {filename}")

def main():
    source_directory = 'path/to/source/directory'
    destination_directory = 'path/to/destination/directory'
    organize_photos_by_camera(source_directory, destination_directory)

if __name__ == '__main__':
    main()