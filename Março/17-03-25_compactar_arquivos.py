import os
import tarfile
import zipfile

# Função para compactar arquivos em .tar
def compactar_tar(diretorio, arquivo_tar):
    """
    Função para compactar um diretório em um arquivo .tar.
    :param diretorio: Caminho do diretório que será compactado.
    :param arquivo_tar: Nome do arquivo .tar de saída.
    """
    try:
        with tarfile.open(arquivo_tar, "w") as tar:
            tar.add(diretorio, arcname=os.path.basename(diretorio))
        print(f"Diretório '{diretorio}' compactado em '{arquivo_tar}' com sucesso!")
    except Exception as e:
        print(f"Erro ao compactar diretório: {e}")

# Função para descompactar arquivos .tar
def descompactar_tar(arquivo_tar, destino):
    """
    Função para descompactar um arquivo .tar em um diretório de destino.
    :param arquivo_tar: Caminho do arquivo .tar que será descompactado.
    :param destino: Diretório onde os arquivos serão extraídos.
    """
    try:
        with tarfile.open(arquivo_tar, "r") as tar:
            tar.extractall(path=destino)
        print(f"Arquivo '{arquivo_tar}' descompactado em '{destino}' com sucesso!")
    except Exception as e:
        print(f"Erro ao descompactar arquivo .tar: {e}")

# Função para compactar arquivos em .zip
def compactar_zip(diretorio, arquivo_zip):
    """
    Função para compactar um diretório em um arquivo .zip.
    :param diretorio: Caminho do diretório que será compactado.
    :param arquivo_zip: Nome do arquivo .zip de saída.
    """
    try:
        with zipfile.ZipFile(arquivo_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
            for raiz, dirs, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    caminho_arquivo = os.path.join(raiz, arquivo)
                    zipf.write(caminho_arquivo, arcname=os.path.relpath(caminho_arquivo, diretorio))
        print(f"Diretório '{diretorio}' compactado em '{arquivo_zip}' com sucesso!")
    except Exception as e:
        print(f"Erro ao compactar diretório: {e}")

# Função para descompactar arquivos .zip
def descompactar_zip(arquivo_zip, destino):
    """
    Função para descompactar um arquivo .zip em um diretório de destino.
    :param arquivo_zip: Caminho do arquivo .zip que será descompactado.
    :param destino: Diretório onde os arquivos serão extraídos.
    """
    try:
        with zipfile.ZipFile(arquivo_zip, "r") as zipf:
            zipf.extractall(destino)
        print(f"Arquivo '{arquivo_zip}' descompactado em '{destino}' com sucesso!")
    except Exception as e:
        print(f"Erro ao descompactar arquivo .zip: {e}")

# Função principal para exibir o menu
def menu():
    while True:
        print("\nEscolha uma operação:")
        print("1. Compactar diretório em .tar")
        print("2. Descompactar arquivo .tar")
        print("3. Compactar diretório em .zip")
        print("4. Descompactar arquivo .zip")
        print("5. Sair")
        
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == "1":
            diretorio = input("Digite o caminho do diretório a ser compactado: ")
            arquivo_tar = input("Digite o nome do arquivo .tar de saída: ")
            compactar_tar(diretorio, arquivo_tar)
        elif escolha == "2":
            arquivo_tar = input("Digite o caminho do arquivo .tar a ser descompactado: ")
            destino = input("Digite o diretório de destino para descompactar: ")
            descompactar_tar(arquivo_tar, destino)
        elif escolha == "3":
            diretorio = input("Digite o caminho do diretório a ser compactado: ")
            arquivo_zip = input("Digite o nome do arquivo .zip de saída: ")
            compactar_zip(diretorio, arquivo_zip)
        elif escolha == "4":
            arquivo_zip = input("Digite o caminho do arquivo .zip a ser descompactado: ")
            destino = input("Digite o diretório de destino para descompactar: ")
            descompactar_zip(arquivo_zip, destino)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    menu()
