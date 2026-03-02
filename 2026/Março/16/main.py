def convert_to_uppercase(file_path):
    """
    Converte todo o conteúdo de um arquivo de texto para letras maiúsculas.

    Args:
        file_path (str): O caminho para o arquivo de texto que será convertido.

    Returns:
        str: O conteúdo do arquivo convertido para maiúsculas.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content.upper()
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao ler o arquivo: {e}")

def write_to_file(file_path, content):
    """
    Escreve o conteúdo fornecido em um arquivo de texto.

    Args:
        file_path (str): O caminho para o arquivo onde o conteúdo será escrito.
        content (str): O conteúdo que será escrito no arquivo.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao escrever no arquivo: {e}")

def main():
    """
    Função principal que lê um arquivo de texto, converte seu conteúdo para maiúsculas
    e escreve o resultado em um novo arquivo.
    """
    input_file_path = 'input.txt'  # Caminho para o arquivo de entrada
    output_file_path = 'output.txt'  # Caminho para o arquivo de saída

    try:
        uppercase_content = convert_to_uppercase(input_file_path)
        write_to_file(output_file_path, uppercase_content)
        print(f"O conteúdo foi convertido e salvo em {output_file_path}.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()