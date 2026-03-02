"""
calculadora_financeira_price.py

Este script gera a tabela de amortização para empréstimos e financiamentos
utilizando o sistema Price. O sistema Price é um método de amortização em que
o valor da prestação é fixo ao longo do tempo, mas o valor amortizado e o
juros pagos variam.

Uso:
    python calculadora_financeira_price.py <valor_emprestimo> <taxa_juros> <num_parcelas>

Exemplo:
    python calculadora_financeira_price.py 100000 0.05 60
"""

import sys

def calcular_prestacao_fixa(valor_emprestimo, taxa_juros, num_parcelas):
    """
    Calcula a prestação fixa para o sistema Price.

    Args:
        valor_emprestimo (float): O valor total do empréstimo.
        taxa_juros (float): A taxa de juros anual (ex: 0.05 para 5%).
        num_parcelas (int): O número total de parcelas.

    Returns:
        float: O valor da prestação fixa.
    """
    if taxa_juros == 0:
        return valor_emprestimo / num_parcelas
    return valor_emprestimo * (taxa_juros / (1 - (1 + taxa_juros) ** -num_parcelas))

def gerar_tabela_amortizacao(valor_emprestimo, taxa_juros, num_parcelas):
    """
    Gera a tabela de amortização para o sistema Price.

    Args:
        valor_emprestimo (float): O valor total do empréstimo.
        taxa_juros (float): A taxa de juros anual (ex: 0.05 para 5%).
        num_parcelas (int): O número total de parcelas.

    Returns:
        list: Uma lista de dicionários contendo os detalhes de cada parcela.
    """
    prestacao_fixa = calcular_prestacao_fixa(valor_emprestimo, taxa_juros, num_parcelas)
    saldo_devedor = valor_emprestimo
    tabela = []

    for parcela in range(1, num_parcelas + 1):
        juros = saldo_devedor * taxa_juros
        amortizacao = prestacao_fixa - juros
        saldo_devedor -= amortizacao
        tabela.append({
            'Parcela': parcela,
            'Prestacao': prestacao_fixa,
            'Juros': juros,
            'Amortizacao': amortizacao,
            'Saldo Devedor': saldo_devedor
        })

    return tabela

def main():
    if len(sys.argv) != 4:
        print("Uso: python calculadora_financeira_price.py <valor_emprestimo> <taxa_juros> <num_parcelas>")
        sys.exit(1)

    try:
        valor_emprestimo = float(sys.argv[1])
        taxa_juros = float(sys.argv[2])
        num_parcelas = int(sys.argv[3])
    except ValueError:
        print("Erro: Todos os argumentos devem ser numéricos.")
        sys.exit(1)

    tabela = gerar_tabela_amortizacao(valor_emprestimo, taxa_juros, num_parcelas)

    print("\nTabela de Amortização (Sistema Price)\n")
    print(f"{'Parcela':<10}{'Prestacao':<15}{'Juros':<15}{'Amortizacao':<15}{'Saldo Devedor':<20}")
    for linha in tabela:
        print(f"{linha['Parcela']:<10}{linha['Prestacao']:<15.2f}{linha['Juros']:<15.2f}{linha['Amortizacao']:<15.2f}{linha['Saldo Devedor']:<20.2f}")

if __name__ == '__main__':
    main()