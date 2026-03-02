import PyPDF2
from PyPDF2 import PdfReader

def extrair_texto_de_intervalo_de_paginas(pdf_path, start_page, end_page):
    """
    Extrai o texto de um intervalo de páginas especificado de um arquivo PDF.

    Args:
        pdf_path (str): Caminho para o arquivo PDF.
        start_page (int): Página inicial (inclusiva).
        end_page (int): Página final (inclusiva).

    Returns:
        str: Texto extraído das páginas especificadas.
    """
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page_num in range(start_page - 1, end_page):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def main():
    pdf_path = input("Digite o caminho para o arquivo PDF: ")
    start_page = int(input("Digite a página inicial: "))
    end_page = int(input("Digite a página final: "))
    
    try:
        texto_extraido = extrair_texto_de_intervalo_de_paginas(pdf_path, start_page, end_page)
        print("Texto extraído das páginas especificadas:")
        print(texto_extraido)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()