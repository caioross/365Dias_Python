"""
leitor_metadados_imagem.py

Script para extrair informações básicas de uma imagem, incluindo dimensões, formato e modo de cor.
"""

from PIL import Image

def extrair_metadados_imagem(caminho_imagem):
    """
    Extrai informações básicas de uma imagem.

    Args:
        caminho_imagem (str): O caminho para o arquivo de imagem.

    Returns:
        dict: Um dicionário contendo as informações da imagem.
    """
    try:
        with Image.open(caminho_imagem) as img:
            metadados = {
                'formato': img.format,
                'modo': img.mode,
                'dimensoes': img.size
            }
            return metadados
    except IOError as e:
        print(f"Erro ao abrir a imagem: {e}")
        return None

def main():
    """
    Função principal que executa o script.
    """
    caminho_imagem = input("Digite o caminho para a imagem: ")
    metadados = extrair_metadados_imagem(caminho_imagem)
    if metadados:
        print("Metadados da imagem:")
        for chave, valor in metadados.items():
            print(f"{chave}: {valor}")

if __name__ == '__main__':
    main()