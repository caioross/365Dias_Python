"""
conversor_docx_para_pdf.py

Script para converter arquivos .docx para .pdf mantendo a formatação básica.
"""

import os
from docx2pdf import convert

def converter_docx_para_pdf(caminho_docx, caminho_pdf):
    """
    Converte um arquivo .docx para .pdf.

    Args:
        caminho_docx (str): Caminho para o arquivo .docx.
        caminho_pdf (str): Caminho onde o arquivo .pdf será salvo.
    """
    try:
        convert(caminho_docx, caminho_pdf)
        print(f"Conversão concluída: {caminho_pdf}")
    except Exception as e:
        print(f"Erro ao converter: {e}")

def main():
    """
    Função principal que realiza a conversão de .docx para .pdf.
    """
    caminho_docx = input("Digite o caminho do arquivo .docx: ")
    nome_arquivo = os.path.splitext(os.path.basename(caminho_docx))[0]
    caminho_pdf = os.path.join(os.path.dirname(caminho_docx), f"{nome_arquivo}.pdf")
    
    converter_docx_para_pdf(caminho_docx, caminho_pdf)

if __name__ == '__main__':
    main()