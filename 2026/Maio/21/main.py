"""
gerador_grafico_pizza.py

Este script cria um gráfico de setores (pizza) com base nas categorias e valores fornecidos pelo usuário.
"""

import matplotlib.pyplot as plt

def criar_grafico_pizza(categorias, valores):
    """
    Cria um gráfico de setores (pizza) com as categorias e valores fornecidos.

    :param categorias: Lista de strings representando as categorias.
    :param valores: Lista de números representando os valores correspondentes a cada categoria.
    """
    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
    plt.title('Gráfico de Setores (Pizza)')
    plt.show()

def main():
    """
    Função principal que solicita ao usuário as categorias e valores, e então cria o gráfico de pizza.
    """
    categorias = input("Digite as categorias separadas por vírgula: ").split(',')
    valores_input = input("Digite os valores correspondentes separados por vírgula: ").split(',')
    
    try:
        valores = [float(valor) for valor in valores_input]
    except ValueError:
        print("Valores inválidos. Certifique-se de que todos os valores sejam numéricos.")
        return
    
    if len(categorias) != len(valores):
        print("O número de categorias e valores deve ser o mesmo.")
        return
    
    criar_grafico_pizza(categorias, valores)

if __name__ == '__main__':
    main()