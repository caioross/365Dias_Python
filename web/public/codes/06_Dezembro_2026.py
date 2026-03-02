"""
conversor_imagem_para_vetor_svg.py

Este script transforma silhuetas de imagens bitmap em caminhos vetoriais escaláveis (.svg).
"""

import sys
from PIL import Image
from svgwrite import Drawing

def bitmap_to_svg(bitmap_path, svg_path):
    """
    Converte uma imagem bitmap em um arquivo SVG.

    :param bitmap_path: Caminho para o arquivo de imagem bitmap.
    :param svg_path: Caminho para o arquivo SVG de saída.
    """
    # Abrir a imagem bitmap
    image = Image.open(bitmap_path).convert('L')  # Converter para escala de cinza
    width, height = image.size

    # Criar um novo arquivo SVG
    dwg = Drawing(svg_path, size=(f'{width}px', f'{height}px'))

    # Percorrer cada pixel da imagem
    for y in range(height):
        for x in range(width):
            if image.getpixel((x, y)) < 128:  # Considerar pixels escuros como parte da silhueta
                dwg.add(dwg.rect(insert=(x, y), size=(1, 1), fill='black'))

    # Salvar o arquivo SVG
    dwg.save()

def main():
    """
    Função principal que executa o script.
    """
    if len(sys.argv) != 3:
        print("Uso: python conversor_imagem_para_vetor_svg.py <caminho_do_bitmap> <caminho_do_svg>")
        sys.exit(1)

    bitmap_path = sys.argv[1]
    svg_path = sys.argv[2]

    try:
        bitmap_to_svg(bitmap_path, svg_path)
        print(f"Imagem convertida com sucesso para {svg_path}")
    except Exception as e:
        print(f"Erro ao converter imagem: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()