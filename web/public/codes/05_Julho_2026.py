"""
Script para validar números de CNH (Carteira Nacional de Habilitação) brasileiros.
Este script verifica se o número de CNH fornecido segue o padrão de cálculo oficial.

Uso:
    python validador_cnh_brasileira.py <numero_cnh>
"""

import sys

def calcular_digito_verificador(cnh):
    """
    Calcula o dígito verificador de um número de CNH.

    Args:
        cnh (str): Número de CNH sem o dígito verificador.

    Returns:
        int: Dígito verificador calculado.
    """
    pesos = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    soma = 0

    for i in range(18):
        soma += int(cnh[i]) * pesos[i]

    resto = soma % 11
    digito = 11 - resto

    if digito > 9:
        digito = 0

    return digito

def validar_cnh(cnh):
    """
    Valida um número de CNH.

    Args:
        cnh (str): Número de CNH a ser validado.

    Returns:
        bool: True se o número de CNH é válido, False caso contrário.
    """
    if len(cnh) != 19:
        return False

    numero_cnh = cnh[:18]
    digito_verificador = cnh[18]

    if not numero_cnh.isdigit() or not digito_verificador.isdigit():
        return False

    digito_calculado = calcular_digito_verificador(numero_cnh)

    return int(digito_verificador) == digito_calculado

def main():
    """
    Função principal do script.
    """
    if len(sys.argv) != 2:
        print("Uso: python validador_cnh_brasileira.py <numero_cnh>")
        sys.exit(1)

    numero_cnh = sys.argv[1]

    if validar_cnh(numero_cnh):
        print("O número de CNH é válido.")
    else:
        print("O número de CNH é inválido.")

if __name__ == '__main__':
    main()