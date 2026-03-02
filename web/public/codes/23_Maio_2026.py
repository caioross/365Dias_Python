"""
simulador_investimento_tesouro.py

Este script compara a rentabilidade bruta entre os investimentos Tesouro Selic, IPCA e Prefixado em um período específico.
"""

from typing import Dict

def calcular_rentabilidade_selic(taxa_selic: float, periodo_anos: int) -> float:
    """
    Calcula a rentabilidade bruta do Tesouro Selic.

    :param taxa_selic: Taxa SELIC anual (em decimal).
    :param periodo_anos: Período de investimento em anos.
    :return: Rentabilidade bruta do Tesouro Selic.
    """
    return taxa_selic * periodo_anos

def calcular_rentabilidade_ipca(taxa_ipca: float, inflacao_anual: float, periodo_anos: int) -> float:
    """
    Calcula a rentabilidade bruta do IPCA.

    :param taxa_ipca: Taxa IPCA anual (em decimal).
    :param inflacao_anual: Taxa de inflação anual (em decimal).
    :param periodo_anos: Período de investimento em anos.
    :return: Rentabilidade bruta do IPCA.
    """
    return (1 + taxa_ipca) ** periodo_anos - 1 - inflacao_anual * periodo_anos

def calcular_rentabilidade_prefixado(taxa_prefixado: float, periodo_anos: int) -> float:
    """
    Calcula a rentabilidade bruta do Tesouro Prefixado.

    :param taxa_prefixado: Taxa Prefixado anual (em decimal).
    :param periodo_anos: Período de investimento em anos.
    :return: Rentabilidade bruta do Tesouro Prefixado.
    """
    return taxa_prefixado * periodo_anos

def main():
    """
    Função principal que compara a rentabilidade bruta entre Tesouro Selic, IPCA e Prefixado.
    """
    taxa_selic = 0.10  # 10% SELIC
    taxa_ipca = 0.06   # 6% IPCA
    inflacao_anual = 0.05  # 5% inflação
    taxa_prefixado = 0.08  # 8% Prefixado
    periodo_anos = 5  # 5 anos de investimento

    rentabilidade_selic = calcular_rentabilidade_selic(taxa_selic, periodo_anos)
    rentabilidade_ipca = calcular_rentabilidade_ipca(taxa_ipca, inflacao_anual, periodo_anos)
    rentabilidade_prefixado = calcular_rentabilidade_prefixado(taxa_prefixado, periodo_anos)

    resultados = {
        'Selic': rentabilidade_selic,
        'IPCA': rentabilidade_ipca,
        'Prefixado': rentabilidade_prefixado
    }

    print("Rentabilidades após 5 anos:")
    for investimento, rentabilidade in resultados.items():
        print(f"{investimento}: {rentabilidade:.2%}")

if __name__ == '__main__':
    main()