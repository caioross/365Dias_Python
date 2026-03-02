import os
import shutil
from datetime import datetime, timedelta

def get_desktop_path():
    """Returns the path to the desktop directory."""
    return os.path.join(os.path.expanduser("~"), "Desktop")

def organize_desktop(days_threshold):
    """
    Organizes the desktop by moving files accessed more than 'days_threshold' days ago to a 'Old Files' folder.
    
    :param days_threshold: Number of days since last access to consider a file old.
    """
    desktop_path = get_desktop_path()
    old_files_folder = os.path.join(desktop_path, "Old Files")
    
    if not os.path.exists(old_files_folder):
        os.makedirs(old_files_folder)
    
    threshold_date = datetime.now() - timedelta(days=days_threshold)
    
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        
        if os.path.isfile(file_path):
            last_access_time = datetime.fromtimestamp(os.path.getatime(file_path))
            
            if last_access_time < threshold_date:
                shutil.move(file_path, old_files_folder)
                print(f"Moved {filename} to 'Old Files' folder.")

def main():
    """Main function to execute the desktop organizer."""
    days_threshold = 30  # Example threshold: files not accessed in the last 30 days
    organize_desktop(days_threshold)

if __name__ == '__main__':
    main()