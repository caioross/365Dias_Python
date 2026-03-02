"""
Script para contar o número de linhas de código em um arquivo Python,
ignorando comentários e linhas em branco.
"""

import sys

def contar_linhas_codigo(arquivo):
    """
    Conta o número de linhas de código em um arquivo Python,
    ignorando comentários e linhas em branco.

    :param arquivo: Caminho para o arquivo Python.
    :return: Número de linhas de código.
    """
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
        return 0
    except IOError:
        print(f"Erro ao ler o arquivo {arquivo}.")
        return 0

    count = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#'):
            count += 1

    return count

def main():
    """
    Função principal que executa o script.
    """
    if len(sys.argv) != 2:
        print("Uso: python contador_linhas_codigo.py <caminho_do_arquivo>")
        sys.exit(1)

    arquivo = sys.argv[1]
    numero_de_linhas = contar_linhas_codigo(arquivo)
    print(f"O arquivo {arquivo} tem {numero_de_linhas} linhas de código.")

if __name__ == '__main__':
    main()