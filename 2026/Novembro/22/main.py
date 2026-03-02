"""
simulador_mercado_acoes_v2.py

Este script permite simular a compra de ações reais com preços atualizados da bolsa utilizando a biblioteca YFinance.
"""

import yfinance as yf
from datetime import datetime

def obter_preco_acao(ticker):
    """
    Obtém o preço atual de uma ação específica.

    Args:
        ticker (str): O símbolo da ação (por exemplo, 'AAPL' para Apple Inc.).

    Returns:
        float: O preço atual da ação.
    """
    acao = yf.Ticker(ticker)
    historico = acao.history(period="1d")
    preco_atual = historico['Close'].iloc[-1]
    return preco_atual

def simular_compra_acao(ticker, quantidade, dinheiro_disponivel):
    """
    Simula a compra de uma quantidade específica de ações.

    Args:
        ticker (str): O símbolo da ação.
        quantidade (int): A quantidade de ações a serem compradas.
        dinheiro_disponivel (float): O dinheiro disponível para a compra.

    Returns:
        tuple: Uma tupla contendo o número de ações compradas e o dinheiro restante.
    """
    preco_acao = obter_preco_acao(ticker)
    custo_total = preco_acao * quantidade

    if custo_total > dinheiro_disponivel:
        print("Saldo insuficiente para realizar a compra.")
        return 0, dinheiro_disponivel

    dinheiro_restante = dinheiro_disponivel - custo_total
    print(f"Compra realizada com sucesso: {quantidade} ações de {ticker} por R$ {preco_acao:.2f} cada.")
    print(f"Dinheiro restante: R$ {dinheiro_restante:.2f}")
    return quantidade, dinheiro_restante

def main():
    """
    Função principal que executa o simulador de mercado de ações.
    """
    ticker = input("Digite o símbolo da ação (por exemplo, AAPL): ")
    quantidade = int(input("Digite a quantidade de ações a serem compradas: "))
    dinheiro_disponivel = float(input("Digite o dinheiro disponível para a compra: "))

    simular_compra_acao(ticker, quantidade, dinheiro_disponivel)

if __name__ == '__main__':
    main()