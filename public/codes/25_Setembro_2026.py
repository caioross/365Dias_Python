import requests
from bs4 import BeautifulSoup
import re

def extrair_links_playlist(url_playlist):
    """
    Extrai os títulos e URLs dos vídeos de uma playlist do YouTube.

    Args:
        url_playlist (str): O URL da playlist do YouTube.

    Returns:
        list: Uma lista de dicionários contendo o título e a URL de cada vídeo.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url_playlist, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    videos = []
    for video in soup.select('a#video-title'):
        title = video.get_text()
        link = f"https://www.youtube.com{video['href']}"
        videos.append({'title': title, 'url': link})
    
    return videos

def salvar_links_em_arquivo(videos, nome_arquivo='links_playlist.txt'):
    """
    Salva os títulos e URLs dos vídeos em um arquivo de texto.

    Args:
        videos (list): A lista de vídeos com títulos e URLs.
        nome_arquivo (str): O nome do arquivo onde os links serão salvos.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for video in videos:
            arquivo.write(f"Título: {video['title']}\n")
            arquivo.write(f"URL: {video['url']}\n\n")

def main():
    url_playlist = input("Digite o URL da playlist do YouTube: ")
    videos = extrair_links_playlist(url_playlist)
    salvar_links_em_arquivo(videos)
    print(f"Links salvos em 'links_playlist.txt'.")

if __name__ == '__main__':
    main()