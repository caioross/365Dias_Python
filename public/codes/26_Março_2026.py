def luhn_checksum(card_number):
    """
    Calcula o checksum do número de cartão de crédito usando o Algoritmo de Luhn.

    :param card_number: Número do cartão de crédito como string.
    :return: True se o número é válido, False caso contrário.
    """
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_valid_credit_card(card_number):
    """
    Verifica se um número de cartão de crédito é válido.

    :param card_number: Número do cartão de crédito como string.
    :return: True se o número é válido, False caso contrário.
    """
    return luhn_checksum(card_number) == 0

def main():
    """
    Função principal que solicita ao usuário um número de cartão de crédito
    e verifica sua validade usando o Algoritmo de Luhn.
    """
    card_number = input("Digite o número do cartão de crédito: ")
    if is_valid_credit_card(card_number):
        print("O número do cartão de crédito é válido.")
    else:
        print("O número do cartão de crédito é inválido.")

if __name__ == '__main__':
    main()