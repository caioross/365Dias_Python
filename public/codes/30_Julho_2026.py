"""
extrator_texto_pdf_ocr.py

Este script converte PDFs que são imagens (scaneados) em texto pesquisável usando técnicas de OCR.
"""

import os
import pytesseract
from pdf2image import convert_from_path

def pdf_to_text(pdf_path, output_text_path):
    """
    Converte um PDF scaneado em texto usando OCR.

    Args:
        pdf_path (str): Caminho para o arquivo PDF.
        output_text_path (str): Caminho para o arquivo de texto de saída.
    """
    # Converter PDF para imagens
    images = convert_from_path(pdf_path)

    # Processar cada imagem para extrair texto
    with open(output_text_path, 'w', encoding='utf-8') as text_file:
        for page_num, image in enumerate(images):
            # Usar pytesseract para extrair texto da imagem
            text = pytesseract.image_to_string(image, lang='por')
            text_file.write(f"Página {page_num + 1}:\n{text}\n")

def main():
    """
    Função principal que executa o script.
    """
    pdf_path = 'caminho_para_seu_pdf.pdf'
    output_text_path = 'texto_extraido.txt'
    
    pdf_to_text(pdf_path, output_text_path)
    print(f"Texto extraído com sucesso e salvo em {output_text_path}")

if __name__ == '__main__':
    main()