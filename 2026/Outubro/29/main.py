"""
gerador_meme_terminal.py

Este script permite adicionar textos em cima de templates de imagens famosas usando a biblioteca Pillow.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def adicionar_texto_na_imagem(template_path, texto_superior, texto_inferior, output_path):
    """
    Adiciona textos em cima de um template de imagem.

    :param template_path: Caminho para o arquivo de imagem template.
    :param texto_superior: Texto a ser adicionado no topo da imagem.
    :param texto_inferior: Texto a ser adicionado na base da imagem.
    :param output_path: Caminho onde a imagem resultante será salva.
    """
    # Carrega a imagem template
    imagem = Image.open(template_path)
    draw = ImageDraw.Draw(imagem)

    # Define a fonte
    fonte = ImageFont.truetype("arial.ttf", 36)  # Certifique-se de que a fonte está disponível

    # Calcula as posições dos textos
    largura, altura = imagem.size
    texto_superior_largura, texto_superior_altura = draw.textsize(texto_superior, font=fonte)
    texto_inferior_largura, texto_inferior_altura = draw.textsize(texto_inferior, font=fonte)

    # Posiciona os textos
    posicao_superior = ((largura - texto_superior_largura) / 2, 10)
    posicao_inferior = ((largura - texto_inferior_largura) / 2, altura - texto_inferior_altura - 10)

    # Adiciona os textos à imagem
    draw.text(posicao_superior, texto_superior, (255, 255, 255), font=fonte)
    draw.text(posicao_inferior, texto_inferior, (255, 255, 255), font=fonte)

    # Salva a imagem resultante
    imagem.save(output_path)

def main():
    """
    Função principal que executa o script.
    """
    template_path = "template.jpg"  # Substitua pelo caminho do seu template
    texto_superior = "Texto Superior"
    texto_inferior = "Texto Inferior"
    output_path = "meme_resultante.jpg"

    adicionar_texto_na_imagem(template_path, texto_superior, texto_inferior, output_path)
    print(f"Imagem gerada com sucesso em {output_path}")

if __name__ == '__main__':
    main()