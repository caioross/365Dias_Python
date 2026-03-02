import os
from PIL import Image, ImageDraw, ImageFont

def gerar_avatar(iniciais, cor_fundo, cor_texto, tamanho=200):
    """
    Gera um avatar PNG com as iniciais do usuário no centro.

    :param iniciais: As iniciais do usuário a serem exibidas no avatar.
    :param cor_fundo: A cor do fundo do avatar em formato RGB.
    :param cor_texto: A cor do texto (iniciais) em formato RGB.
    :param tamanho: O tamanho da imagem em pixels (altura e largura).
    :return: Caminho para o arquivo de imagem gerado.
    """
    # Cria uma nova imagem com o tamanho especificado e a cor de fundo
    avatar = Image.new('RGB', (tamanho, tamanho), cor_fundo)
    draw = ImageDraw.Draw(avatar)

    # Define a fonte e o tamanho do texto
    font = ImageFont.truetype('arial.ttf', int(tamanho * 0.5))
    
    # Calcula a posição do texto para centralizá-lo
    text_width, text_height = draw.textsize(iniciais, font=font)
    position = ((tamanho - text_width) / 2, (tamanho - text_height) / 2)

    # Desenha o texto no centro da imagem
    draw.text(position, iniciais, font=font, fill=cor_texto)

    # Define o nome do arquivo
    filename = f'avatar_{iniciais}.png'
    
    # Salva a imagem
    avatar.save(filename)
    
    return filename

def main():
    """
    Função principal que gera um avatar com as iniciais do usuário.
    """
    iniciais = input("Digite as iniciais do usuário: ")
    cor_fundo = input("Digite a cor do fundo (ex: 255, 0, 0 para vermelho): ")
    cor_texto = input("Digite a cor do texto (ex: 0, 0, 255 para azul): ")

    # Converte as cores de string para tuplas de inteiros
    cor_fundo = tuple(map(int, cor_fundo.split(',')))
    cor_texto = tuple(map(int, cor_texto.split(',')))

    # Gera o avatar
    arquivo_avatar = gerar_avatar(iniciais, cor_fundo, cor_texto)
    print(f"Avatar gerado com sucesso: {arquivo_avatar}")

if __name__ == '__main__':
    main()