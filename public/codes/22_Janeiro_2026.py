def calcular_gorjeta(total_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta com base no total da conta e na porcentagem desejada.

    Args:
        total_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta desejada.

    Returns:
        float: O valor da gorjeta.
    """
    if total_conta < 0:
        raise ValueError("O total da conta não pode ser negativo.")
    if porcentagem_gorjeta < 0:
        raise ValueError("A porcentagem da gorjeta não pode ser negativa.")
    
    return (total_conta * porcentagem_gorjeta) / 100

def main():
    """
    Função principal que interage com o usuário para calcular a gorjeta.
    """
    try:
        total_conta = float(input("Digite o total da conta: "))
        porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta desejada: "))
        
        gorjeta = calcular_gorjeta(total_conta, porcentagem_gorjeta)
        print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()