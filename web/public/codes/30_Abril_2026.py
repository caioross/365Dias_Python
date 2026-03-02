"""
tradutor_texto_online.py

Traduz uma frase do português para o inglês usando a biblioteca de tradução automática gratuita 'googletrans'.
"""

from googletrans import Translator

def traduzir_frase(frase):
    """
    Traduz uma frase do português para o inglês.

    Args:
        frase (str): A frase em português que deve ser traduzida.

    Returns:
        str: A frase traduzida para o inglês.
    """
    tradutor = Translator()
    traducao = tradutor.translate(frase, src='pt', dest='en')
    return traducao.text

def main():
    """
    Função principal que solicita uma frase em português ao usuário e imprime a tradução para o inglês.
    """
    frase_pt = input("Digite uma frase em português para traduzir: ")
    frase_en = traduzir_frase(frase_pt)
    print(f"Frase traduzida para inglês: {frase_en}")

if __name__ == '__main__':
    main()