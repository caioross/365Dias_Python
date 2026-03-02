import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

def get_dominant_colors(image_path, num_colors=5):
    """
    Extracts the top 'num_colors' dominant colors from an image.

    Parameters:
    image_path (str): The path to the image file.
    num_colors (int): The number of dominant colors to extract.

    Returns:
    list: A list of the top 'num_colors' dominant colors in hexadecimal format.
    """
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to a list of pixels
    pixels = image.reshape((-1, 3))

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    # Get the most common colors
    labels = kmeans.labels_
    counts = Counter(labels)
    most_common_labels = counts.most_common(num_colors)

    # Get the hexadecimal color codes
    dominant_colors = []
    for label, _ in most_common_labels:
        color = kmeans.cluster_centers_[label]
        hex_color = '#{:02x}{:02x}{:02x}'.format(int(color[0]), int(color[1]), int(color[2]))
        dominant_colors.append(hex_color)

    return dominant_colors

def main():
    """
    Main function to execute the script.
    """
    image_path = 'path_to_your_image.jpg'  # Replace with the path to your image
    dominant_colors = get_dominant_colors(image_path)
    print("Dominant Colors:", dominant_colors)

if __name__ == '__main__':
    main()