import os
import time
from datetime import datetime, timedelta

def listar_arquivos_antigos(diretorio, meses=6):
    """
    Lista todos os arquivos em um diretório que não foram modificados há mais de um número especificado de meses.

    :param diretorio: Caminho para o diretório a ser verificado.
    :param meses: Número de meses para considerar um arquivo como 'antigo'.
    :return: Lista de nomes de arquivos que não foram modificados há mais de 'meses' meses.
    """
    arquivos_antigos = []
    tempo_atual = time.time()
    tempo_corte = tempo_atual - (meses * 30 * 24 * 60 * 60)  # Aproximação de meses para segundos

    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        if os.path.isfile(caminho_arquivo):
            tempo_modificacao = os.path.getmtime(caminho_arquivo)
            if tempo_modificacao < tempo_corte:
                arquivos_antigos.append(nome_arquivo)

    return arquivos_antigos

def main():
    diretorio = input("Digite o caminho do diretório a ser verificado: ")
    arquivos_antigos = listar_arquivos_antigos(diretorio)
    if arquivos_antigos:
        print("Arquivos não modificados há mais de 6 meses:")
        for arquivo in arquivos_antigos:
            print(arquivo)
    else:
        print("Nenhum arquivo antigo encontrado.")

if __name__ == '__main__':
    main()