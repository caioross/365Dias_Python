"""
Script para gerar um mapa de calor no terminal usando diferentes tons de cores de fundo.
"""

import sys

def print_colored_char(char, color_code):
    """
    Imprime um caractere com um código de cor de fundo específico.

    :param char: O caractere a ser impresso.
    :param color_code: O código de cor ANSI para o fundo.
    """
    print(f"\033[48;5;{color_code}m{char}\033[0m", end='')

def generate_heatmap(data, min_val, max_val, char='█'):
    """
    Gera um mapa de calor no terminal com base nos dados fornecidos.

    :param data: Uma lista de listas contendo os valores numéricos a serem representados.
    :param min_val: O valor mínimo na escala de cores.
    :param max_val: O valor máximo na escala de cores.
    :param char: O caractere usado para representar cada valor.
    """
    for row in data:
        for value in row:
            # Normaliza o valor para a escala de 0 a 255
            normalized_value = int(((value - min_val) / (max_val - min_val)) * 255)
            # Escolhe um código de cor de fundo baseado no valor normalizado
            color_code = min(15, normalized_value // 17)  # Limita a 16 cores
            print_colored_char(char, color_code)
        print()  # Nova linha após cada linha de dados

def main():
    """
    Função principal que gera um mapa de calor com dados de exemplo.
    """
    # Dados de exemplo
    data = [
        [0, 50, 100, 150, 200],
        [200, 150, 100, 50, 0],
        [50, 100, 150, 200, 250],
        [250, 200, 150, 100, 50]
    ]
    
    min_val = 0
    max_val = 250
    
    generate_heatmap(data, min_val, max_val)

if __name__ == '__main__':
    main()