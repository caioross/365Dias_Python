"""
gerador_encurtador_url_simples.py

Script para gerar um redirecionamento simples usando a API do Bitly.
Requer uma chave de acesso ao Bitly, que pode ser obtida em https://bitly.com/.
"""

import requests

def encurtar_url(url_longa, access_token):
    """
    Encurta uma URL usando a API do Bitly.

    Args:
        url_longa (str): A URL que deseja encurtar.
        access_token (str): O token de acesso ao Bitly.

    Returns:
        str: A URL encurtada.
    """
    endpoint = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "long_url": url_longa
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    response.raise_for_status()
    return response.json().get('link')

def main():
    """
    Função principal que solicita uma URL ao usuário, encurta-a usando a API do Bitly,
    e exibe a URL encurtada.
    """
    access_token = input("Digite seu token de acesso ao Bitly: ")
    url_longa = input("Digite a URL que deseja encurtar: ")
    try:
        url_encurtada = encurtar_url(url_longa, access_token)
        print(f"URL encurtada: {url_encurtada}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao encurtar a URL: {e}")

if __name__ == '__main__':
    main()