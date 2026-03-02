import requests

def verificar_site_online(url):
    """
    Verifica se um site está online ou fora do ar.

    Args:
        url (str): A URL do site que deseja verificar.

    Returns:
        bool: True se o site estiver online, False caso contrário.
    """
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    """
    Função principal que solicita uma URL ao usuário e verifica se o site está online.
    """
    url = input("Digite a URL do site que deseja verificar: ")
    if verificar_site_online(url):
        print(f"O site {url} está online.")
    else:
        print(f"O site {url} está fora do ar.")

if __name__ == '__main__':
    main()