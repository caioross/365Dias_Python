import requests
from typing import Dict

def detect_language(text: str) -> Dict[str, str]:
    """
    Detects the language of the given text using the Google Cloud Translation API.

    Args:
        text (str): The text to detect the language of.

    Returns:
        Dict[str, str]: A dictionary containing the detected language code and name.
    """
    url = "https://translation.googleapis.com/language/translate/v2/detect"
    params = {
        "q": text,
        "key": "YOUR_GOOGLE_CLOUD_API_KEY"  # Replace with your actual API key
    }
    response = requests.post(url, data=params)
    response.raise_for_status()
    result = response.json()
    detection = result['data']['detections'][0][0]
    return {
        "language_code": detection['language'],
        "language_name": detection['name']
    }

def main():
    """
    Main function to execute the language detection script.
    """
    sample_text = "Hello, how are you?"
    try:
        language_info = detect_language(sample_text)
        print(f"Detected Language Code: {language_info['language_code']}")
        print(f"Detected Language Name: {language_info['language_name']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()