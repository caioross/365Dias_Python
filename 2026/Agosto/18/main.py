"""
conversor_unidades_cozinha.py

Este script permite a conversão de medidas de ingredientes comuns na cozinha, incluindo:
- Xícaras para gramas
- Colheres de sopa para gramas
- Gramas para xícaras (para certos ingredientes)
- Gramas para colheres de sopa (para certos ingredientes)

O script utiliza conversões médias e pode não ser precisa para todos os ingredientes.
"""

def xicara_para_gramas(ingrediente, xicaras):
    """
    Converte xícaras para gramas com base no ingrediente.

    :param ingrediente: Nome do ingrediente (str)
    :param xicaras: Quantidade em xícaras (float)
    :return: Quantidade em gramas (float)
    """
    conversoes = {
        'arroz': 180,
        'feijão': 160,
        'açúcar': 200,
        'farinha': 120,
        'óleo': 230
    }
    return xicaras * conversoes.get(ingrediente.lower(), 0)

def colher_de_sopa_para_gramas(ingrediente, colheres):
    """
    Converte colheres de sopa para gramas com base no ingrediente.

    :param ingrediente: Nome do ingrediente (str)
    :param colheres: Quantidade em colheres de sopa (float)
    :return: Quantidade em gramas (float)
    """
    conversoes = {
        'manteiga': 12,
        'sal': 6,
        'azeite': 7
    }
    return colheres * conversoes.get(ingrediente.lower(), 0)

def gramas_para_xicara(ingrediente, gramas):
    """
    Converte gramas para xícaras com base no ingrediente.

    :param ingrediente: Nome do ingrediente (str)
    :param gramas: Quantidade em gramas (float)
    :return: Quantidade em xícaras (float)
    """
    conversoes = {
        'arroz': 180,
        'feijão': 160,
        'açúcar': 200,
        'farinha': 120,
        'óleo': 230
    }
    return gramas / conversoes.get(ingrediente.lower(), 1)

def gramas_para_colher_de_sopa(ingrediente, gramas):
    """
    Converte gramas para colheres de sopa com base no ingrediente.

    :param ingrediente: Nome do ingrediente (str)
    :param gramas: Quantidade em gramas (float)
    :return: Quantidade em colheres de sopa (float)
    """
    conversoes = {
        'manteiga': 12,
        'sal': 6,
        'azeite': 7
    }
    return gramas / conversoes.get(ingrediente.lower(), 1)

def main():
    print("Conversor de Unidades de Cozinha")
    print("1. Xícaras para Gramas")
    print("2. Colheres de Sopa para Gramas")
    print("3. Gramas para Xícaras")
    print("4. Gramas para Colheres de Sopa")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        ingrediente = input("Ingrediente: ")
        xicaras = float(input("Quantidade em xícaras: "))
        print(f"{xicaras} xícaras de {ingrediente} é aproximadamente {xicara_para_gramas(ingrediente, xicaras)} gramas.")
    elif escolha == '2':
        ingrediente = input("Ingrediente: ")
        colheres = float(input("Quantidade em colheres de sopa: "))
        print(f"{colheres} colheres de sopa de {ingrediente} é aproximadamente {colher_de_sopa_para_gramas(ingrediente, colheres)} gramas.")
    elif escolha == '3':
        ingrediente = input("Ingrediente: ")
        gramas = float(input("Quantidade em gramas: "))
        print(f"{gramas} gramas de {ingrediente} é aproximadamente {gramas_para_xicara(ingrediente, gramas)} xícaras.")
    elif escolha == '4':
        ingrediente = input("Ingrediente: ")
        gramas = float(input("Quantidade em gramas: "))
        print(f"{gramas} gramas de {ingrediente} é aproximadamente {gramas_para_colher_de_sopa(ingrediente, gramas)} colheres de sopa.")
    else:
        print("Opção inválida.")

if __name__ == '__main__':
    main()