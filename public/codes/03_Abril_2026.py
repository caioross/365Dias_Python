def sao_anagramas(frase1: str, frase2: str) -> bool:
    """
    Verifica se duas frases são anagramas uma da outra, desconsiderando espaços.

    Args:
        frase1 (str): A primeira frase a ser comparada.
        frase2 (str): A segunda frase a ser comparada.

    Returns:
        bool: True se as frases são anagramas, False caso contrário.
    """
    # Remove espaços e converte para minúsculas
    frase1_cleaned = frase1.replace(" ", "").lower()
    frase2_cleaned = frase2.replace(" ", "").lower()

    # Verifica se os caracteres ordenados das frases são iguais
    return sorted(frase1_cleaned) == sorted(frase2_cleaned)

def main():
    frase1 = input("Digite a primeira frase: ")
    frase2 = input("Digite a segunda frase: ")

    if sao_anagramas(frase1, frase2):
        print("As frases são anagramas.")
    else:
        print("As frases não são anagramas.")

if __name__ == '__main__':
    main()