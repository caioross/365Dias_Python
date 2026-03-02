"""
extrator_tags_id3_v2.py

Script para editar informações de tags ID3v2 em arquivos de áudio.
Permite a edição do título e do artista dos arquivos MP3.

Uso:
    python extrator_tags_id3_v2.py <caminho_arquivo> <novo_titulo> <novo_artista>

Exemplo:
    python extrator_tags_id3_v2.py "musica.mp3" "Novo Título" "Novo Artista"
"""

import sys
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2, TPE1
from mutagen.mp3 import MP3

def editar_tags(caminho_arquivo, novo_titulo, novo_artista):
    """
    Edita as tags ID3v2 de um arquivo MP3.

    :param caminho_arquivo: Caminho para o arquivo MP3.
    :param novo_titulo: Novo título para o arquivo.
    :param novo_artista: Novo artista para o arquivo.
    """
    try:
        # Carrega o arquivo MP3
        audio = MP3(caminho_arquivo, ID3=EasyID3)
        
        # Verifica se o arquivo tem tags ID3
        if not audio.tags:
            audio.add_tags()
        
        # Edita as tags
        audio['title'] = novo_titulo
        audio['artist'] = novo_artista
        
        # Salva as alterações
        audio.save()
        print(f"Tags atualizadas com sucesso para {caminho_arquivo}.")
    except Exception as e:
        print(f"Erro ao atualizar tags: {e}")

def main():
    """
    Função principal que processa os argumentos de linha de comando e chama a função para editar as tags.
    """
    if len(sys.argv) != 4:
        print("Uso: python extrator_tags_id3_v2.py <caminho_arquivo> <novo_titulo> <novo_artista>")
        sys.exit(1)
    
    caminho_arquivo = sys.argv[1]
    novo_titulo = sys.argv[2]
    novo_artista = sys.argv[3]
    
    editar_tags(caminho_arquivo, novo_titulo, novo_artista)

if __name__ == '__main__':
    main()