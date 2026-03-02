"""
rastreador_papai_noel_simulado.py

Este script simula a localização fictícia do trenó de Papai Noel e fornece curiosidades sobre os países visitados.
"""

import random

def obter_localizacao_ficticia():
    """
    Gera uma localização fictícia para o trenó de Papai Noel.

    Returns:
        tuple: Uma tupla contendo as coordenadas (latitude, longitude) fictícias.
    """
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return latitude, longitude

def obter_curiosidade_sobre_pais(pais):
    """
    Retorna uma curiosidade fictícia sobre um país.

    Args:
        pais (str): O nome do país.

    Returns:
        str: Uma curiosidade sobre o país.
    """
    curiosidades = {
        "Brasil": "O Brasil é o país com maior número de favelas do mundo.",
        "Rússia": "A Rússia é o país mais alto do mundo.",
        "Canadá": "O Canadá é o segundo maior país do mundo por área territorial.",
        "China": "A China é o país mais populoso do mundo.",
        "Austrália": "A Austrália é o país mais alto do mundo.",
        "Alemanha": "A Alemanha é o país mais industrializado do mundo.",
        "Japão": "O Japão é o país com maior densidade demográfica do mundo.",
        "Argentina": "A Argentina é o país mais alto do mundo.",
        "Índia": "A Índia é o país com maior número de vegetarianos do mundo.",
        "México": "O México é o país com maior número de piratas do mundo."
    }
    return curiosidades.get(pais, "Desculpe, não temos curiosidade sobre esse país.")

def main():
    """
    Função principal que simula a localização do trenó e exibe curiosidades sobre os países visitados.
    """
    paises_visitados = ["Brasil", "Rússia", "Canadá", "China", "Austrália", "Alemanha", "Japão", "Argentina", "Índia", "México"]
    
    for pais in paises_visitados:
        latitude, longitude = obter_localizacao_ficticia()
        curiosidade = obter_curiosidade_sobre_pais(pais)
        print(f"Localização do trenó em {pais}: ({latitude:.2f}, {longitude:.2f})")
        print(f"Curiosidade sobre {pais}: {curiosidade}\n")

if __name__ == '__main__':
    main()