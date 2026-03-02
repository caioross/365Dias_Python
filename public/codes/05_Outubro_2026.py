import re

def validar_iban(iban):
    """
    Valida se um código IBAN é válido estruturalmente.

    Args:
        iban (str): O código IBAN a ser validado.

    Returns:
        bool: True se o IBAN for válido, False caso contrário.
    """
    # Remover espaços e converter para maiúsculas
    iban = iban.replace(" ", "").upper()

    # Verificar se o IBAN tem o tamanho mínimo de 5 caracteres
    if len(iban) < 5:
        return False

    # Verificar se o IBAN começa com duas letras
    if not re.match(r'^[A-Z]{2}', iban):
        return False

    # Mover os quatro primeiros caracteres para o final
    iban = iban[4:] + iban[:4]

    # Converter letras para números (A=10, B=11, ..., Z=35)
    iban_converted = ''.join(str(ord(char) - 55) if char.isalpha() else char for char in iban)

    # Verificar se o número resultante é divisível por 97
    return int(iban_converted) % 97 == 1

def main():
    """
    Função principal para testar a validação de IBAN.
    """
    test_iban = "PT50000201231234567890154"
    if validar_iban(test_iban):
        print(f"O IBAN {test_iban} é válido.")
    else:
        print(f"O IBAN {test_iban} é inválido.")

if __name__ == '__main__':
    main()