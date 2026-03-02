import re

def extract_links_from_markdown(file_path):
    """
    Extrai todos os links e seus respectivos textos âncora de um arquivo Markdown.

    Args:
        file_path (str): O caminho para o arquivo Markdown.

    Returns:
        list: Uma lista de tuplas contendo o texto âncora e a URL do link.
    """
    link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
    links = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = link_pattern.findall(content)
            links.extend(matches)
    except FileNotFoundError:
        print(f"O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

    return links

def main():
    """
    Função principal que executa o script de extração de links.
    """
    file_path = 'example.md'  # Substitua pelo caminho do seu arquivo Markdown
    links = extract_links_from_markdown(file_path)

    if links:
        print("Links extraídos do arquivo Markdown:")
        for anchor_text, url in links:
            print(f"Texto âncora: {anchor_text}, URL: {url}")
    else:
        print("Nenhum link foi encontrado no arquivo.")

if __name__ == '__main__':
    main()