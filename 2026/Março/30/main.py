def calcular_roi(custo_inicial, valor_final):
    """
    Calcula o Retorno sobre Investimento (ROI).

    Args:
        custo_inicial (float): O custo inicial do investimento.
        valor_final (float): O valor final do investimento após um período.

    Returns:
        float: O ROI calculado em porcentagem.
    """
    if custo_inicial == 0:
        raise ValueError("O custo inicial não pode ser zero.")
    roi = ((valor_final - custo_inicial) / custo_inicial) * 100
    return roi

def main():
    """
    Função principal que solicita ao usuário os dados necessários para calcular o ROI
    e exibe o resultado.
    """
    try:
        custo_inicial = float(input("Digite o custo inicial do investimento: "))
        valor_final = float(input("Digite o valor final do investimento: "))
        roi = calcular_roi(custo_inicial, valor_final)
        print(f"O ROI calculado é: {roi:.2f}%")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()