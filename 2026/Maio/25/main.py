"""
conversor_pdf_para_txt.py

Script para converter o conteúdo textual de um arquivo PDF para um arquivo de texto simples (.txt).
"""

import PyPDF2

def pdf_to_text(pdf_path, txt_path):
    """
    Converte o conteúdo textual de um arquivo PDF para um arquivo de texto simples (.txt).

    Args:
        pdf_path (str): Caminho para o arquivo PDF de entrada.
        txt_path (str): Caminho para o arquivo de texto de saída.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"

    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    """
    Função principal que executa a conversão de PDF para TXT.
    """
    pdf_path = 'input.pdf'  # Caminho para o arquivo PDF de entrada
    txt_path = 'output.txt'  # Caminho para o arquivo de texto de saída
    pdf_to_text(pdf_path, txt_path)
    print(f"Conversão concluída. O arquivo de texto foi salvo em {txt_path}")

if __name__ == '__main__':
    main()