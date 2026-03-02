import matplotlib.pyplot as plt

def carregar_dados(caminho_arquivo):
    """
    Carrega dados de vendas mensais de um arquivo CSV.
    
    Args:
        caminho_arquivo (str): Caminho para o arquivo CSV contendo os dados de vendas.
    
    Returns:
        list: Lista de tuplas com o mês e o valor de vendas.
    """
    dados = []
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            mes, vendas = linha.strip().split(',')
            dados.append((mes, float(vendas)))
    return dados

def gerar_grafico(dados):
    """
    Gera um gráfico de linhas com a tendência das vendas.
    
    Args:
        dados (list): Lista de tuplas com o mês e o valor de vendas.
    """
    meses, vendas = zip(*dados)
    plt.figure(figsize=(10, 5))
    plt.plot(meses, vendas, marker='o', linestyle='-', color='b')
    plt.title('Tendência de Vendas Mensais')
    plt.xlabel('Mês')
    plt.ylabel('Vendas')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Função principal do script.
    """
    caminho_arquivo = 'vendas_mensais.csv'
    dados = carregar_dados(caminho_arquivo)
    gerar_grafico(dados)

if __name__ == '__main__':
    main()