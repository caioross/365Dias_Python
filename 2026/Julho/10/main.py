"""
Script para gerar padrões simétricos aleatórios de 8x8 pixels para ícones.
"""

import random

def gerar_padrao_simetrico():
    """
    Gera um padrão simétrico aleatório de 8x8 pixels.
    
    Retorna:
        list: Uma lista de listas representando o padrão 8x8.
    """
    padrao = [[random.choice([0, 1]) for _ in range(8)] for _ in range(8)]
    
    # Aplicar simetria vertical
    for i in range(8):
        for j in range(4):
            padrao[i][j] = padrao[i][7-j]
    
    # Aplicar simetria horizontal
    for i in range(4):
        for j in range(8):
            padrao[i][j] = padrao[7-i][j]
    
    return padrao

def exibir_padrao(padrao):
    """
    Exibe o padrão 8x8 no console.
    
    Args:
        padrao (list): Uma lista de listas representando o padrão 8x8.
    """
    for linha in padrao:
        print(' '.join(str(pixel) for pixel in linha))

def main():
    """
    Função principal que gera e exibe um padrão simétrico aleatório.
    """
    padrao = gerar_padrao_simetrico()
    exibir_padrao(padrao)

if __name__ == '__main__':
    main()