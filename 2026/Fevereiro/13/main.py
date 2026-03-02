def romano_para_inteiro(romano: str) -> int:
    """
    Converte um número romano para um número inteiro.

    Args:
        romano (str): O número romano a ser convertido.

    Returns:
        int: O número inteiro correspondente ao número romano.

    Raises:
        ValueError: Se o número romano for inválido.
    """
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    anterior = 0

    for letra in reversed(romano):
        if letra not in valores:
            raise ValueError(f"Caractere inválido: {letra}")
        if valores[letra] < anterior:
            total -= valores[letra]
        else:
            total += valores[letra]
        anterior = valores[letra]

    return total

def main():
    """
    Função principal que solicita ao usuário um número romano e exibe seu valor inteiro.
    """
    romano = input("Digite um número romano: ").strip().upper()
    try:
        inteiro = romano_para_inteiro(romano)
        print(f"O número romano {romano} é igual a {inteiro} em decimal.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()