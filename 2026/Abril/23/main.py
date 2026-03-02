import requests
from bs4 import BeautifulSoup
import pandas as pd

def extrair_tabelas(url):
    """
    Captura todas as tabelas HTML de uma URL e as converte em arquivos CSV individuais.

    Args:
        url (str): A URL do site a partir do qual as tabelas devem ser extraídas.

    Returns:
        None
    """
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

    soup = BeautifulSoup(response.content, 'html.parser')
    tabelas = soup.find_all('table')

    for i, tabela in enumerate(tabelas):
        df = pd.read_html(str(tabela))[0]  # Converte a tabela HTML para DataFrame
        nome_arquivo = f'tabela_{i + 1}.csv'
        df.to_csv(nome_arquivo, index=False)
        print(f'Tabela {i + 1} salva como {nome_arquivo}')

def main():
    url = input("Digite a URL do site: ")
    extrair_tabelas(url)

if __name__ == '__main__':
    main()