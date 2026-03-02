import os

def gerar_playlist_m3u(caminho_pasta, nome_playlist='playlist.m3u'):
    """
    Gera um arquivo de playlist .m3u a partir de arquivos de música em uma pasta.

    Args:
        caminho_pasta (str): O caminho para a pasta onde estão os arquivos de música.
        nome_playlist (str, optional): O nome do arquivo de playlist a ser criado. Defaults to 'playlist.m3u'.
    """
    try:
        with open(nome_playlist, 'w', encoding='utf-8') as playlist_file:
            for root, _, files in os.walk(caminho_pasta):
                for file in files:
                    if file.lower().endswith(('.mp3', '.flac', '.wav', '.ogg', '.aac')):
                        caminho_arquivo = os.path.join(root, file)
                        playlist_file.write(f"{caminho_arquivo}\n")
        print(f"Playlist '{nome_playlist}' criada com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar a playlist: {e}")

def main():
    """
    Função principal que executa o script para gerar a playlist.
    """
    caminho_pasta = input("Digite o caminho da pasta onde estão os arquivos de música: ")
    nome_playlist = input("Digite o nome do arquivo de playlist (opcional): ") or 'playlist.m3u'
    gerar_playlist_m3u(caminho_pasta, nome_playlist)

if __name__ == '__main__':
    main()