def is_triangle(a, b, c):
    """
    Verifica se três medidas podem formar um triângulo.

    :param a: Medida do primeiro lado
    :param b: Medida do segundo lado
    :param c: Medida do terceiro lado
    :return: True se pode formar um triângulo, False caso contrário
    """
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    """
    Determina o tipo de triângulo com base nas medidas dos lados.

    :param a: Medida do primeiro lado
    :param b: Medida do segundo lado
    :param c: Medida do terceiro lado
    :return: Tipo do triângulo ('Equilátero', 'Isósceles', 'Escaleno')
    """
    if a == b == c:
        return 'Equilátero'
    elif a == b or b == c or a == c:
        return 'Isósceles'
    else:
        return 'Escaleno'

def main():
    """
    Função principal que recebe as medidas dos lados e imprime o tipo de triângulo.
    """
    try:
        a = float(input("Digite a medida do primeiro lado: "))
        b = float(input("Digite a medida do segundo lado: "))
        c = float(input("Digite a medida do terceiro lado: "))

        if is_triangle(a, b, c):
            print(f"Os lados formam um triângulo {triangle_type(a, b, c)}.")
        else:
            print("Os lados não formam um triângulo.")
    except ValueError:
        print("Por favor, insira medidas numéricas válidas.")

if __name__ == '__main__':
    main()