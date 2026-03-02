"""
conversor_heic_para_jpg.py

Script para converter arquivos HEIC (formato padrão de iPhones) para JPG em lote.
"""

import os
from PIL import Image

def converter_heic_para_jpg(diretorio):
    """
    Converte todos os arquivos HEIC em um diretório para JPG.

    Args:
        diretorio (str): Caminho para o diretório contendo os arquivos HEIC.
    """
    if not os.path.isdir(diretorio):
        raise ValueError(f"O diretório {diretorio} não existe.")

    for arquivo in os.listdir(diretorio):
        if arquivo.lower().endswith('.heic'):
            caminho_completo = os.path.join(diretorio, arquivo)
            try:
                with Image.open(caminho_completo) as img:
                    nome_base, _ = os.path.splitext(caminho_completo)
                    caminho_jpg = f"{nome_base}.jpg"
                    img.save(caminho_jpg, 'JPEG')
                    print(f"Convertido: {caminho_completo} -> {caminho_jpg}")
            except Exception as e:
                print(f"Erro ao converter {caminho_completo}: {e}")

def main():
    """
    Função principal para executar o script de conversão.
    """
    diretorio = input("Digite o caminho do diretório com os arquivos HEIC: ")
    converter_heic_para_jpg(diretorio)

if __name__ == '__main__':
    main()