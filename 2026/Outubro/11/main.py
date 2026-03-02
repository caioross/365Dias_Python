import matplotlib.pyplot as plt
import numpy as np

def gerar_dados_aleatorios(tamanho):
    """
    Gera dados aleatórios para x e y.

    Args:
        tamanho (int): O número de pontos a serem gerados.

    Returns:
        tuple: Uma tupla contendo dois arrays numpy, x e y.
    """
    x = np.random.rand(tamanho)
    y = np.random.rand(tamanho)
    return x, y

def criar_grafico_dispersao(x, y):
    """
    Cria um gráfico de dispersão para as variáveis x e y.

    Args:
        x (array): Os dados para o eixo x.
        y (array): Os dados para o eixo y.
    """
    plt.scatter(x, y, color='blue', alpha=0.5)
    plt.title('Gráfico de Dispersão')
    plt.xlabel('Variável X')
    plt.ylabel('Variável Y')
    plt.grid(True)
    plt.show()

def main():
    """
    Função principal que gera dados aleatórios e cria um gráfico de dispersão.
    """
    tamanho_dados = 100  # Define o número de pontos aleatórios
    x, y = gerar_dados_aleatorios(tamanho_dados)
    criar_grafico_dispersao(x, y)

if __name__ == '__main__':
    main()