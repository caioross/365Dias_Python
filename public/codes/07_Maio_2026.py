"""
Gerador de Capa de Livro Digital

Este script cria uma imagem JPG simples com um título e autor centralizados.
É útil para gerar capas provisórias de livros digitais.

Uso:
python gerador_capa_livro_digital.py --titulo "Título do Livro" --autor "Nome do Autor"
"""

import argparse
from PIL import Image, ImageDraw, ImageFont

def criar_capa(titulo, autor, largura=600, altura=900):
    """
    Cria uma imagem de capa com o título e autor centralizados.

    :param titulo: Título do livro.
    :param autor: Nome do autor.
    :param largura: Largura da imagem em pixels.
    :param altura: Altura da imagem em pixels.
    :return: Um objeto Image da biblioteca PIL.
    """
    # Cria uma imagem branca
    capa = Image.new('RGB', (largura, altura), color='white')
    draw = ImageDraw.Draw(capa)

    # Define a fonte
    font_titulo = ImageFont.truetype("arial.ttf", 40)
    font_autor = ImageFont.truetype("arial.ttf", 30)

    # Calcula a posição central do título
    text_width, text_height = draw.textsize(titulo, font=font_titulo)
    pos_titulo = ((largura - text_width) / 2, (altura - text_height) / 2 - 50)

    # Calcula a posição central do autor
    text_width, text_height = draw.textsize(autor, font=font_autor)
    pos_autor = ((largura - text_width) / 2, (altura - text_height) / 2 + 50)

    # Desenha o título e o autor
    draw.text(pos_titulo, titulo, font=font_titulo, fill='black')
    draw.text(pos_autor, autor, font=font_autor, fill='black')

    return capa

def main():
    """
    Função principal que processa os argumentos da linha de comando e cria a capa.
    """
    parser = argparse.ArgumentParser(description='Cria uma imagem de capa de livro digital.')
    parser.add_argument('--titulo', required=True, help='Título do livro')
    parser.add_argument('--autor', required=True, help='Nome do autor')

    args = parser.parse_args()

    capa = criar_capa(args.titulo, args.autor)
    capa.save('capa_livro.jpg')
    print("Capa criada com sucesso: capa_livro.jpg")

if __name__ == '__main__':
    main()