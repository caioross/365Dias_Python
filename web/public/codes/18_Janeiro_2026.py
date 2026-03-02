def calcular_preco_final(preco_original, porcentagem_desconto):
    """
    Calcula o preço final de um produto após aplicar um desconto.

    :param preco_original: float - O preço original do produto.
    :param porcentagem_desconto: float - A porcentagem de desconto a ser aplicada.
    :return: float - O preço final do produto após o desconto.
    """
    if preco_original < 0:
        raise ValueError("O preço original não pode ser negativo.")
    if not (0 <= porcentagem_desconto <= 100):
        raise ValueError("A porcentagem de desconto deve estar entre 0 e 100.")

    desconto = (preco_original * porcentagem_desconto) / 100
    preco_final = preco_original - desconto
    return preco_final

def exibir_preco_final(preco_original, porcentagem_desconto):
    """
    Exibe o preço final do produto após aplicar o desconto e quanto foi economizado.

    :param preco_original: float - O preço original do produto.
    :param porcentagem_desconto: float - A porcentagem de desconto a ser aplicada.
    """
    preco_final = calcular_preco_final(preco_original, porcentagem_desconto)
    economia = preco_original - preco_final

    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Desconto: {porcentagem_desconto}%")
    print(f"Preço final: R$ {preco_final:.2f}")
    print(f"Economia: R$ {economia:.2f}")

def main():
    """
    Função principal que solicita ao usuário o preço original e a porcentagem de desconto,
    e exibe o preço final e a economia.
    """
    try:
        preco_original = float(input("Digite o preço original do produto: "))
        porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))
        exibir_preco_final(preco_original, porcentagem_desconto)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()