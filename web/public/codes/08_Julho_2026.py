def calcular_perimetro_poligono(numero_lados, comprimento_lado):
    """
    Calcula o perímetro de um polígono regular.

    Args:
        numero_lados (int): O número de lados do polígono.
        comprimento_lado (float): O comprimento de cada lado do polígono.

    Returns:
        float: O perímetro do polígono.
    """
    if numero_lados < 3:
        raise ValueError("Um polígono deve ter pelo menos 3 lados.")
    
    return numero_lados * comprimento_lado

def main():
    try:
        numero_lados = int(input("Digite o número de lados do polígono: "))
        comprimento_lado = float(input("Digite o comprimento de cada lado: "))
        
        perimetro = calcular_perimetro_poligono(numero_lados, comprimento_lado)
        print(f"O perímetro do polígono é: {perimetro}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()