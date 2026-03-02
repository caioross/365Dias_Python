import math

def calcular_volume(raio):
    """
    Calcula o volume de uma esfera a partir do raio informado.

    Args:
        raio (float): O raio da esfera.

    Returns:
        float: O volume da esfera.
    """
    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    volume = (4/3) * math.pi * (raio ** 3)
    return volume

def main():
    """
    Função principal que solicita o raio ao usuário e exibe o volume da esfera.
    """
    try:
        raio = float(input("Digite o raio da esfera: "))
        volume = calcular_volume(raio)
        print(f"O volume da esfera com raio {raio} é {volume:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()