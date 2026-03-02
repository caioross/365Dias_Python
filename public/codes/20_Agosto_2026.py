import os

def verificar_arquivo_corrompido(caminho_arquivo):
    """
    Tenta abrir um arquivo e retorna True se o arquivo estiver corrompido ou não puder ser lido,
    caso contrário, retorna False.

    :param caminho_arquivo: Caminho para o arquivo que será verificado.
    :return: Booleano indicando se o arquivo está corrompido ou não.
    """
    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            pass
        return False
    except Exception as e:
        print(f"Erro ao tentar ler o arquivo {caminho_arquivo}: {e}")
        return True

def verificar_diretorio(diretorio):
    """
    Verifica todos os arquivos em um diretório e seus subdiretórios para verificar se estão corrompidos.

    :param diretorio: Caminho para o diretório que será verificado.
    """
    for root, _, files in os.walk(diretorio):
        for file in files:
            caminho_arquivo = os.path.join(root, file)
            if verificar_arquivo_corrompido(caminho_arquivo):
                print(f"Arquivo corrompido ou não lido: {caminho_arquivo}")

def main():
    """
    Função principal que executa o script.
    """
    diretorio = input("Digite o caminho do diretório que deseja verificar: ")
    verificar_diretorio(diretorio)

if __name__ == '__main__':
    main()