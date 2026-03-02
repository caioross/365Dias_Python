def fibonacci_sequence(n):
    """
    Gera uma lista contendo os primeiros n elementos da sequência de Fibonacci.

    Args:
        n (int): O número de elementos da sequência de Fibonacci a serem gerados.

    Returns:
        list: Uma lista contendo os primeiros n elementos da sequência de Fibonacci.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence

def main():
    """
    Solicita ao usuário um número 'n' e exibe os primeiros 'n' elementos da sequência de Fibonacci.
    """
    try:
        n = int(input("Digite o número de elementos da sequência de Fibonacci que deseja gerar: "))
        if n < 0:
            print("O número deve ser não negativo.")
            return
        
        sequence = fibonacci_sequence(n)
        print(f"Os primeiros {n} elementos da sequência de Fibonacci são: {sequence}")
    
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == '__main__':
    main()