import math

def seno(angulo):
    """
    Calcula o seno de um ângulo em graus.

    :param angulo: Ângulo em graus
    :return: Valor do seno
    """
    return math.sin(math.radians(angulo))

def cosseno(angulo):
    """
    Calcula o cosseno de um ângulo em graus.

    :param angulo: Ângulo em graus
    :return: Valor do cosseno
    """
    return math.cos(math.radians(angulo))

def logaritmo_base10(numero):
    """
    Calcula o logaritmo base 10 de um número.

    :param numero: Número para calcular o logaritmo
    :return: Valor do logaritmo base 10
    """
    if numero <= 0:
        raise ValueError("O número deve ser maior que zero.")
    return math.log10(numero)

def raiz_quadrada(numero):
    """
    Calcula a raiz quadrada de um número.

    :param numero: Número para calcular a raiz quadrada
    :return: Valor da raiz quadrada
    """
    if numero < 0:
        raise ValueError("O número deve ser não negativo.")
    return math.sqrt(numero)

def main():
    """
    Função principal que executa o menu interativo da calculadora científica.
    """
    while True:
        print("\nCalculadora Científica")
        print("1. Seno")
        print("2. Cosseno")
        print("3. Logaritmo base 10")
        print("4. Raiz Quadrada")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '5':
            print("Saindo da calculadora.")
            break

        try:
            if escolha == '1':
                angulo = float(input("Digite o ângulo em graus: "))
                print(f"Seno({angulo}) = {seno(angulo)}")
            elif escolha == '2':
                angulo = float(input("Digite o ângulo em graus: "))
                print(f"Cosseno({angulo}) = {cosseno(angulo)}")
            elif escolha == '3':
                numero = float(input("Digite o número para calcular o logaritmo: "))
                print(f"log10({numero}) = {logaritmo_base10(numero)}")
            elif escolha == '4':
                numero = float(input("Digite o número para calcular a raiz quadrada: "))
                print(f"sqrt({numero}) = {raiz_quadrada(numero)}")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == '__main__':
    main()