"""
extrator_texto_imagem_ocr.py

Este script utiliza OCR (Reconhecimento Óptico de Caracteres) para ler texto de fotos de documentos ou capturas de tela.
Requisitos: Tesseract OCR deve estar instalado e configurado no sistema.
"""

import pytesseract
from PIL import Image

def extrair_texto_imagem(caminho_imagem):
    """
    Extrai texto de uma imagem utilizando OCR.

    Args:
        caminho_imagem (str): O caminho para o arquivo de imagem.

    Returns:
        str: Texto extraído da imagem.
    """
    try:
        # Abre a imagem usando a biblioteca PIL
        imagem = Image.open(caminho_imagem)
        
        # Usa o Tesseract OCR para extrair texto da imagem
        texto = pytesseract.image_to_string(imagem)
        
        return texto
    except Exception as e:
        print(f"Erro ao extrair texto da imagem: {e}")
        return None

def main():
    """
    Função principal que executa o script.
    """
    caminho_imagem = input("Digite o caminho para a imagem: ")
    texto_extraido = extrair_texto_imagem(caminho_imagem)
    
    if texto_extraido:
        print("Texto extraído da imagem:")
        print(texto_extraido)
    else:
        print("Não foi possível extrair texto da imagem.")

if __name__ == '__main__':
    main()