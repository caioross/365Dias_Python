import requests
import time
from datetime import datetime

def check_site(url):
    """
    Verifica se um site está respondendo corretamente.
    
    Args:
        url (str): A URL do site a ser verificado.
    
    Returns:
        bool: True se o site estiver respondendo, False caso contrário.
    """
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def monitor_sites(sites):
    """
    Monitora uma lista de sites, verificando se estão respondendo a cada 5 minutos.
    
    Args:
        sites (list): Uma lista de URLs dos sites a serem monitorados.
    """
    while True:
        for site in sites:
            is_up = check_site(site)
            status = "UP" if is_up else "DOWN"
            print(f"{datetime.now()} - {site} is {status}")
        time.sleep(300)  # Espera 5 minutos (300 segundos)

def main():
    """
    Função principal que define a lista de sites a serem monitorados e inicia o monitoramento.
    """
    sites_to_monitor = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.python.org"
    ]
    monitor_sites(sites_to_monitor)

if __name__ == '__main__':
    main()