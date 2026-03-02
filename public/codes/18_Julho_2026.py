import random
import time

class Acao:
    """
    Classe que representa uma ação fictícia.
    """
    def __init__(self, nome, preco_inicial):
        self.nome = nome
        self.preco = preco_inicial

    def variar_preco(self):
        """
        Varia o preço da ação de forma aleatória.
        """
        self.preco += random.uniform(-10, 10)
        self.preco = round(self.preco, 2)

class BolsaValores:
    """
    Classe que simula uma bolsa de valores com várias ações.
    """
    def __init__(self, acoes):
        self.acoes = acoes

    def atualizar_precos(self):
        """
        Atualiza os preços de todas as ações na bolsa.
        """
        for acao in self.acoes:
            acao.variar_preco()

    def exibir_precos(self):
        """
        Exibe os preços atuais de todas as ações.
        """
        print("Preços das ações:")
        for acao in self.acoes:
            print(f"{acao.nome}: R${acao.preco}")

def main():
    """
    Função principal do simulador de bolsa de valores.
    """
    acoes = [
        Acao("AAPL", 150.00),
        Acao("GOOGL", 2800.00),
        Acao("AMZN", 3400.00),
        Acao("MSFT", 300.00),
        Acao("FB", 280.00)
    ]

    bolsa = BolsaValores(acoes)

    while True:
        bolsa.atualizar_precos()
        bolsa.exibir_precos()
        time.sleep(5)  # Atualiza os preços a cada 5 segundos

if __name__ == '__main__':
    main()