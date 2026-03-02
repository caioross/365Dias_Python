"""
gerador_identidade_visual_ascii.py

Este script gera banners de texto estilizados usando diferentes fontes ASCII.
Ideal para cabeçalhos de scripts.

Uso:
    python gerador_identidade_visual_ascii.py "Seu Texto Aqui"
"""

import sys
from pyfiglet import Figlet

def gerar_banner(texto):
    """
    Gera um banner ASCII para o texto fornecido.

    Args:
        texto (str): O texto para o qual o banner será gerado.

    Returns:
        str: O banner ASCII gerado.
    """
    figlet = Figlet(font='slant')
    return figlet.renderText(texto)

def main():
    """
    Função principal do script.
    """
    if len(sys.argv) != 2:
        print("Uso: python gerador_identidade_visual_ascii.py \"Seu Texto Aqui\"")
        sys.exit(1)

    texto = sys.argv[1]
    banner = gerar_banner(texto)
    print(banner)

if __name__ == '__main__':
    main()