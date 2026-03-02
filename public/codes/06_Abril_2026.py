"""
conversor_polegadas_para_cm.py

Este script converte um valor dado em polegadas para centímetros.
A conversão é realizada com precisão decimal.
"""

def polegadas_para_centimetros(polegadas):
    """
    Converte o valor de polegadas para centímetros.

    Args:
        polegadas (float): O valor em polegadas a ser convertido.

    Returns:
        float: O valor convertido em centímetros.
    """
    return polegadas * 2.54

def main():
    """
    Função principal do script. Solicita ao usuário um valor em polegadas,
    realiza a conversão para centímetros e exibe o resultado.
    """
    try:
        polegadas = float(input("Digite o valor em polegadas: "))
        centimetros = polegadas_para_centimetros(polegadas)
        print(f"{polegadas} polegadas é igual a {centimetros:.2f} centímetros.")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == '__main__':
    main()