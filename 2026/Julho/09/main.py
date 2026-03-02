"""
Script para extrair metadados de um arquivo de vídeo, incluindo resolução, bitrate e codec.
Suporta arquivos MP4 e MKV.
"""

import subprocess

def extrair_metadados(caminho_arquivo):
    """
    Extrai metadados de um arquivo de vídeo usando o comando 'ffprobe'.
    
    Args:
        caminho_arquivo (str): Caminho para o arquivo de vídeo.
    
    Returns:
        dict: Dicionário contendo resolução, bitrate e codec.
    """
    try:
        # Executa o ffprobe para obter informações sobre o vídeo
        resultado = subprocess.run(
            ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
             'stream=width,height,bit_rate,codec_name', '-of', 'default=noprint_wrappers=1:nokey=1',
             caminho_arquivo],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if resultado.returncode != 0:
            raise Exception(f"Erro ao extrair metadados: {resultado.stderr}")
        
        # Processa a saída do ffprobe
        metadados = {}
        for linha in resultado.stdout.splitlines():
            chave, valor = linha.split('=')
            metadados[chave.strip()] = valor.strip()
        
        # Formata a resolução
        metadados['resolucao'] = f"{metadados['width']}x{metadados['height']}"
        
        # Converte bitrate de bps para Mbps
        metadados['bitrate'] = f"{int(metadados['bit_rate']) / 1000000:.2f} Mbps"
        
        return metadados
    
    except Exception as e:
        print(f"Erro: {e}")
        return None

def main():
    """
    Função principal para demonstrar o uso do extrator de metadados.
    """
    caminho_arquivo = input("Digite o caminho para o arquivo de vídeo: ")
    metadados = extrair_metadados(caminho_arquivo)
    
    if metadados:
        print("\nMetadados do vídeo:")
        print(f"Resolução: {metadados['resolucao']}")
        print(f"Bitrate: {metadados['bitrate']}")
        print(f"Codec: {metadados['codec_name']}")
    else:
        print("Não foi possível extrair metadados do vídeo.")

if __name__ == '__main__':
    main()