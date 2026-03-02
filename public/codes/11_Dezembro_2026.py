import json
from typing import Any, Dict, List

def generate_model_class(json_data: Dict[str, Any], class_name: str) -> str:
    """
    Generates a Python class from a JSON data structure.

    Args:
        json_data (Dict[str, Any]): The JSON data to be converted into a class.
        class_name (str): The name of the class to be generated.

    Returns:
        str: The generated Python class as a string.
    """
    class_definition = f"class {class_name}:\n"
    for key, value in json_data.items():
        if isinstance(value, dict):
            nested_class_name = key.capitalize()
            nested_class = generate_model_class(value, nested_class_name)
            class_definition += f"    {nested_class_name} = {nested_class_name}\n"
            class_definition += f"    {key}: {nested_class_name}\n"
        elif isinstance(value, list):
            if value and isinstance(value[0], dict):
                item_class_name = f"{key.capitalize()}Item"
                item_class = generate_model_class(value[0], item_class_name)
                class_definition += f"    {item_class_name} = {item_class_name}\n"
                class_definition += f"    {key}: List[{item_class_name}]\n"
            else:
                class_definition += f"    {key}: List[{type(value[0]).__name__ if value else 'Any'}]\n"
        else:
            class_definition += f"    {key}: {type(value).__name__}\n"
    return class_definition

def main():
    """
    Main function to generate Python model classes from a JSON file.
    """
    try:
        with open('api_response.json', 'r') as file:
            json_data = json.load(file)
        
        class_name = "APIResponseModel"
        generated_class = generate_model_class(json_data, class_name)
        
        print(generated_class)
        
    except FileNotFoundError:
        print("Error: The file 'api_response.json' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")

if __name__ == '__main__':
    main()