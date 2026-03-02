def is_bissextum(year):
    """
    Verifica se um ano é bissexto de acordo com as regras do calendário gregoriano.

    Args:
    year (int): O ano a ser verificado.

    Returns:
    bool: True se o ano é bissexto, False caso contrário.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    """
    Função principal que solicita ao usuário um ano e verifica se é bissexto.
    """
    try:
        year = int(input("Digite um ano para verificar se é bissexto: "))
        if is_bissextum(year):
            print(f"O ano {year} é bissexto.")
        else:
            print(f"O ano {year} não é bissexto.")
    except ValueError:
        print("Por favor, insira um ano válido (número inteiro).")

if __name__ == '__main__':
    main()