"""
gerador_tabuleiro_xadrez.py

Este script gera uma representação visual ou em texto de um tabuleiro de xadrez.
"""

def gerar_tabuleiro(tamanho=8):
    """
    Gera uma representação de um tabuleiro de xadrez.

    Args:
        tamanho (int): O tamanho do tabuleiro (padrão é 8x8).

    Returns:
        str: Uma string representando o tabuleiro de xadrez.
    """
    tabuleiro = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if (i + j) % 2 == 0:
                linha.append(' ')
            else:
                linha.append('#')
        tabuleiro.append(' '.join(linha))
    return '\n'.join(tabuleiro)

def main():
    """
    Função principal que gera e imprime um tabuleiro de xadrez.
    """
    tabuleiro = gerar_tabuleiro()
    print(tabuleiro)

if __name__ == '__main__':
    main()