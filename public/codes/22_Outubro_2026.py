"""
conversor_mp4_para_gif.py

Script para converter vídeos MP4 em GIFs animados com controle de frames por segundo.
"""

import os
import moviepy.editor as mp

def converter_mp4_para_gif(caminho_mp4, caminho_gif, fps=10):
    """
    Converte um vídeo MP4 para um GIF animado.

    Args:
        caminho_mp4 (str): Caminho para o arquivo MP4 de entrada.
        caminho_gif (str): Caminho para o arquivo GIF de saída.
        fps (int, optional): Frames por segundo para o GIF. Padrão é 10.

    Raises:
        FileNotFoundError: Se o arquivo MP4 não for encontrado.
        Exception: Se ocorrer um erro durante a conversão.
    """
    if not os.path.exists(caminho_mp4):
        raise FileNotFoundError(f"O arquivo MP4 {caminho_mp4} não foi encontrado.")

    try:
        video = mp.VideoFileClip(caminho_mp4)
        video.write_gif(caminho_gif, fps=fps)
        print(f"Conversão concluída. O GIF foi salvo em {caminho_gif}")
    except Exception as e:
        raise Exception(f"Ocorreu um erro durante a conversão: {e}")

def main():
    """
    Função principal para executar o script.
    """
    caminho_mp4 = input("Digite o caminho para o arquivo MP4: ")
    caminho_gif = input("Digite o caminho para salvar o GIF: ")
    fps = int(input("Digite o número de frames por segundo (FPS) para o GIF (padrão 10): ") or 10)

    converter_mp4_para_gif(caminho_mp4, caminho_gif, fps)

if __name__ == '__main__':
    main()