"""
Calculadora de Férias para CLT

Este script calcula o valor bruto e líquido a receber nas férias,
considerando o terço constitucional, para um empregado com contrato de CLT.
"""

def calcular_ferias(salario_bruto, meses_trabalhados):
    """
    Calcula o valor bruto e líquido das férias.

    Args:
        salario_bruto (float): O salário bruto do empregado.
        meses_trabalhados (int): O número de meses trabalhados no ano.

    Returns:
        tuple: Um tuple contendo o valor bruto das férias e o valor líquido das férias.
    """
    # Cálculo do valor bruto das férias
    valor_ferias = salario_bruto * meses_trabalhados

    # Cálculo do terço constitucional
    terco_constitucional = salario_bruto / 3

    # Valor bruto total das férias
    valor_bruto_total = valor_ferias + terco_constitucional

    # Simplesmente descontando 11% de INSS e 15% de IR para cálculo líquido
    desconto_inss = valor_bruto_total * 0.11
    desconto_ir = valor_bruto_total * 0.15
    valor_liquido_total = valor_bruto_total - desconto_inss - desconto_ir

    return valor_bruto_total, valor_liquido_total

def main():
    """
    Função principal que solicita ao usuário os dados necessários e exibe o resultado.
    """
    try:
        salario_bruto = float(input("Digite o salário bruto do empregado: "))
        meses_trabalhados = int(input("Digite o número de meses trabalhados no ano: "))

        valor_bruto, valor_liquido = calcular_ferias(salario_bruto, meses_trabalhados)

        print(f"Valor bruto das férias: R$ {valor_bruto:.2f}")
        print(f"Valor líquido das férias: R$ {valor_liquido:.2f}")

    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira valores numéricos válidos.")

if __name__ == '__main__':
    main()