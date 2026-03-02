def gerar_tabuada(numero):
    """
    Gera a tabuada de um número de 1 a 10.

    Args:
        numero (int): O número para o qual a tabuada será gerada.

    Returns:
        str: Uma string contendo a tabuada formatada.
    """
    if not (1 <= numero <= 10):
        raise ValueError("O número deve estar entre 1 e 10.")

    tabuada = ""
    for i in range(1, 11):
        resultado = numero * i
        tabuada += f"{numero} x {i} = {resultado}\n"
    return tabuada

def main():
    """
    Função principal que solicita ao usuário um número e exibe sua tabuada.
    """
    try:
        numero = int(input("Digite um número entre 1 e 10 para gerar a tabuada: "))
        tabuada = gerar_tabuada(numero)
        print("\nTabuada:")
        print(tabuada)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()