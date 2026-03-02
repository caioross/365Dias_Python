def cm_para_polegadas(centimetros):
    """
    Converte um valor de centímetros para polegadas.

    Args:
        centimetros (float): O valor em centímetros que deseja converter.

    Returns:
        float: O valor convertido em polegadas.
    """
    polegadas = centimetros / 2.54
    return polegadas

def main():
    """
    Função principal que solicita ao usuário um valor em centímetros,
    converte esse valor para polegadas e exibe o resultado.
    """
    try:
        centimetros = float(input("Digite o valor em centímetros: "))
        polegadas = cm_para_polegadas(centimetros)
        print(f"{centimetros} centímetros é igual a {polegadas:.2f} polegadas.")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == '__main__':
    main()