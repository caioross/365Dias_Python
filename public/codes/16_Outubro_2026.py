import re
import os

def extract_colors_from_css(file_path):
    """
    Extracts all hexadecimal and RGB color codes from a given CSS file.

    Args:
        file_path (str): The path to the CSS file.

    Returns:
        list: A list of tuples containing the color code and its line number.
    """
    colors = []
    hex_color_pattern = re.compile(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})')
    rgb_color_pattern = re.compile(r'rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            hex_colors = hex_color_pattern.findall(line)
            rgb_colors = rgb_color_pattern.findall(line)
            
            for color in hex_colors:
                colors.append((f'#{color}', line_number))
            
            for color in rgb_colors:
                colors.append((f'rgb({", ".join(color)})', line_number))
    
    return colors

def main():
    """
    Main function to execute the script.
    """
    css_file_path = 'styles.css'  # Replace with the actual CSS file path
    if not os.path.isfile(css_file_path):
        print(f"File not found: {css_file_path}")
        return
    
    colors = extract_colors_from_css(css_file_path)
    if colors:
        print("Extracted colors from CSS:")
        for color, line_number in colors:
            print(f"Color: {color}, Line: {line_number}")
    else:
        print("No colors found in the CSS file.")

if __name__ == '__main__':
    main()