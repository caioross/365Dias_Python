import math

def calcular_delta(a, b, c):
    """
    Calcula o delta da equação de segundo grau.

    Args:
        a (float): Coeficiente A da equação.
        b (float): Coeficiente B da equação.
        c (float): Coeficiente C da equação.

    Returns:
        float: O valor do delta.
    """
    return b**2 - 4*a*c

def calcular_raizes(a, b, delta):
    """
    Calcula as raízes da equação de segundo grau.

    Args:
        a (float): Coeficiente A da equação.
        b (float): Coeficiente B da equação.
        delta (float): O valor do delta.

    Returns:
        tuple: Uma tupla contendo as raízes da equação.
    """
    if delta < 0:
        return None, None
    elif delta == 0:
        x = -b / (2*a)
        return x, x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

def main():
    """
    Função principal que solicita os coeficientes da equação de segundo grau
    e exibe as raízes calculadas.
    """
    print("Resolução de equações de segundo grau (Ax^2 + Bx + C = 0)")
    try:
        a = float(input("Digite o coeficiente A: "))
        b = float(input("Digite o coeficiente B: "))
        c = float(input("Digite o coeficiente C: "))

        if a == 0:
            print("O coeficiente A não pode ser zero para uma equação de segundo grau.")
            return

        delta = calcular_delta(a, b, c)
        raiz1, raiz2 = calcular_raizes(a, b, delta)

        if raiz1 is None and raiz2 is None:
            print("A equação não possui raízes reais.")
        elif raiz1 == raiz2:
            print(f"A equação possui uma raiz real: x = {raiz1}")
        else:
            print(f"A equação possui duas raízes reais: x1 = {raiz1}, x2 = {raiz2}")

    except ValueError:
        print("Por favor, digite valores numéricos válidos para os coeficientes.")

if __name__ == '__main__':
    main()