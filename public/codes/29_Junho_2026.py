"""
verificador_forca_senha_v2.py

Este script analisa a força de uma senha comparando-a com uma lista das 10.000 senhas mais comuns.
"""

def carregar_senhas_comuns(caminho_arquivo):
    """
    Carrega as senhas comuns de um arquivo de texto.

    Args:
        caminho_arquivo (str): O caminho para o arquivo contendo as senhas comuns.

    Returns:
        set: Um conjunto contendo as senhas comuns.
    """
    with open(caminho_arquivo, 'r') as arquivo:
        senhas_comuns = set(arquivo.read().splitlines())
    return senhas_comuns

def verificar_forca_senha(senha, senhas_comuns):
    """
    Verifica a força de uma senha comparando-a com uma lista de senhas comuns.

    Args:
        senha (str): A senha a ser verificada.
        senhas_comuns (set): Um conjunto contendo as senhas comuns.

    Returns:
        bool: True se a senha não estiver na lista de senhas comuns, False caso contrário.
    """
    return senha not in senhas_comuns

def main():
    """
    Função principal do script.
    """
    caminho_arquivo = 'senhas_comuns.txt'
    senhas_comuns = carregar_senhas_comuns(caminho_arquivo)

    senha = input("Digite a senha para verificar: ")
    if verificar_forca_senha(senha, senhas_comuns):
        print("A senha é forte e não está na lista de senhas comuns.")
    else:
        print("A senha é fraca e está na lista de senhas comuns.")

if __name__ == '__main__':
    main()