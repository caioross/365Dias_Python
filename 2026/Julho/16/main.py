import pyperclip
import re

def extract_plain_text(formatted_text):
    """
    Extracts plain text from formatted text by removing special characters and extra spaces.

    Args:
        formatted_text (str): The text with formatting to be converted to plain text.

    Returns:
        str: The plain text extracted from the formatted text.
    """
    # Remove special characters and extra spaces
    plain_text = re.sub(r'\s+', ' ', formatted_text)
    plain_text = re.sub(r'[^\w\s]', '', plain_text)
    return plain_text.strip()

def main():
    """
    Main function to execute the script. It captures text from the clipboard,
    extracts plain text, and prints it.
    """
    # Capture text from clipboard
    clipboard_text = pyperclip.paste()
    
    # Extract plain text
    plain_text = extract_plain_text(clipboard_text)
    
    # Print the plain text
    print("Plain Text:")
    print(plain_text)

if __name__ == '__main__':
    main()