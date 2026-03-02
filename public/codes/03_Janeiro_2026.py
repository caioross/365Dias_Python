def contar_vogais(frase):
    """
    Conta o número de vogais em uma frase, ignorando maiúsculas e minúsculas.

    Args:
        frase (str): A frase na qual as vogais serão contadas.

    Returns:
        int: O número total de vogais na frase.
    """
    vogais = 'aeiou'
    frase = frase.lower()
    return sum(1 for char in frase if char in vogais)

def main():
    frase = input("Digite uma frase: ")
    total_vogais = contar_vogais(frase)
    print(f"Total de vogais na frase: {total_vogais}")

if __name__ == '__main__':
    main()