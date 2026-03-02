import math

def calcular_distancia(ponto1, ponto2):
    """
    Calcula a distância entre dois pontos no plano cartesiano.

    Args:
        ponto1 (tuple): Tupla contendo as coordenadas (x, y) do primeiro ponto.
        ponto2 (tuple): Tupla contendo as coordenadas (x, y) do segundo ponto.

    Returns:
        float: A distância entre os dois pontos.
    """
    x1, y1 = ponto1
    x2, y2 = ponto2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calcular_ponto_medio(ponto1, ponto2):
    """
    Calcula o ponto médio do segmento que une dois pontos no plano cartesiano.

    Args:
        ponto1 (tuple): Tupla contendo as coordenadas (x, y) do primeiro ponto.
        ponto2 (tuple): Tupla contendo as coordenadas (x, y) do segundo ponto.

    Returns:
        tuple: As coordenadas (x, y) do ponto médio.
    """
    x1, y1 = ponto1
    x2, y2 = ponto2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def main():
    """
    Função principal que solicita ao usuário dois pontos e calcula a distância entre eles e o ponto médio.
    """
    ponto1 = tuple(map(float, input("Digite as coordenadas do primeiro ponto (x y): ").split()))
    ponto2 = tuple(map(float, input("Digite as coordenadas do segundo ponto (x y): ").split()))

    distancia = calcular_distancia(ponto1, ponto2)
    ponto_medio = calcular_ponto_medio(ponto1, ponto2)

    print(f"Distância entre os pontos: {distancia:.2f}")
    print(f"Ponto médio: {ponto_medio}")

if __name__ == '__main__':
    main()