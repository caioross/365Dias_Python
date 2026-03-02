"""
extrator_comentarios_instagram.py

Script para extrair comentários de um post específico do Instagram
para fins de sorteios ou análise.

Este script utiliza a biblioteca instaloader para realizar o scraping.
Certifique-se de ter a biblioteca instalada (`pip install instaloader`) e
de estar logado em uma conta do Instagram.

Uso:
    python extrator_comentarios_instagram.py <username> <post_url> <output_file>

Exemplo:
    python extrator_comentarios_instagram.py usuario https://www.instagram.com/p/C0a1b2c3/ comentarios.txt
"""

import sys
import instaloader

def extrair_comentarios(username, post_url, output_file):
    """
    Extrai comentários de um post do Instagram e salva em um arquivo.

    :param username: Nome de usuário do Instagram.
    :param post_url: URL do post do Instagram.
    :param output_file: Nome do arquivo onde os comentários serão salvos.
    """
    # Inicializa o instaloader
    L = instaloader.Instaloader()

    # Faz login no Instagram (necessário para acessar posts privados)
    L.login(username, input("Digite sua senha do Instagram: "))

    # Baixa o post
    post = instaloader.Post.from_shortcode(L.context, post_url.split('/')[-2])

    # Abre o arquivo de saída
    with open(output_file, 'w', encoding='utf-8') as file:
        for comment in post.get_comments():
            file.write(f"{comment.owner.username}: {comment.text}\n")

def main():
    if len(sys.argv) != 4:
        print("Uso: python extrator_comentarios_instagram.py <username> <post_url> <output_file>")
        sys.exit(1)

    username = sys.argv[1]
    post_url = sys.argv[2]
    output_file = sys.argv[3]

    extrair_comentarios(username, post_url, output_file)
    print(f"Comentários extraídos e salvos em {output_file}")

if __name__ == '__main__':
    main()