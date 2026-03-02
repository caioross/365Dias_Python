import sys

def remove_blank_lines(input_file, output_file):
    """
    Remove blank lines from the input file and writes the result to the output file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file where the result will be saved.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file_in:
            lines = file_in.readlines()

        non_blank_lines = [line for line in lines if line.strip()]

        with open(output_file, 'w', encoding='utf-8') as file_out:
            file_out.writelines(non_blank_lines)

        print(f"Blank lines removed. Output saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 3:
        print("Usage: python filtro_linhas_vazias.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    remove_blank_lines(input_file, output_file)

if __name__ == '__main__':
    main()