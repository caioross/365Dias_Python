import os

def comparador_tamanho_arquivos(arquivo1, arquivo2):
    """
    Compara o tamanho de dois arquivos e retorna uma string informando qual arquivo é maior.

    :param arquivo1: Caminho para o primeiro arquivo.
    :param arquivo2: Caminho para o segundo arquivo.
    :return: String informando qual arquivo é maior ou se eles têm o mesmo tamanho.
    """
    try:
        tamanho1 = os.path.getsize(arquivo1)
        tamanho2 = os.path.getsize(arquivo2)
        
        if tamanho1 > tamanho2:
            return f"O arquivo '{arquivo1}' é maior que o arquivo '{arquivo2}'."
        elif tamanho1 < tamanho2:
            return f"O arquivo '{arquivo2}' é maior que o arquivo '{arquivo1}'."
        else:
            return "Os arquivos têm o mesmo tamanho."
    except FileNotFoundError as e:
        return f"Erro: {e}"
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"

def main():
    arquivo1 = input("Digite o caminho para o primeiro arquivo: ")
    arquivo2 = input("Digite o caminho para o segundo arquivo: ")
    
    resultado = comparador_tamanho_arquivos(arquivo1, arquivo2)
    print(resultado)

if __name__ == '__main__':
    main()