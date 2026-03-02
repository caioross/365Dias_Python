import math

def calcular_area_circulo(raio):
    """
    Calcula a área de um círculo dado o raio.

    Args:
        raio (float): O raio do círculo.

    Returns:
        float: A área do círculo.
    """
    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    return math.pi * (raio ** 2)

def main():
    """
    Função principal que solicita o raio ao usuário e imprime a área do círculo.
    """
    try:
        raio = float(input("Digite o raio do círculo: "))
        area = calcular_area_circulo(raio)
        print(f"A área do círculo com raio {raio} é {area:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()