def calcular_potencia(base, expoente):
    """
    Calcula a potência de um número sem usar o operador **.

    Args:
        base (float): A base do cálculo.
        expoente (int): O expoente do cálculo.

    Returns:
        float: O resultado da potência.
    """
    if expoente == 0:
        return 1
    elif expoente < 0:
        base = 1 / base
        expoente = -expoente

    resultado = 1
    for _ in range(expoente):
        resultado *= base

    return resultado

def main():
    """
    Função principal que solicita a base e o expoente ao usuário e exibe o resultado da potência.
    """
    try:
        base = float(input("Digite a base: "))
        expoente = int(input("Digite o expoente: "))
        resultado = calcular_potencia(base, expoente)
        print(f"{base} elevado a {expoente} é {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

if __name__ == '__main__':
    main()