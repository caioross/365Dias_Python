"""
organizador_musicas_artista.py

Script para organizar arquivos MP3 em pastas com base nas tags ID3 de artista e álbum.
"""

import os
import shutil
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

def organizar_musicas(caminho_pasta):
    """
    Organiza arquivos MP3 em pastas com base nas tags ID3 de artista e álbum.

    :param caminho_pasta: Caminho para a pasta contendo os arquivos MP3.
    """
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith('.mp3'):
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            try:
                tags = EasyID3(caminho_arquivo)
                artista = tags.get('artist', ['Desconhecido'])[0]
                album = tags.get('album', ['Desconhecido'])[0]
                pasta_destino = os.path.join(caminho_pasta, artista, album)

                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                print(f'Movido: {caminho_arquivo} para {pasta_destino}')
            except ID3NoHeaderError:
                print(f'Arquivo sem cabeçalho ID3: {caminho_arquivo}')
            except Exception as e:
                print(f'Erro ao processar {caminho_arquivo}: {e}')

def main():
    """
    Função principal para executar o script.
    """
    caminho_pasta = input("Digite o caminho da pasta contendo os arquivos MP3: ")
    organizar_musicas(caminho_pasta)

if __name__ == '__main__':
    main()