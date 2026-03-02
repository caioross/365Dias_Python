def comparar_numeros_decimais(num1, num2, margem_erro=1e-9):
    """
    Compara dois números decimais considerando uma margem de erro.

    Args:
        num1 (float): O primeiro número a ser comparado.
        num2 (float): O segundo número a ser comparado.
        margem_erro (float, optional): A margem de erro permitida para a comparação. Padrão é 1e-9.

    Returns:
        bool: True se os números são considerados iguais dentro da margem de erro, False caso contrário.
    """
    return abs(num1 - num2) < margem_erro

def main():
    # Exemplo de uso
    numero1 = 0.1 + 0.2
    numero2 = 0.3
    margem = 1e-9

    if comparar_numeros_decimais(numero1, numero2, margem):
        print("Os números são considerados iguais dentro da margem de erro.")
    else:
        print("Os números não são considerados iguais dentro da margem de erro.")

if __name__ == '__main__':
    main()