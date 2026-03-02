"""
gerador_cartao_natal_ascii.py

Este script gera uma arte ASCII de uma árvore de Natal e Papai Noel.
"""

def desenhar_arvore():
    """
    Desenha uma árvore de Natal usando caracteres de texto.
    """
    arvore = [
        "    *    ",
        "   ***   ",
        "  *****  ",
        " ******* ",
        "*********",
        "   |||   ",
        "   |||   ",
        "   |||   "
    ]
    for linha in arvore:
        print(linha)

def desenhar_papai_noel():
    """
    Desenha Papai Noel usando caracteres de texto.
    """
    papai_noel = [
        "  /\\  ",
        " /  \\ ",
        "/____\\",
        " |  | ",
        " |  | ",
        " |  | ",
        " |__| ",
        " |  | ",
        " |  | ",
        " |  | ",
        " |__| "
    ]
    for linha in papai_noel:
        print(linha)

def main():
    """
    Função principal que chama as funções para desenhar a árvore e Papai Noel.
    """
    print("Feliz Natal!")
    desenhar_arvore()
    print()
    desenhar_papai_noel()

if __name__ == '__main__':
    main()