"""
Script para gerar um mapa de calor representando as vendas por cidade.
"""

import folium
from collections import Counter

def gerar_mapa_calor(cidades):
    """
    Gera um mapa de calor com base em uma lista de cidades.

    Args:
        cidades (list): Lista de nomes de cidades.

    Returns:
        folium.Map: Um objeto de mapa com o mapa de calor.
    """
    # Conta a ocorrência de cada cidade
    cidade_counts = Counter(cidades)

    # Coordenadas aproximadas para algumas cidades brasileiras
    cidade_coords = {
        'São Paulo': (-23.5505, -46.6333),
        'Rio de Janeiro': (-22.9068, -43.1729),
        'Belo Horizonte': (-19.8158, -43.9542),
        'Brasília': (-15.7801, -47.8796),
        'Salvador': (-12.9742, -38.5139),
        'Fortaleza': (-3.7097, -38.5078),
        'Porto Alegre': (-30.0370, -51.2293),
        'Curitiba': (-25.4284, -49.2734),
        'Recife': (-8.0543, -34.8813),
        'Belém': (-1.4554, -48.5251)
    }

    # Cria um mapa centrado no Brasil
    mapa = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)

    # Adiciona pontos de calor ao mapa
    for cidade, count in cidade_counts.items():
        if cidade in cidade_coords:
            lat, lon = cidade_coords[cidade]
            folium.CircleMarker(
                location=[lat, lon],
                radius=count * 5,  # Tamanho do marcador proporcional ao número de vendas
                color='red',
                fill=True,
                fill_color='red',
                fill_opacity=0.6,
                popup=f'{cidade}: {count} vendas'
            ).add_to(mapa)

    return mapa

def main():
    """
    Função principal para executar o script.
    """
    # Exemplo de lista de cidades
    cidades = [
        'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília',
        'Salvador', 'Fortaleza', 'Porto Alegre', 'Curitiba',
        'Recife', 'Belém', 'São Paulo', 'Rio de Janeiro', 'Belo Horizonte'
    ]

    # Gera o mapa de calor
    mapa = gerar_mapa_calor(cidades)

    # Salva o mapa em um arquivo HTML
    mapa.save('mapa_calor_vendas.html')
    print("Mapa de calor gerado com sucesso. Abra o arquivo 'mapa_calor_vendas.html' em um navegador.")

if __name__ == '__main__':
    main()