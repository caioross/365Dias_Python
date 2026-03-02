"""
Calculadora de Financiamento SAC

Este script gera uma tabela de amortização para financiamento de imóveis ou veículos
utilizando o sistema de amortização SAC (Sistema de Amortização Constante).
"""

import csv

def calcular_amortizacao_sac(valor_financiado, taxa_juros_mensal, numero_parcelas):
    """
    Calcula a tabela de amortização SAC.

    Args:
        valor_financiado (float): O valor total financiado.
        taxa_juros_mensal (float): A taxa de juros mensal (em decimal).
        numero_parcelas (int): O número total de parcelas.

    Returns:
        list: Uma lista de dicionários contendo os dados da tabela de amortização.
    """
    amortizacao = valor_financiado / numero_parcelas
    saldo_devedor = valor_financiado
    tabela_amortizacao = []

    for parcela in range(1, numero_parcelas + 1):
        juros = saldo_devedor * taxa_juros_mensal
        parcela_total = amortizacao + juros
        saldo_devedor -= amortizacao

        tabela_amortizacao.append({
            'Parcela': parcela,
            'Amortização': amortizacao,
            'Juros': juros,
            'Parcela Total': parcela_total,
            'Saldo Devedor': saldo_devedor
        })

    return tabela_amortizacao

def salvar_tabela_amortizacao_csv(tabela_amortizacao, nome_arquivo):
    """
    Salva a tabela de amortização em um arquivo CSV.

    Args:
        tabela_amortizacao (list): A tabela de amortização a ser salva.
        nome_arquivo (str): O nome do arquivo CSV onde a tabela será salva.
    """
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'Parcela', 'Amortização', 'Juros', 'Parcela Total', 'Saldo Devedor'
        ])
        writer.writeheader()
        writer.writerows(tabela_amortizacao)

def main():
    """
    Função principal que executa o script.
    """
    valor_financiado = float(input("Digite o valor financiado: "))
    taxa_juros_anual = float(input("Digite a taxa de juros anual (em %): "))
    numero_parcelas = int(input("Digite o número de parcelas: "))

    taxa_juros_mensal = taxa_juros_anual / 100 / 12
    tabela_amortizacao = calcular_amortizacao_sac(valor_financiado, taxa_juros_mensal, numero_parcelas)

    for linha in tabela_amortizacao:
        print(linha)

    salvar_tabela_amortizacao_csv(tabela_amortizacao, 'tabela_amortizacao_sac.csv')
    print(f"Tabela de amortização salva em 'tabela_amortizacao_sac.csv'.")

if __name__ == '__main__':
    main()