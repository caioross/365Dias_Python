"""
buscador_clima_maritimo.py

Script para consultar temperatura da água e altura de ondas para praias específicas utilizando uma API.
"""

import requests

def get_weather_data(api_url, api_key, beach_name):
    """
    Consulta a API para obter dados de clima marítimo.

    :param api_url: URL base da API.
    :param api_key: Chave de API para autenticação.
    :param beach_name: Nome da praia para a qual se deseja obter os dados.
    :return: Dados de clima marítimo em formato JSON ou None se a consulta falhar.
    """
    params = {
        'q': beach_name,
        'appid': api_key,
        'units': 'metric'  # Temperatura em Celsius
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
        return None

def parse_weather_data(weather_data):
    """
    Parseia os dados de clima marítimo para extrair temperatura da água e altura de ondas.

    :param weather_data: Dados de clima marítimo em formato JSON.
    :return: Um dicionário com temperatura da água e altura de ondas ou None se os dados não estiverem disponíveis.
    """
    if not weather_data:
        return None

    try:
        water_temperature = weather_data['main']['temp']
        wave_height = weather_data['wave_height']  # Supondo que a API retorne esta informação
        return {
            'water_temperature': water_temperature,
            'wave_height': wave_height
        }
    except KeyError:
        print("Dados de clima marítimo incompletos.")
        return None

def main():
    """
    Função principal para executar o script.
    """
    api_url = 'https://api.example.com/weather'  # Substituir pela URL real da API
    api_key = 'your_api_key_here'  # Substituir pela chave real da API
    beach_name = 'Copacabana'  # Nome da praia para consulta

    weather_data = get_weather_data(api_url, api_key, beach_name)
    parsed_data = parse_weather_data(weather_data)

    if parsed_data:
        print(f"Temperatura da água em {beach_name}: {parsed_data['water_temperature']}°C")
        print(f"Altura de ondas em {beach_name}: {parsed_data['wave_height']}m")

if __name__ == '__main__':
    main()