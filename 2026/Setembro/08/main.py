"""
buscador_precos_jogos.py

Script para comparar o preço de um jogo em diferentes lojas digitais via scraping.
"""

import requests
from bs4 import BeautifulSoup

def buscar_preco_na_loja(url):
    """
    Busca o preço de um jogo em uma loja digital a partir de uma URL.

    Args:
        url (str): A URL da página do jogo na loja digital.

    Returns:
        float: O preço do jogo ou None se não for possível encontrar.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Supondo que o preço está em uma tag <span> com a classe 'price'
        preco_tag = soup.find('span', class_='price')
        if preco_tag:
            # Removendo caracteres não numéricos e convertendo para float
            preco = float(''.join(filter(str.isdigit, preco_tag.text)))
            return preco
    except requests.RequestException as e:
        print(f"Erro ao buscar preço na URL {url}: {e}")
    return None

def comparar_precos(jogo, urls_lojas):
    """
    Compara o preço de um jogo em diferentes lojas digitais.

    Args:
        jogo (str): O nome do jogo.
        urls_lojas (dict): Um dicionário com o nome da loja como chave e a URL do jogo como valor.

    Returns:
        dict: Um dicionário com o nome da loja como chave e o preço do jogo como valor.
    """
    precos = {}
    for loja, url in urls_lojas.items():
        preco = buscar_preco_na_loja(url)
        if preco is not None:
            precos[loja] = preco
    return precos

def main():
    """
    Função principal para executar o script.
    """
    jogo = "The Legend of Zelda: Breath of the Wild"
    urls_lojas = {
        "Steam": "https://store.steampowered.com/app/258530/",
        "Epic Games": "https://www.epicgames.com/store/en-US/product/the-legend-of-zelda-breath-of-the-wild",
        "GOG": "https://www.gog.com/game/the_legend_of_zelda_breath_of_the_wild"
    }

    precos = comparar_precos(jogo, urls_lojas)
    for loja, preco in precos.items():
        print(f"Preço em {loja}: R${preco:.2f}")

if __name__ == '__main__':
    main()