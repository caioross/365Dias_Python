"""
simulador_investimento_fii.py

Este script calcula a projeção de rendimentos mensais de Fundos Imobiliários (FII)
com base no Dividend Yield e no aporte inicial.
"""

def calcular_rendimento_mensal(dividend_yield, aporte):
    """
    Calcula o rendimento mensal de um FII.

    Args:
        dividend_yield (float): O Dividend Yield do FII (em porcentagem).
        aporte (float): O valor do aporte inicial no FII.

    Returns:
        float: O rendimento mensal.
    """
    return (dividend_yield / 100) * aporte

def projetar_rendimentos(dividend_yield, aporte, meses):
    """
    Projeção de rendimentos mensais de um FII.

    Args:
        dividend_yield (float): O Dividend Yield do FII (em porcentagem).
        aporte (float): O valor do aporte inicial no FII.
        meses (int): O número de meses para a projeção.

    Returns:
        list: Uma lista com os rendimentos mensais.
    """
    rendimentos = []
    for _ in range(meses):
        rendimento_mensal = calcular_rendimento_mensal(dividend_yield, aporte)
        rendimentos.append(rendimento_mensal)
    return rendimentos

def main():
    """
    Função principal que executa o simulador de investimento em FII.
    """
    try:
        dividend_yield = float(input("Digite o Dividend Yield do FII (em porcentagem): "))
        aporte = float(input("Digite o valor do aporte inicial no FII: "))
        meses = int(input("Digite o número de meses para a projeção: "))

        rendimentos = projetar_rendimentos(dividend_yield, aporte, meses)
        print("\nProjeção de Rendimentos Mensais:")
        for mes, rendimento in enumerate(rendimentos, start=1):
            print(f"Mês {mes}: R$ {rendimento:.2f}")

    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira valores numéricos válidos.")

if __name__ == '__main__':
    main()