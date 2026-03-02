"""
Extrator de Áudio de Vídeo

Este script extrai a trilha sonora de um arquivo de vídeo e salva como um arquivo .mp3 separado.
"""

import os
import sys
from moviepy.editor import VideoFileClip

def extrair_audio(video_path, output_audio_path):
    """
    Extrai a trilha sonora de um arquivo de vídeo.

    Args:
        video_path (str): Caminho para o arquivo de vídeo.
        output_audio_path (str): Caminho onde o arquivo de áudio será salvo.

    Raises:
        FileNotFoundError: Se o arquivo de vídeo não for encontrado.
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"O arquivo de vídeo '{video_path}' não foi encontrado.")

    # Carrega o vídeo
    video = VideoFileClip(video_path)

    # Extrai o áudio
    audio = video.audio

    # Salva o áudio como .mp3
    audio.write_audiofile(output_audio_path, codec='libmp3lame')

    print(f"Áudio extraído com sucesso e salvo em '{output_audio_path}'.")

def main():
    if len(sys.argv) != 3:
        print("Uso: python extrator_audios_video.py <caminho_do_video> <caminho_do_audio>")
        sys.exit(1)

    video_path = sys.argv[1]
    output_audio_path = sys.argv[2]

    try:
        extrair_audio(video_path, output_audio_path)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()