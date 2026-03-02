import math

def calcular_crescimento_populacional(populacao_inicial, taxa_crescimento, anos):
    """
    Calcula o crescimento de uma população ao longo de um período de anos.

    Args:
        populacao_inicial (int): O número de indivíduos na população inicial.
        taxa_crescimento (float): A taxa de crescimento anual da população (em decimal).
        anos (int): O número de anos para prever o crescimento.

    Returns:
        int: O tamanho estimado da população após o período especificado.
    """
    if taxa_crescimento < 0:
        raise ValueError("A taxa de crescimento não pode ser negativa.")
    if anos < 0:
        raise ValueError("O número de anos não pode ser negativo.")

    populacao_final = populacao_inicial * math.exp(taxa_crescimento * anos)
    return round(populacao_final)

def main():
    """
    Função principal que executa o simulador de evolução populacional.
    """
    try:
        populacao_inicial = int(input("Digite a população inicial: "))
        taxa_crescimento = float(input("Digite a taxa de crescimento anual (em decimal): "))
        anos = int(input("Digite o número de anos para prever: "))

        populacao_final = calcular_crescimento_populacional(populacao_inicial, taxa_crescimento, anos)
        print(f"A população estimada após {anos} anos será de {populacao_final} indivíduos.")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()