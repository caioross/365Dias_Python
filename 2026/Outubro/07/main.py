import os

def get_user_input(prompt):
    """Prompt the user for input and return the response."""
    return input(prompt).strip()

def generate_readme_content():
    """Generate the content for the README.md file based on user input."""
    project_name = get_user_input("Enter the project name: ")
    description = get_user_input("Enter a brief description of the project: ")
    installation = get_user_input("Enter the installation instructions: ")
    usage = get_user_input("Enter the usage instructions: ")
    contributing = get_user_input("Enter the contribution guidelines: ")
    license = get_user_input("Enter the license type: ")

    readme_content = f"""# {project_name}

## Description
{description}

## Installation
{installation}

## Usage
{usage}

## Contributing
{contributing}

## License
This project is licensed under the {license} License.
"""

    return readme_content

def write_readme_file(content):
    """Write the generated content to a README.md file."""
    with open("README.md", "w") as file:
        file.write(content)
    print("README.md file has been created successfully.")

def main():
    """Main function to execute the script."""
    print("Welcome to the README.md Generator!")
    readme_content = generate_readme_content()
    write_readme_file(readme_content)

if __name__ == '__main__':
    main()