import os
import shutil

def organize_desktop(source_dir, categories):
    """
    Organizes files and shortcuts from the desktop into specified categories.

    Args:
        source_dir (str): The path to the desktop directory.
        categories (dict): A dictionary where keys are category names and values are lists of file extensions.
    """
    for category, extensions in categories.items():
        category_dir = os.path.join(source_dir, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isfile(item_path):
                _, ext = os.path.splitext(item)
                if ext in extensions:
                    shutil.move(item_path, category_dir)
                    print(f"Moved {item} to {category}")

def main():
    desktop_path = os.path.expanduser("~/Desktop")
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Executables': ['.exe', '.lnk'],
        'Others': []
    }
    organize_desktop(desktop_path, categories)

if __name__ == '__main__':
    main()