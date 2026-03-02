"""
gerador_nomes_bebes.py

Este script sugere nomes de bebês baseados em tendências de anos anteriores e significados.
"""

import random

def carregar_nomes_de_arquivo(caminho_arquivo):
    """
    Carrega nomes de bebês de um arquivo de texto.

    Args:
        caminho_arquivo (str): O caminho para o arquivo de texto contendo nomes de bebês.

    Returns:
        list: Uma lista de nomes de bebês.
    """
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        nomes = arquivo.readlines()
    return [nome.strip() for nome in nomes]

def sugerir_nome(nomes):
    """
    Sugere um nome de bebê aleatório da lista fornecida.

    Args:
        nomes (list): Uma lista de nomes de bebês.

    Returns:
        str: Um nome de bebê sugerido.
    """
    if not nomes:
        return "Não há nomes disponíveis."
    return random.choice(nomes)

def main():
    """
    Função principal que carrega nomes de bebês e sugere um nome aleatório.
    """
    caminho_arquivo = 'nomes_bebes.txt'
    nomes_bebes = carregar_nomes_de_arquivo(caminho_arquivo)
    nome_sugerido = sugerir_nome(nomes_bebes)
    print(f"Nome sugerido: {nome_sugerido}")

if __name__ == '__main__':
    main()