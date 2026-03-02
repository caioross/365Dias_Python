"""
analisador_retrospectiva_ano.py

Este script lê os logs de projetos do ano e gera um resumo de quantas linhas de código foram escritas.
"""

import os
import re

def count_lines_of_code(file_path):
    """
    Conta o número de linhas de código em um arquivo.

    Args:
        file_path (str): O caminho para o arquivo.

    Returns:
        int: O número de linhas de código no arquivo.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # Ignora linhas em branco e comentários
        return sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))

def analyze_logs(directory):
    """
    Analisa os logs de projetos em um diretório e gera um resumo de linhas de código.

    Args:
        directory (str): O diretório contendo os logs de projetos.

    Returns:
        dict: Um dicionário com o nome do arquivo e o número de linhas de código.
    """
    summary = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                lines_count = count_lines_of_code(file_path)
                summary[file] = lines_count
    return summary

def main():
    """
    Função principal que executa o script.
    """
    directory = 'logs'  # Substitua pelo diretório correto
    summary = analyze_logs(directory)
    for file, lines in summary.items():
        print(f'{file}: {lines} linhas de código')

if __name__ == '__main__':
    main()