import requests
from bs4 import BeautifulSoup
import time

class EcommerceMonitor:
    """
    Classe para monitorar a disponibilidade de produtos em uma loja de ecommerce.
    """
    
    def __init__(self, product_url, check_interval=60):
        """
        Inicializa o monitor com a URL do produto e o intervalo de verificação.
        
        :param product_url: URL do produto a ser monitorado.
        :param check_interval: Intervalo de tempo (em segundos) entre as verificações.
        """
        self.product_url = product_url
        self.check_interval = check_interval
        self.last_status = None

    def fetch_product_status(self):
        """
        Faz uma requisição à URL do produto e verifica se está disponível.
        
        :return: Status do produto ('disponível' ou 'esgotado').
        """
        response = requests.get(self.product_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Supondo que o status do produto esteja em uma tag com a classe 'product-status'
        status_tag = soup.find(class_='product-status')
        if status_tag:
            return status_tag.text.strip().lower()
        return 'disponível'  # Caso não encontre, assume como disponível

    def monitor_product(self):
        """
        Monitora o produto periodicamente e avisa quando ele volta a ficar disponível.
        """
        while True:
            current_status = self.fetch_product_status()
            if current_status == 'disponível' and self.last_status == 'esgotado':
                print(f"Produto disponível! Verifique: {self.product_url}")
            self.last_status = current_status
            time.sleep(self.check_interval)

def main():
    """
    Função principal para iniciar o monitoramento do estoque.
    """
    product_url = 'https://exemplo.com/produto'  # Substituir pela URL real do produto
    monitor = EcommerceMonitor(product_url)
    monitor.monitor_product()

if __name__ == '__main__':
    main()