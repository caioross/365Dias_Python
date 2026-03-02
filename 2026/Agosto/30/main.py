import requests
from bs4 import BeautifulSoup

def buscar_vagas_linkedin(palavra_chave, localizacao):
    """
    Busca vagas no LinkedIn com base em uma palavra-chave e localização.

    Args:
        palavra_chave (str): A palavra-chave para a busca de vagas.
        localizacao (str): A localização onde as vagas serão buscadas.

    Returns:
        list: Uma lista de títulos de vagas encontradas.
    """
    url = f"https://www.linkedin.com/jobs/search/?keywords={palavra_chave}&location={localizacao}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")

    soup = BeautifulSoup(response.content, 'html.parser')
    vagas = soup.find_all('h3', class_='base-search-card__title')

    return [vaga.text.strip() for vaga in vagas]

def main():
    """
    Função principal que executa a busca de vagas no LinkedIn.
    """
    palavra_chave = input("Digite a palavra-chave para a busca de vagas: ")
    localizacao = input("Digite a localização para a busca de vagas: ")

    try:
        vagas_encontradas = buscar_vagas_linkedin(palavra_chave, localizacao)
        print("\nVagas encontradas:")
        for vaga in vagas_encontradas:
            print(vaga)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()