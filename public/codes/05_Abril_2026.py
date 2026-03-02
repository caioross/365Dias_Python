import sys

def extrair_erros_de_log(arquivo_log):
    """
    Extrai linhas contendo a palavra 'ERROR' de um arquivo de log.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        list: Lista de linhas que contêm a palavra 'ERROR'.
    """
    try:
        with open(arquivo_log, 'r') as file:
            linhas = file.readlines()
    except FileNotFoundError:
        print(f"O arquivo {arquivo_log} não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        sys.exit(1)

    erros = [linha for linha in linhas if 'ERROR' in linha]
    return erros

def main():
    if len(sys.argv) != 2:
        print("Uso: python filtro_logs_erros.py <caminho_do_arquivo_log>")
        sys.exit(1)

    arquivo_log = sys.argv[1]
    erros = extrair_erros_de_log(arquivo_log)

    for erro in erros:
        print(erro.strip())

if __name__ == '__main__':
    main()