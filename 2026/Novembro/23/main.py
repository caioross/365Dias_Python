"""
conversor_unidades_energia.py

Este script fornece funções para converter valores entre as unidades de energia:
Joule, Caloria, BTU e Kilowatt-hora.
"""

def joule_to_caloria(joule):
    """
    Converte Joules para Calorias.

    :param joule: Valor em Joules
    :return: Valor convertido em Calorias
    """
    return joule / 4184

def joule_to_btu(joule):
    """
    Converte Joules para BTU.

    :param joule: Valor em Joules
    :return: Valor convertido em BTU
    """
    return joule / 1055.06

def joule_to_kwh(joule):
    """
    Converte Joules para Kilowatt-hora.

    :param joule: Valor em Joules
    :return: Valor convertido em Kilowatt-hora
    """
    return joule / 3600000

def caloria_to_joule(caloria):
    """
    Converte Calorias para Joules.

    :param caloria: Valor em Calorias
    :return: Valor convertido em Joules
    """
    return caloria * 4184

def caloria_to_btu(caloria):
    """
    Converte Calorias para BTU.

    :param caloria: Valor em Calorias
    :return: Valor convertido em BTU
    """
    return caloria * 0.252

def caloria_to_kwh(caloria):
    """
    Converte Calorias para Kilowatt-hora.

    :param caloria: Valor em Calorias
    :return: Valor convertido em Kilowatt-hora
    """
    return caloria * 0.001163

def btu_to_joule(btu):
    """
    Converte BTU para Joules.

    :param btu: Valor em BTU
    :return: Valor convertido em Joules
    """
    return btu * 1055.06

def btu_to_caloria(btu):
    """
    Converte BTU para Calorias.

    :param btu: Valor em BTU
    :return: Valor convertido em Calorias
    """
    return btu / 0.252

def btu_to_kwh(btu):
    """
    Converte BTU para Kilowatt-hora.

    :param btu: Valor em BTU
    :return: Valor convertido em Kilowatt-hora
    """
    return btu * 0.000293071

def kwh_to_joule(kwh):
    """
    Converte Kilowatt-hora para Joules.

    :param kwh: Valor em Kilowatt-hora
    :return: Valor convertido em Joules
    """
    return kwh * 3600000

def kwh_to_caloria(kwh):
    """
    Converte Kilowatt-hora para Calorias.

    :param kwh: Valor em Kilowatt-hora
    :return: Valor convertido em Calorias
    """
    return kwh / 0.001163

def kwh_to_btu(kwh):
    """
    Converte Kilowatt-hora para BTU.

    :param kwh: Valor em Kilowatt-hora
    :return: Valor convertido em BTU
    """
    return kwh / 0.000293071

def main():
    """
    Função principal para demonstrar o uso das funções de conversão.
    """
    value = 100  # Exemplo de valor a ser convertido

    print(f"{value} Joules é igual a:")
    print(f"{joule_to_caloria(value)} Calorias")
    print(f"{joule_to_btu(value)} BTU")
    print(f"{joule_to_kwh(value)} Kilowatt-hora")

    print(f"\n{value} Calorias é igual a:")
    print(f"{caloria_to_joule(value)} Joules")
    print(f"{caloria_to_btu(value)} BTU")
    print(f"{caloria_to_kwh(value)} Kilowatt-hora")

    print(f"\n{value} BTU é igual a:")
    print(f"{btu_to_joule(value)} Joules")
    print(f"{btu_to_caloria(value)} Calorias")
    print(f"{btu_to_kwh(value)} Kilowatt-hora")

    print(f"\n{value} Kilowatt-hora é igual a:")
    print(f"{kwh_to_joule(value)} Joules")
    print(f"{kwh_to_caloria(value)} Calorias")
    print(f"{kwh_to_btu(value)} BTU")

if __name__ == '__main__':
    main()