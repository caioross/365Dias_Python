"""
buscador_clima_historico.py

Script para consultar e exibir a temperatura média de uma cidade em uma data específica no passado usando uma API de clima.
"""

import requests

def obter_temperatura_media(cidade, data, chave_api):
    """
    Obtém a temperatura média de uma cidade em uma data específica no passado.

    :param cidade: Nome da cidade (str)
    :param data: Data no formato YYYY-MM-DD (str)
    :param chave_api: Chave de API para o serviço de clima (str)
    :return: Temperatura média (float) ou None se a consulta falhar
    """
    url = f"http://api.weatherapi.com/v1/history.json?key={chave_api}&q={cidade}&dt={data}"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        temperatura_media = dados['forecast']['forecastday'][0]['day']['avgtemp_c']
        return temperatura_media
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Erro ao obter dados de clima: {e}")
        return None

def main():
    """
    Função principal que executa o script.
    """
    cidade = input("Digite o nome da cidade: ")
    data = input("Digite a data (YYYY-MM-DD): ")
    chave_api = input("Digite sua chave de API: ")

    temperatura_media = obter_temperatura_media(cidade, data, chave_api)
    if temperatura_media is not None:
        print(f"A temperatura média em {cidade} em {data} foi {temperatura_media}°C.")
    else:
        print("Não foi possível obter a temperatura média.")

if __name__ == '__main__':
    main()