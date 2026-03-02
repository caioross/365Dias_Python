"""
conversor_epub_para_pdf.py

Script para converter livros digitais no formato EPUB para arquivos PDF prontos para impressão.
"""

import os
from pathlib import Path
from typing import List

def convert_epub_to_pdf(epub_path: str, pdf_path: str) -> None:
    """
    Converte um arquivo EPUB para PDF.

    Args:
        epub_path (str): Caminho para o arquivo EPUB.
        pdf_path (str): Caminho onde o arquivo PDF será salvo.
    """
    # Aqui você adicionaria a lógica de conversão, por exemplo, usando uma biblioteca como ePUBtoPDF
    # Por enquanto, estamos apenas imprimindo uma mensagem de exemplo
    print(f"Convertendo {epub_path} para {pdf_path}")

def main() -> None:
    """
    Função principal que realiza a conversão de EPUB para PDF para todos os arquivos EPUB em um diretório.
    """
    input_directory = 'epub_books'
    output_directory = 'pdf_books'

    # Cria o diretório de saída se ele não existir
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    # Lista todos os arquivos EPUB no diretório de entrada
    epub_files = [f for f in os.listdir(input_directory) if f.endswith('.epub')]
    for epub_file in epub_files:
        epub_path = os.path.join(input_directory, epub_file)
        pdf_file = os.path.splitext(epub_file)[0] + '.pdf'
        pdf_path = os.path.join(output_directory, pdf_file)
        convert_epub_to_pdf(epub_path, pdf_path)

if __name__ == '__main__':
    main()