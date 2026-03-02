"""
Script para baixar a legenda de um vídeo do YouTube.
"""

import os
import sys
from pytube import YouTube

def baixar_legenda(url, idioma='pt'):
    """
    Baixa a legenda de um vídeo do YouTube.

    Args:
        url (str): URL do vídeo do YouTube.
        idioma (str): Código do idioma da legenda (padrão 'pt' para português).

    Returns:
        str: Caminho do arquivo de legenda baixado.
    """
    try:
        yt = YouTube(url)
        legenda = yt.captions.get_by_language_code(idioma)
        if not legenda:
            raise ValueError(f"Legenda no idioma {idioma} não disponível.")
        
        legenda.download()
        return legenda.generate_srt_captions()
    except Exception as e:
        print(f"Erro ao baixar legenda: {e}", file=sys.stderr)
        return None

def main():
    """
    Função principal para executar o script.
    """
    if len(sys.argv) != 2:
        print("Uso: python extrator_legenda_youtube.py <URL_DO_VIDEO>")
        sys.exit(1)
    
    url = sys.argv[1]
    legenda = baixar_legenda(url)
    if legenda:
        print("Legenda baixada com sucesso!")
    else:
        print("Falha ao baixar a legenda.")

if __name__ == '__main__':
    main()