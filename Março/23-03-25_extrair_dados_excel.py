import pandas as pd

def ler_planilha_excel(caminho_arquivo):
    """
    Função para ler dados de uma planilha Excel e exibi-los no terminal.
    :param caminho_arquivo: Caminho do arquivo Excel (.xlsx)
    :return: Dados da planilha em formato DataFrame
    """
    try:
        # Lê o arquivo Excel usando pandas
        dados = pd.read_excel(caminho_arquivo)

        # Exibe os dados no terminal
        print("Dados da Planilha Excel:")
        print(dados)
        return dados
    except Exception as e:
        print(f"Erro ao ler a planilha: {e}")

def main():
    """
    Função principal que executa a leitura do arquivo Excel.
    """
    caminho_arquivo = input("Digite o caminho da planilha Excel (.xlsx): ")

    # Chama a função para ler e exibir os dados da planilha
    ler_planilha_excel(caminho_arquivo)

if __name__ == "__main__":
    main()
