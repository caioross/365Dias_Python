"""
buscador_de_palavras_em_txt.py

Script para buscar uma palavra específica em um arquivo de texto e indicar em quais linhas ela aparece.

Uso:
    python buscador_de_palavras_em_txt.py <nome_do_arquivo> <palavra_a_buscar>
"""

import sys

def buscar_palavra_em_arquivo(nome_arquivo, palavra):
    """
    Busca uma palavra específica em um arquivo de texto e retorna as linhas onde ela aparece.

    Args:
        nome_arquivo (str): O nome do arquivo de texto a ser lido.
        palavra (str): A palavra a ser buscada no arquivo.

    Returns:
        list: Uma lista de números de linha onde a palavra aparece.
    """
    linhas_com_palavra = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                if palavra in linha:
                    linhas_com_palavra.append(numero_linha)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    return linhas_com_palavra

def main():
    if len(sys.argv) != 3:
        print("Uso: python buscador_de_palavras_em_txt.py <nome_do_arquivo> <palavra_a_buscar>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    palavra = sys.argv[2]

    linhas = buscar_palavra_em_arquivo(nome_arquivo, palavra)
    if linhas:
        print(f"A palavra '{palavra}' aparece nas seguintes linhas: {', '.join(map(str, linhas))}")
    else:
        print(f"A palavra '{palavra}' não foi encontrada no arquivo.")

if __name__ == '__main__':
    main()