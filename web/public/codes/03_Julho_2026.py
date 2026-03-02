"""
buscador_letras_musicas.py

Script para buscar a letra de uma música informando o nome do artista e da canção.
"""

import requests

def buscar_letra_artista_cancao(artista, cancao):
    """
    Busca a letra de uma música informando o nome do artista e da canção.

    Args:
        artista (str): Nome do artista.
        cancao (str): Nome da canção.

    Returns:
        str: A letra da música ou uma mensagem de erro se não encontrar.
    """
    url = f"https://api.vagalume.com.br/search.php?art={artista}&mus={cancao}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'success':
            letra = data['response']['mus'][0]['text']
            return letra
        else:
            return "Música não encontrada."
    else:
        return "Erro ao buscar a letra da música."

def main():
    """
    Função principal que solicita ao usuário o nome do artista e da canção,
    e exibe a letra da música.
    """
    artista = input("Digite o nome do artista: ")
    cancao = input("Digite o nome da canção: ")
    
    letra = buscar_letra_artista_cancao(artista, cancao)
    print(letra)

if __name__ == '__main__':
    main()