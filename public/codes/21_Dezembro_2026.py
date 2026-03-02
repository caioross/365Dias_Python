"""
extrator_tags_seo_site.py

Este script analisa as tags Title, Meta Description e H1 de uma página web para verificar a otimização SEO.
"""

import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    """
    Faz uma requisição HTTP para obter o conteúdo da página.

    Args:
        url (str): A URL da página a ser analisada.

    Returns:
        str: O conteúdo HTML da página.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Erro ao buscar a página: {e}")
        return None

def parse_html_content(html_content):
    """
    Analisa o conteúdo HTML para extrair as tags Title, Meta Description e H1.

    Args:
        html_content (str): O conteúdo HTML da página.

    Returns:
        dict: Um dicionário contendo os valores das tags Title, Meta Description e H1.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title.string if soup.title else None
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_description_content = meta_description['content'] if meta_description else None
    h1 = soup.find('h1').string if soup.find('h1') else None

    return {
        'title': title,
        'meta_description': meta_description_content,
        'h1': h1
    }

def analyze_seo_tags(tags):
    """
    Analisa as tags para verificar a otimização SEO.

    Args:
        tags (dict): Um dicionário contendo os valores das tags Title, Meta Description e H1.

    Returns:
        dict: Um dicionário contendo o resultado da análise.
    """
    analysis = {
        'title_length': len(tags['title']) if tags['title'] else 0,
        'meta_description_length': len(tags['meta_description']) if tags['meta_description'] else 0,
        'h1_present': tags['h1'] is not None
    }

    return analysis

def main():
    """
    Função principal que executa o script.
    """
    url = input("Digite a URL do site a ser analisado: ")
    html_content = fetch_page_content(url)
    if html_content:
        tags = parse_html_content(html_content)
        analysis = analyze_seo_tags(tags)
        print("\nAnálise de SEO:")
        print(f"Title Length: {analysis['title_length']} caracteres")
        print(f"Meta Description Length: {analysis['meta_description_length']} caracteres")
        print(f"H1 Present: {'Sim' if analysis['h1_present'] else 'Não'}")

if __name__ == '__main__':
    main()