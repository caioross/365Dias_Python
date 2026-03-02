def calcular_rendimento_mensal(valor_investido, taxa_mensal):
    """
    Calcula o rendimento mensal de um investimento em poupança.

    Args:
        valor_investido (float): O valor inicial investido.
        taxa_mensal (float): A taxa de rendimento mensal (em decimal).

    Returns:
        float: O valor do rendimento mensal.
    """
    return valor_investido * taxa_mensal

def main():
    """
    Função principal que executa o simulador de investimento em poupança.
    Solicita ao usuário o valor investido e a taxa mensal, e exibe o rendimento mensal.
    """
    try:
        valor_investido = float(input("Digite o valor investido: "))
        taxa_mensal = float(input("Digite a taxa mensal de rendimento (em %): ")) / 100

        rendimento_mensal = calcular_rendimento_mensal(valor_investido, taxa_mensal)
        print(f"O rendimento mensal será de: R$ {rendimento_mensal:.2f}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == '__main__':
    main()