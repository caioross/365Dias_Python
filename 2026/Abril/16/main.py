"""
Script para remover o fundo de uma imagem utilizando a biblioteca rembg.
Requisitos:
    pip install rembg
    pip install pillow
"""

from rembg import remove
from PIL import Image
import sys

def remover_fundo(input_path, output_path):
    """
    Remove o fundo de uma imagem e salva a imagem resultante.

    :param input_path: Caminho para a imagem de entrada.
    :param output_path: Caminho para salvar a imagem de saída.
    """
    with Image.open(input_path) as img:
        output = remove(img)
        output.save(output_path)

def main():
    if len(sys.argv) != 3:
        print("Uso: python remover_fundo_imagem.py <caminho_da_imagem_entrada> <caminho_da_imagem_saida>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        remover_fundo(input_path, output_path)
        print(f"Fundo removido com sucesso. Imagem salva em {output_path}")
    except Exception as e:
        print(f"Erro ao remover fundo: {e}")

if __name__ == '__main__':
    main()