def decimal_to_binary_octal_hexadecimal(decimal_number):
    """
    Converte um número decimal para suas representações binária, octal e hexadecimal.

    Args:
    decimal_number (int): O número decimal a ser convertido.

    Returns:
    tuple: Uma tupla contendo a representação binária, octal e hexadecimal do número.
    """
    binary = bin(decimal_number)[2:]
    octal = oct(decimal_number)[2:]
    hexadecimal = hex(decimal_number)[2:]
    return binary, octal, hexadecimal

def binary_to_decimal(binary_number):
    """
    Converte um número binário para decimal.

    Args:
    binary_number (str): O número binário a ser convertido.

    Returns:
    int: O número decimal correspondente.
    """
    return int(binary_number, 2)

def octal_to_decimal(octal_number):
    """
    Converte um número octal para decimal.

    Args:
    octal_number (str): O número octal a ser convertido.

    Returns:
    int: O número decimal correspondente.
    """
    return int(octal_number, 8)

def hexadecimal_to_decimal(hexadecimal_number):
    """
    Converte um número hexadecimal para decimal.

    Args:
    hexadecimal_number (str): O número hexadecimal a ser convertido.

    Returns:
    int: O número decimal correspondente.
    """
    return int(hexadecimal_number, 16)

def main():
    """
    Função principal que solicita ao usuário um número decimal e exibe suas conversões para binário, octal e hexadecimal.
    """
    try:
        decimal_number = int(input("Digite um número decimal: "))
        binary, octal, hexadecimal = decimal_to_binary_octal_hexadecimal(decimal_number)
        print(f"Decimal: {decimal_number}")
        print(f"Binário: {binary}")
        print(f"Octal: {octal}")
        print(f"Hexadecimal: {hexadecimal}")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == '__main__':
    main()