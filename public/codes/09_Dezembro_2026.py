"""
Script para converter texto em áudio com opção de escolher sotaques e vozes de diferentes países.
"""

import pyttsx3
from pyttsx3 import engine

def configurar_engine(idioma: str) -> engine.Engine:
    """
    Configura o motor de fala para o idioma especificado.

    Args:
        idioma (str): O código do idioma para o qual configurar o motor de fala.

    Returns:
        engine.Engine: O motor de fala configurado.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if idioma in voice.languages:
            engine.setProperty('voice', voice.id)
            break
    else:
        raise ValueError(f"Idioma '{idioma}' não suportado ou não encontrado.")
    return engine

def falar_texto(texto: str, idioma: str) -> None:
    """
    Converte o texto fornecido em áudio usando o idioma especificado.

    Args:
        texto (str): O texto a ser convertido em áudio.
        idioma (str): O código do idioma para a fala.
    """
    try:
        engine = configurar_engine(idioma)
        engine.say(texto)
        engine.runAndWait()
    except Exception as e:
        print(f"Erro ao falar texto: {e}")

def main():
    """
    Função principal que executa o script.
    """
    texto = input("Digite o texto que deseja falar: ")
    idioma = input("Digite o código do idioma (por exemplo, 'pt-br' para português do Brasil): ")
    falar_texto(texto, idioma)

if __name__ == '__main__':
    main()