def calcular_preco_venda(custo, taxa_imposto, margem_lucro):
    """
    Calcula o preço de venda de um item baseado no custo, impostos e margem de lucro desejada.

    :param custo: O custo de aquisição do item (float).
    :param taxa_imposto: A taxa de imposto a ser aplicada (float, em decimal, por exemplo, 0.20 para 20%).
    :param margem_lucro: A margem de lucro desejada (float, em decimal, por exemplo, 0.30 para 30%).
    :return: O preço de venda calculado (float).
    """
    imposto = custo * taxa_imposto
    custo_total = custo + imposto
    preco_venda = custo_total / (1 - margem_lucro)
    return preco_venda

def main():
    """
    Função principal que solicita ao usuário os dados necessários para calcular o preço de venda
    e exibe o resultado.
    """
    try:
        custo = float(input("Digite o custo do item: "))
        taxa_imposto = float(input("Digite a taxa de imposto (em decimal, por exemplo, 0.20 para 20%): "))
        margem_lucro = float(input("Digite a margem de lucro desejada (em decimal, por exemplo, 0.30 para 30%): "))

        preco_venda = calcular_preco_venda(custo, taxa_imposto, margem_lucro)
        print(f"O preço de venda do item deve ser: R$ {preco_venda:.2f}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == '__main__':
    main()