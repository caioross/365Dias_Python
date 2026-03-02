"""
simulador_fila_banco.py

Este script simula o funcionamento de uma fila bancária usando uma estrutura de dados FIFO (First In, First Out).
"""

from collections import deque

class FilaBanco:
    """
    Classe que representa uma fila bancária.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da FilaBanco.
        """
        self.fila = deque()

    def adicionar_cliente(self, cliente):
        """
        Adiciona um cliente à fila.

        :param cliente: Nome do cliente a ser adicionado.
        """
        self.fila.append(cliente)
        print(f"Cliente {cliente} adicionado à fila.")

    def atender_proximo(self):
        """
        Atende o próximo cliente na fila.

        :return: Nome do cliente atendido ou uma mensagem se a fila estiver vazia.
        """
        if not self.fila:
            return "Fila vazia. Nenhum cliente para atender."
        cliente = self.fila.popleft()
        print(f"Atendendo cliente: {cliente}")
        return cliente

    def tamanho_fila(self):
        """
        Retorna o número de clientes na fila.

        :return: Tamanho da fila.
        """
        return len(self.fila)

def main():
    """
    Função principal que demonstra o funcionamento da FilaBanco.
    """
    fila_banco = FilaBanco()
    
    # Adicionando clientes à fila
    fila_banco.adicionar_cliente("João")
    fila_banco.adicionar_cliente("Maria")
    fila_banco.adicionar_cliente("Carlos")
    
    # Atendendo clientes
    fila_banco.atender_proximo()
    fila_banco.atender_proximo()
    
    # Verificando o tamanho da fila
    print(f"Tamanho da fila: {fila_banco.tamanho_fila()}")
    
    # Atendendo o último cliente
    fila_banco.atender_proximo()
    
    # Tentando atender um cliente em uma fila vazia
    fila_banco.atender_proximo()

if __name__ == '__main__':
    main()