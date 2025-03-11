def verificar_primo(n):
    """
    Função para verificar se um número é primo.
    Um número primo é aquele que só é divisível por 1 e por ele mesmo.

    :param n: O número a ser verificado.
    :return: True se o número for primo, False caso contrário.
    """
    # Números menores que 2 não são primos
    if n < 2:
        return False

    # Verifica se o número é divisível por algum número entre 2 e a raiz quadrada de n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # Se n for divisível por i, então não é primo
            return False

    # Se nenhum número foi encontrado que divide n, então é primo
    return True


def main():
    """
    Função principal que solicita ao usuário um número e chama a função de verificação.
    """
    try:
        # Solicita ao usuário que insira um número
        num = int(input("Digite um número para verificar se é primo: "))

        # Chama a função verificar_primo e exibe o resultado
        if verificar_primo(num):
            print(f"O número {num} é primo!")
        else:
            print(f"O número {num} não é primo.")
    except ValueError:
        # Caso o usuário insira algo que não seja um número, exibe uma mensagem de erro
        print("Por favor, insira um número válido.")


if __name__ == "__main__":
    # Chama a função principal apenas se o script for executado diretamente
    main()
