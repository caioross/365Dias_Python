def calcular_cedulas(saque):
    """
    Calcula o menor número de cédulas de 100, 50, 20, 10, 5 e 2 para um valor de saque.

    Args:
        saque (int): O valor do saque a ser realizado.

    Returns:
        dict: Um dicionário com as cédulas como chaves e a quantidade como valores.
    """
    cedulas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}
    for cedula in cedulas:
        cedulas[cedula] = saque // cedula
        saque %= cedula
    return cedulas

def main():
    """
    Função principal que solicita o valor do saque ao usuário e exibe a quantidade
    de cédulas necessárias para realizar o saque.
    """
    try:
        valor_saque = int(input("Digite o valor do saque: "))
        if valor_saque < 2:
            print("O valor do saque deve ser pelo menos 2.")
            return
        
        resultado = calcular_cedulas(valor_saque)
        print("Cédulas necessárias:")
        for cedula, quantidade in resultado.items():
            print(f"{cedula}: {quantidade}")
    
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == '__main__':
    main()