from haversine import haversine, Unit

def calcular_distancia(coord1, coord2):
    """
    Função para calcular a distância entre duas coordenadas geográficas usando a fórmula de Haversine.
    :param coord1: Coordenada 1 (latitude, longitude)
    :param coord2: Coordenada 2 (latitude, longitude)
    :return: Distância em quilômetros
    """
    try:
        distancia = haversine(coord1, coord2, unit=Unit.KILOMETERS)
        return distancia
    except Exception as e:
        print(f"Erro ao calcular a distância: {e}")
        return None

def main():
    """
    Função principal para interagir com o usuário e calcular a distância entre duas coordenadas.
    """
    print("Calculadora de Distância Geográfica\n")
    
    # Entrada das coordenadas
    lat1 = float(input("Digite a latitude da coordenada 1: "))
    lon1 = float(input("Digite a longitude da coordenada 1: "))
    lat2 = float(input("Digite a latitude da coordenada 2: "))
    lon2 = float(input("Digite a longitude da coordenada 2: "))

    # Calcula a distância entre as coordenadas
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)
    
    distancia = calcular_distancia(coord1, coord2)
    
    if distancia is not None:
        print(f"\nA distância entre as coordenadas é: {distancia:.2f} km")

if __name__ == "__main__":
    main()
