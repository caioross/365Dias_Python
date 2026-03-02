import requests
from bs4 import BeautifulSoup

def extrair_tags_youtube(url):
    """
    Extrai as palavras-chave (tags) de um vídeo do YouTube a partir da URL fornecida.

    Args:
        url (str): A URL do vídeo do YouTube.

    Returns:
        list: Uma lista de tags (palavras-chave) associadas ao vídeo.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    tags = []

    # YouTube usa a classe 'keywords' para armazenar as tags
    meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
    if meta_keywords and 'content' in meta_keywords.attrs:
        tags = meta_keywords['content'].split(',')

    return tags

def main():
    url = input("Digite a URL do vídeo do YouTube: ")
    tags = extrair_tags_youtube(url)
    if tags:
        print("Tags do vídeo:")
        for tag in tags:
            print(tag.strip())
    else:
        print("Não foi possível extrair as tags do vídeo.")

if __name__ == '__main__':
    main()