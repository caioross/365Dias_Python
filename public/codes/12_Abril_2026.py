def gerar_sequencia_lucas(n):
    """
    Gera os primeiros N termos da Sequência de Lucas.

    A Sequência de Lucas é semelhante à Sequência de Fibonacci, mas começa com 2 e 1.
    Os termos subsequentes são a soma dos dois termos anteriores.

    :param n: Número de termos da sequência a serem gerados.
    :return: Lista contendo os primeiros N termos da Sequência de Lucas.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 1]

    sequencia = [2, 1]
    for i in range(2, n):
        proximo_termo = sequencia[i - 1] + sequencia[i - 2]
        sequencia.append(proximo_termo)

    return sequencia

def main():
    """
    Função principal que executa o script para gerar e exibir a Sequência de Lucas.
    """
    try:
        n = int(input("Digite o número de termos da Sequência de Lucas que deseja gerar: "))
        sequencia_lucas = gerar_sequencia_lucas(n)
        print(f"Os primeiros {n} termos da Sequência de Lucas são: {sequencia_lucas}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == '__main__':
    main()