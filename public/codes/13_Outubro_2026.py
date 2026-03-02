```python
import re

def validate_postal_code(postal_code: str, country_code: str) -> bool:
    """
    Validates the format of a postal code based on the country code.

    Args:
        postal_code (str): The postal code to validate.
        country_code (str): The ISO 3166-1 alpha-2 country code.

    Returns:
        bool: True if the postal code is valid, False otherwise.
    """
    postal_code_masks = {
        'US': r'^\d{5}(-\d{4})?$',
        'BR': r'^\d{5}-\d{3}$',
        'CA': r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$',
        'UK': r'^[A-Za-z]{1,2}\d[A-Za-z\d]?\s?\d[A-Za-z]{2}$',
        'DE': r'^\d{5}$',
        'FR': r'^\d{5}$',
        'JP': r'^\d{3}-\d{4}$',
        'AU': r'^\d{4}$',
        'IN': r'^\d{6}$',
        'ZA': r'^\d{4}$',
        'ES': r'^\d{5}$',
        'IT': r'^\d{5}$',
        'NL': r'^\d{4}\s?[A-Za-z]{2}$',
        'SE': r'^\d{3}\s?\d{2}$',
        'CH': r'^\d{4}$',
        'AT': r'^\d{4}$',
        'BE': r'^\d{4}$',
        'DK': r'^\d{4}$',
        'FI': r'^\d{5}$',
        'NO': r'^\d{4}$',
        'PL': r'^\d{2}-\d{3}$',
        'RU': r'^\d{6}$',
        'CN': r'^\d{6}$',
        'MX': r'^\d{5}$',
        'AR': r'^\d{4}\s?\d{4}$',
        'CL': r'^\d{7}$',
        'CO': r'^\d{6}$',
        'PE': r'^\d{5}$',
        'VE': r'^\d{4}$',
        'ZA': r'^\d{4}$',
        'NG': r'^\d{6}$',
        'KE': r'^\d{5}$',
        'EG': r'^\d{5}$',
        'SA': r'^\d{5}$',
        'AE': r'^\d{5}$',
        'QA': r'^\d{5}$',
        'BH': r'^\d{5}$',
        'OM': r'^\d{5}$',
        'KW': r'^\d{5}$',
        'QA': r'^\d{5}$',
        'JO': r'^\d{5}$',
        'LB': r'^\d{4}-\d{4}$',
        'SY': r'^\d{5}$',
        'YE': r'^\d{5}$',
        'IR': r'^\d{5}$',
        'TR': r'^\d{5}$',
        'PK': r'^\d{5}$',
        'BD': r'^\d{4}$',
        'MM': r'^\d{5}$',
        'PH': r'^\d{4}$',
        'SG': r'^\d{6}$',
        'TH': r'^\d{5}$',
        'VN': r'^\d{6}$',
        'ID': r'^\d{5}$',
        'MY': r'^\d{5}$',
        'AU': r'^\d{4}$',
        'NZ': r'^\d{4}$',
        'CA': r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$',
        'ZA': r'^\d{4}$',
        'IN': r'^\d{6}$',
        'NG': r'^\d{6}$',
        'KE': r'^\d{5}$',
        'EG': r'^\d{5}$',
        'SA': r'^\d{5}$',
        'AE': r'^\d{5}$',
        'QA': r'^\d{5}$',
        'BH': r'^\d{5}$',
        'OM': r'^\d{5}$',
        'KW': r'^\d{5}$',
        'QA': r'^\d{5}$',
        'JO': r'^\d{5}$',
        'LB': r'^\d{4}-\d{4}$',
        'SY': r'^\d{5}$',
        'YE': r'^\d{5}$',
        'IR': r'^\d{5}$',
        'TR': r'^\d{5}$',
        'PK': r'^\d{5}$',
        'BD': r'^\d{4}$',
        'MM': r'^\d{5}$',
        'PH': r'^\d{4}$',
        'SG': r'^\d{6}$',
        'TH': r'^\d{5}$',
        'VN': r'^\d{6}$',
        'ID': r'^\d{5}$',
        'MY': r'^\d{5}$',
        'AU': r'^\d{4}$',
        'NZ': r'^\d{4}$',
    }

    mask = postal_code_masks.get(country_code.upper())
    if not mask:
        raise ValueError(f"Country code {country_code} is not supported.")

    return bool(re.match(mask, postal_code))

def main():
    """
    Main function to test the validate_postal_code function.
    """
    test_cases = [
        ('12345', 'US'),  # Valid US ZIP Code
        ('12345-6789', 'US'),  # Valid US ZIP Code with extension
        ('00000-000', 'BR'),  # Valid Brazilian ZIP Code
        ('M4B 1A1', 'CA'),  # Valid Canadian ZIP Code
        ('W1A 0AX', 'UK'),  # Valid UK ZIP Code
        ('12345', 'DE'),  # Valid German ZIP Code
        ('12345', 'FR'),  # Valid French ZIP Code
        ('123-4567', 'JP'),  # Valid Japanese ZIP Code
        ('2000', 'AU'),  # Valid Australian ZIP Code
        ('123456', 'IN'),  # Valid Indian ZIP Code
        ('1234', 'ZA'),  # Valid South African ZIP Code
        ('12345', 'ES'),  # Valid Spanish ZIP Code
        ('12345', 'IT'),  # Valid Italian ZIP Code
        ('1234 AB', 'NL'),  # Valid Dutch ZIP Code
        ('123 45', 'SE'),  # Valid Swedish ZIP Code
        ('1234', 'CH'),  # Valid Swiss ZIP Code
        ('1234', 'AT'),  # Valid Austrian ZIP Code
        ('1234', 'BE'),  # Valid Belgian ZIP Code
        ('1234', 'DK'),  # Valid Danish ZIP Code
        ('12345', 'FI'),  # Valid Finnish ZIP Code
        ('1234', 'NO'),  # Valid Norwegian ZIP Code
        ('12-345', 'PL'),  # Valid Polish ZIP Code
        ('123456', 'RU'),  # Valid Russian ZIP Code
        ('123456', 'CN'),  # Valid Chinese ZIP Code
        ('12345', 'MX'),  # Valid Mexican ZIP Code
        ('1234 1234', 'AR'),  # Valid Argentine ZIP Code
        ('1234567', 'CL'),  # Valid Chilean ZIP Code
        ('123456', 'CO'),  # Valid Colombian ZIP Code
        ('12345', 'PE'),  # Valid Peruvian ZIP Code
        ('1234', 'VE'),  # Valid Venezuelan ZIP Code
        ('1234', 'NG'),  # Valid Nigerian ZIP Code
        ('12345', 'KE'),  # Valid Kenyan ZIP Code
        ('12345', 'EG'),  # Valid Egyptian ZIP Code
        ('12345', 'SA'),  # Valid Saudi Arabian ZIP Code
        ('12345', 'AE'),  # Valid United Arab Emirates ZIP Code
        ('12345', 'QA'),  # Valid Qatari ZIP Code
        ('12345', 'BH'),  # Valid Bahraini ZIP Code
        ('12345', 'OM'),  # Valid Omani ZIP Code
        ('12345', 'KW'),  # Valid Kuwaiti ZIP Code
        ('1