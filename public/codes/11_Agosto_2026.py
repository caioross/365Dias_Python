import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from prettytable import PrettyTable

def extract_metadata(mp3_file):
    """
    Extracts metadata from an MP3 file.

    Args:
        mp3_file (str): The path to the MP3 file.

    Returns:
        dict: A dictionary containing the metadata.
    """
    audio = MP3(mp3_file, ID3=EasyID3)
    metadata = {
        'artist': audio.get('artist', ['Unknown'])[0],
        'album': audio.get('album', ['Unknown'])[0],
        'year': audio.get('date', ['Unknown'])[0],
        'genre': audio.get('genre', ['Unknown'])[0]
    }
    return metadata

def list_mp3_files(directory):
    """
    Lists all MP3 files in a given directory.

    Args:
        directory (str): The directory to search for MP3 files.

    Returns:
        list: A list of paths to MP3 files.
    """
    mp3_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mp3'):
                mp3_files.append(os.path.join(root, file))
    return mp3_files

def display_metadata(mp3_files):
    """
    Displays the metadata of MP3 files in a table.

    Args:
        mp3_files (list): A list of paths to MP3 files.
    """
    table = PrettyTable()
    table.field_names = ["File", "Artist", "Album", "Year", "Genre"]

    for mp3_file in mp3_files:
        metadata = extract_metadata(mp3_file)
        table.add_row([os.path.basename(mp3_file), metadata['artist'], metadata['album'], metadata['year'], metadata['genre']])

    print(table)

def main():
    directory = input("Enter the directory containing MP3 files: ")
    mp3_files = list_mp3_files(directory)
    display_metadata(mp3_files)

if __name__ == '__main__':
    main()