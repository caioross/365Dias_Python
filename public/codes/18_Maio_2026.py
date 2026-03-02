"""
simulador_venda_estoque.py

Este script simula um sistema de controle de estoque para um produto fictício.
Ele permite a venda de produtos e alerta quando o nível de estoque está baixo.
"""

class Estoque:
    """
    Classe para representar o estoque de um produto.
    """

    def __init__(self, nome_produto, quantidade_inicial, nivel_minimo):
        """
        Inicializa um novo estoque.

        :param nome_produto: Nome do produto.
        :param quantidade_inicial: Quantidade inicial de produtos no estoque.
        :param nivel_minimo: Nível mínimo de estoque que gera um alerta.
        """
        self.nome_produto = nome_produto
        self.quantidade = quantidade_inicial
        self.nivel_minimo = nivel_minimo

    def vender(self, quantidade):
        """
        Vende uma quantidade de produtos.

        :param quantidade: Quantidade de produtos a serem vendidos.
        :return: True se a venda foi realizada com sucesso, False caso contrário.
        """
        if quantidade > self.quantidade:
            print("Erro: Não há estoque suficiente.")
            return False
        self.quantidade -= quantidade
        self.verificar_nivel_estoque()
        return True

    def verificar_nivel_estoque(self):
        """
        Verifica se o nível de estoque está abaixo do nível mínimo e emite um alerta.
        """
        if self.quantidade < self.nivel_minimo:
            print(f"Alerta: O estoque de {self.nome_produto} está abaixo do nível mínimo ({self.nivel_minimo}).")

def main():
    """
    Função principal que simula o controle de estoque.
    """
    estoque = Estoque("Produto X", 50, 10)

    while True:
        print(f"\nEstoque atual de {estoque.nome_produto}: {estoque.quantidade}")
        try:
            quantidade_venda = int(input("Digite a quantidade a vender (ou 0 para sair): "))
            if quantidade_venda == 0:
                break
            estoque.vender(quantidade_venda)
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

if __name__ == '__main__':
    main()