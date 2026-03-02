def calcular_consumo_combustivel(distancia, consumo_medio):
    """
    Calcula a quantidade de combustível gasta em uma viagem.

    Args:
        distancia (float): A distância da viagem em quilômetros.
        consumo_medio (float): O consumo médio do carro em km/l.

    Returns:
        float: A quantidade de combustível gasta em litros.
    """
    if consumo_medio <= 0:
        raise ValueError("O consumo médio deve ser maior que zero.")
    return distancia / consumo_medio

def main():
    try:
        distancia = float(input("Digite a distância da viagem em quilômetros: "))
        consumo_medio = float(input("Digite o consumo médio do carro em km/l: "))

        consumo = calcular_consumo_combustivel(distancia, consumo_medio)
        print(f"Serão necessários {consumo:.2f} litros de combustível para a viagem.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()