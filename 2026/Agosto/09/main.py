def calcular_despesas(despesas, moradores):
    """
    Divide as despesas de uma casa proporcionalmente entre os moradores.

    Args:
        despesas (dict): Um dicionário onde as chaves são os nomes das despesas e os valores são os valores das despesas.
        moradores (list): Uma lista com os nomes dos moradores.

    Returns:
        dict: Um dicionário onde as chaves são os nomes dos moradores e os valores são os valores que cada um deve pagar.
    """
    total_despesas = sum(despesas.values())
    numero_moradores = len(moradores)
    despesa_por_morador = total_despesas / numero_moradores

    distribuicao = {morador: despesa_por_morador for morador in moradores}
    return distribuicao


def main():
    despesas = {
        'luz': 150.00,
        'internet': 100.00,
        'aluguel': 1200.00
    }
    moradores = ['João', 'Maria', 'Carlos']

    distribuicao = calcular_despesas(despesas, moradores)

    print("Distribuição das despesas:")
    for morador, valor in distribuicao.items():
        print(f"{morador}: R$ {valor:.2f}")


if __name__ == '__main__':
    main()