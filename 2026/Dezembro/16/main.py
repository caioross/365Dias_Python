import os
from PIL import Image
from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder, image_format='JPEG'):
    """
    Converts each page of a PDF file into individual image files.

    Args:
        pdf_path (str): The path to the PDF file.
        output_folder (str): The folder where the images will be saved.
        image_format (str): The format of the output images ('JPEG' or 'PNG').

    Raises:
        FileNotFoundError: If the PDF file does not exist.
        ValueError: If the image format is not supported.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The PDF file {pdf_path} does not exist.")

    if image_format not in ['JPEG', 'PNG']:
        raise ValueError("Unsupported image format. Use 'JPEG' or 'PNG'.")

    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    # Save each image to the output folder
    for i, image in enumerate(images):
        image_filename = f"page_{i + 1}.{image_format.lower()}"
        image_path = os.path.join(output_folder, image_filename)
        image.save(image_path, format=image_format)
        print(f"Saved {image_path}")

def main():
    pdf_path = 'example.pdf'  # Path to your PDF file
    output_folder = 'output_images'  # Folder to save the images

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to images
    convert_pdf_to_images(pdf_path, output_folder, image_format='JPEG')

if __name__ == '__main__':
    main()