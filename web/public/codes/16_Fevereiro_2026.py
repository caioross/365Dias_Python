def sao_anagramas(palavra1, palavra2):
    """
    Verifica se duas palavras são anagramas uma da outra.

    Args:
        palavra1 (str): A primeira palavra a ser comparada.
        palavra2 (str): A segunda palavra a ser comparada.

    Returns:
        bool: True se as palavras são anagramas, False caso contrário.
    """
    return sorted(palavra1) == sorted(palavra2)

def main():
    """
    Função principal que solicita ao usuário duas palavras e verifica se são anagramas.
    """
    palavra1 = input("Digite a primeira palavra: ").strip()
    palavra2 = input("Digite a segunda palavra: ").strip()

    if sao_anagramas(palavra1, palavra2):
        print(f'"{palavra1}" e "{palavra2}" são anagramas.')
    else:
        print(f'"{palavra1}" e "{palavra2}" não são anagramas.')

if __name__ == '__main__':
    main()