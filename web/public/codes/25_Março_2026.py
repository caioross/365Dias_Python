"""
Conversor de Markdown para HTML

Este script converte uma sintaxe básica de Markdown (# Título, Negrito) para tags HTML.
"""

import re

def markdown_to_html(markdown_text):
    """
    Converte texto Markdown para HTML.

    Args:
        markdown_text (str): O texto em formato Markdown.

    Returns:
        str: O texto convertido para HTML.
    """
    # Converter cabeçalhos
    html_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', markdown_text, flags=re.MULTILINE)
    html_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_text, flags=re.MULTILINE)
    html_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_text, flags=re.MULTILINE)

    # Converter negrito
    html_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_text)

    return html_text

def main():
    """
    Função principal que lê um arquivo Markdown, converte-o para HTML e salva o resultado.
    """
    markdown_filename = 'input.md'
    html_filename = 'output.html'

    try:
        with open(markdown_filename, 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        html_content = markdown_to_html(markdown_content)

        with open(html_filename, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print(f'Conversão concluída. O arquivo HTML foi salvo como {html_filename}.')
    except FileNotFoundError:
        print(f'O arquivo {markdown_filename} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

if __name__ == '__main__':
    main()