import csv

def ler_cabecalho_csv(caminho_arquivo):
    """
    Lê um arquivo CSV e retorna os nomes das colunas presentes na primeira linha.

    Args:
        caminho_arquivo (str): O caminho para o arquivo CSV.

    Returns:
        list: Uma lista contendo os nomes das colunas.
    """
    try:
        with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            cabecalho = next(leitor_csv)
            return cabecalho
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None

def main():
    caminho_arquivo = input("Digite o caminho do arquivo CSV: ")
    cabecalho = ler_cabecalho_csv(caminho_arquivo)
    if cabecalho:
        print("Nomes das colunas:")
        print(", ".join(cabecalho))

if __name__ == '__main__':
    main()