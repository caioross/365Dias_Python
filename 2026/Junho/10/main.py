import requests

def get_geolocation(ip_address):
    """
    Obtém a geolocalização de um endereço IP.

    Args:
        ip_address (str): O endereço IP para o qual a geolocalização será obtida.

    Returns:
        dict: Um dicionário contendo informações de geolocalização, incluindo cidade e país.
    """
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        response.raise_for_status()
        data = response.json()
        return {
            'city': data.get('city'),
            'country': data.get('country_name')
        }
    except requests.RequestException as e:
        print(f"Erro ao obter a geolocalização: {e}")
        return None

def main():
    """
    Função principal que solicita um endereço IP ao usuário e exibe a cidade e o país associados.
    """
    ip_address = input("Digite o endereço IP para geolocalização: ")
    geolocation = get_geolocation(ip_address)
    if geolocation:
        print(f"Cidade: {geolocation['city']}")
        print(f"País: {geolocation['country']}")
    else:
        print("Não foi possível obter a geolocalização para o endereço IP fornecido.")

if __name__ == '__main__':
    main()