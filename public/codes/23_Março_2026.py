import os
import re

def limpar_nome_arquivo(nome_arquivo):
    """
    Remove caracteres especiais e espaços de um nome de arquivo.

    Args:
        nome_arquivo (str): O nome do arquivo original.

    Returns:
        str: O nome do arquivo com caracteres especiais e espaços removidos.
    """
    # Substitui espaços por underscores
    nome_arquivo = nome_arquivo.replace(' ', '_')
    # Remove caracteres especiais usando regex
    nome_arquivo = re.sub(r'[^A-Za-z0-9._-]', '', nome_arquivo)
    return nome_arquivo

def renomear_arquivos_em_diretorio(diretorio):
    """
    Renomeia todos os arquivos em um diretório, removendo caracteres especiais e espaços.

    Args:
        diretorio (str): O caminho do diretório contendo os arquivos a serem renomeados.
    """
    try:
        for nome_arquivo in os.listdir(diretorio):
            caminho_antigo = os.path.join(diretorio, nome_arquivo)
            if os.path.isfile(caminho_antigo):
                novo_nome_arquivo = limpar_nome_arquivo(nome_arquivo)
                caminho_novo = os.path.join(diretorio, novo_nome_arquivo)
                if caminho_antigo != caminho_novo:
                    os.rename(caminho_antigo, caminho_novo)
                    print(f'Renomeado: {caminho_antigo} -> {caminho_novo}')
    except Exception as e:
        print(f'Erro ao renomear arquivos: {e}')

def main():
    """
    Função principal que executa o script de renomeação de arquivos.
    """
    diretorio = input("Digite o caminho do diretório: ")
    renomear_arquivos_em_diretorio(diretorio)

if __name__ == '__main__':
    main()