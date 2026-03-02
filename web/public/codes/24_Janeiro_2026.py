def decimal_to_binary(decimal_number):
    """
    Converte um número inteiro decimal para sua representação binária.

    Args:
        decimal_number (int): O número decimal a ser convertido.

    Returns:
        str: A representação binária do número decimal.
    """
    if decimal_number < 0:
        raise ValueError("O número decimal deve ser não negativo.")
    
    if decimal_number == 0:
        return "0"
    
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number

def main():
    """
    Função principal que solicita ao usuário um número decimal e exibe sua representação binária.
    """
    try:
        decimal_input = int(input("Digite um número decimal não negativo: "))
        binary_output = decimal_to_binary(decimal_input)
        print(f"A representação binária de {decimal_input} é {binary_output}.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()