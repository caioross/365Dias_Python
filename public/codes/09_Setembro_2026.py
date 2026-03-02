"""
conversor_texto_fala_offline.py

Este script converte texto em fala usando a biblioteca pyttsx3, que não depende de conexão com a internet.
"""

import pyttsx3

def falar(texto):
    """
    Converte o texto fornecido em fala.

    Args:
        texto (str): O texto que será convertido em fala.
    """
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def main():
    """
    Função principal que solicita ao usuário um texto e o converte em fala.
    """
    texto = input("Digite o texto que deseja converter em fala: ")
    falar(texto)

if __name__ == '__main__':
    main()