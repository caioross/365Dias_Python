from datetime import datetime

def calcular_diferenca_em_dias(data1: str, data2: str) -> int:
    """
    Calcula a diferença em dias entre duas datas.

    Args:
        data1 (str): A primeira data no formato 'AAAA-MM-DD'.
        data2 (str): A segunda data no formato 'AAAA-MM-DD'.

    Returns:
        int: A diferença em dias entre as duas datas.
    """
    formato_data = '%Y-%m-%d'
    data_obj1 = datetime.strptime(data1, formato_data)
    data_obj2 = datetime.strptime(data2, formato_data)
    diferenca = abs((data_obj2 - data_obj1).days)
    return diferenca

def main():
    """
    Função principal que solicita ao usuário duas datas e exibe a diferença em dias entre elas.
    """
    print("Calculadora de Diferença de Datas")
    data1 = input("Digite a primeira data (AAAA-MM-DD): ")
    data2 = input("Digite a segunda data (AAAA-MM-DD): ")

    try:
        diferenca_dias = calcular_diferenca_em_dias(data1, data2)
        print(f"A diferença entre as datas é de {diferenca_dias} dias.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira as datas no formato correto (AAAA-MM-DD).")

if __name__ == '__main__':
    main()