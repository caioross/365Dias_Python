import os

def verificar_permissao_arquivo(caminho_arquivo):
    """
    Verifica as permissões de um arquivo específico.

    Args:
        caminho_arquivo (str): O caminho completo para o arquivo.

    Returns:
        dict: Um dicionário contendo as permissões de leitura, escrita e execução.
    """
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo {caminho_arquivo} não existe.")

    permissao = {
        'leitura': os.access(caminho_arquivo, os.R_OK),
        'escrita': os.access(caminho_arquivo, os.W_OK),
        'execucao': os.access(caminho_arquivo, os.X_OK)
    }
    return permissao

def main():
    caminho_arquivo = input("Digite o caminho completo do arquivo: ")
    try:
        permissoes = verificar_permissao_arquivo(caminho_arquivo)
        print(f"Permissões para {caminho_arquivo}:")
        print(f"Leitura: {permissoes['leitura']}")
        print(f"Escrita: {permissoes['escrita']}")
        print(f"Execução: {permissoes['execucao']}")
    except FileNotFoundError as e:
        print(e)

if __name__ == '__main__':
    main()