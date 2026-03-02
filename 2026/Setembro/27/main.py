"""
Script para verificar se uma URL consta em listas negras de phishing ou malware usando uma API.
"""

import requests

def is_url_malicious(url):
    """
    Verifica se uma URL é maliciosa consultando uma API de listas negras.

    Args:
        url (str): A URL a ser verificada.

    Returns:
        bool: True se a URL é maliciosa, False caso contrário.
    """
    # Substitua 'https://api.exemplo.com/check' pela URL real da API que você deseja usar
    api_url = 'https://api.exemplo.com/check'
    params = {'url': url}
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        # Supondo que a API retorne um JSON com um campo 'malicious' que é True ou False
        return data.get('malicious', False)
    except requests.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
        return False

def main():
    """
    Função principal que solicita uma URL ao usuário e verifica se ela é maliciosa.
    """
    url = input("Digite a URL que deseja verificar: ")
    if is_url_malicious(url):
        print("A URL é maliciosa.")
    else:
        print("A URL não é maliciosa.")

if __name__ == '__main__':
    main()