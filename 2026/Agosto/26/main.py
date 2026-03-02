def validador_expressao_matematica(expressao):
    """
    Verifica se os parênteses, colchetes e chaves estão fechados corretamente em uma expressão matemática.

    Args:
        expressao (str): A expressão matemática a ser validada.

    Returns:
        bool: True se a expressão estiver corretamente fechada, False caso contrário.
    """
    pilha = []
    fechamento = {')': '(', ']': '[', '}': '{'}
    
    for char in expressao:
        if char in '([{':
            pilha.append(char)
        elif char in ')]}':
            if not pilha or pilha[-1] != fechamento[char]:
                return False
            pilha.pop()
    
    return not pilha

def main():
    expressao = input("Digite a expressão matemática para validar: ")
    if validador_expressao_matematica(expressao):
        print("A expressão está corretamente fechada.")
    else:
        print("A expressão está incorretamente fechada.")

if __name__ == '__main__':
    main()