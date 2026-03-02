import hashlib

def calcular_hash_md5(caminho_arquivo):
    """
    Calcula o hash MD5 de um arquivo.

    Args:
        caminho_arquivo (str): O caminho completo para o arquivo.

    Returns:
        str: O hash MD5 do arquivo.
    """
    hash_md5 = hashlib.md5()
    try:
        with open(caminho_arquivo, "rb") as arquivo:
            for chunk in iter(lambda: arquivo.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {caminho_arquivo} não foi encontrado.")
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao calcular o hash: {e}")

def main():
    """
    Função principal que solicita ao usuário o caminho do arquivo
    e exibe o hash MD5 calculado para o arquivo.
    """
    caminho_arquivo = input("Digite o caminho completo do arquivo: ")
    try:
        hash_md5 = calcular_hash_md5(caminho_arquivo)
        print(f"O hash MD5 do arquivo é: {hash_md5}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()