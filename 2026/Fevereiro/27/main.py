import os

def extrair_extensao_arquivo(caminho_arquivo):
    """
    Extrai a extensão de um arquivo a partir do seu caminho completo.

    Args:
        caminho_arquivo (str): O caminho completo do arquivo.

    Returns:
        str: A extensão do arquivo. Retorna uma string vazia se o arquivo não tiver extensão.
    """
    _, extensao = os.path.splitext(caminho_arquivo)
    return extensao

def main():
    caminho_arquivo = input("Digite o caminho completo do arquivo: ")
    extensao = extrair_extensao_arquivo(caminho_arquivo)
    print(f"A extensão do arquivo é: {extensao}")

if __name__ == '__main__':
    main()