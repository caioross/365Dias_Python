def calcular_digito_verificador(pis_pasep):
    """
    Calcula o dígito verificador de um número de PIS/PASEP.

    :param pis_pasep: String contendo os 10 primeiros dígitos do PIS/PASEP.
    :return: O dígito verificador calculado.
    """
    if len(pis_pasep) != 10 or not pis_pasep.isdigit():
        raise ValueError("O número de PIS/PASEP deve conter exatamente 10 dígitos numéricos.")

    pesos = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(digito) * peso for digito, peso in zip(pis_pasep, pesos))
    resto = soma % 11
    digito = 11 - resto

    if digito == 10 or digito == 11:
        digito = 0

    return str(digito)


def validar_pis_pasep(pis_pasep):
    """
    Valida um número de PIS/PASEP completo.

    :param pis_pasep: String contendo o número completo de 11 dígitos do PIS/PASEP.
    :return: True se o número for válido, False caso contrário.
    """
    if len(pis_pasep) != 11 or not pis_pasep.isdigit():
        return False

    digitos = pis_pasep[:10]
    digito_verificador_calculado = calcular_digito_verificador(digitos)
    digito_verificador_informado = pis_pasep[10]

    return digito_verificador_calculado == digito_verificador_informado


if __name__ == '__main__':
    def main():
        pis_pasep = input("Digite o número de PIS/PASEP (11 dígitos): ")
        if validar_pis_pasep(pis_pasep):
            print("O número de PIS/PASEP é válido.")
        else:
            print("O número de PIS/PASEP é inválido.")

    main()