def verificar_par_impar(numero):
    """
    Verifica se um número é par ou ímpar.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        str: Uma string indicando se o número é 'Par' ou 'Ímpar'.
    """
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

def main():
    """
    Função principal que solicita ao usuário um número e verifica se ele é par ou ímpar.
    """
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = verificar_par_impar(numero)
        print(f"O número {numero} é {resultado}.")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == '__main__':
    main()