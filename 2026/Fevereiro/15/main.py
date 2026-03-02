import re

def extrair_links_html(caminho_arquivo):
    """
    Extrai todos os links presentes nas tags <a> de um arquivo HTML local.

    Args:
        caminho_arquivo (str): O caminho para o arquivo HTML.

    Returns:
        list: Uma lista de strings contendo os URLs encontrados.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo_html = arquivo.read()
        
        # Expressão regular para encontrar links nas tags <a>
        padrao = r'<a\s+[^>]*href="([^"]+)"'
        links = re.findall(padrao, conteudo_html)
        
        return links
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return []

def main():
    """
    Função principal para executar o script de extração de links HTML.
    """
    caminho_arquivo = 'exemplo.html'  # Substitua pelo caminho do seu arquivo HTML
    links = extrair_links_html(caminho_arquivo)
    
    if links:
        print("Links encontrados:")
        for link in links:
            print(link)
    else:
        print("Nenhum link encontrado ou erro ao processar o arquivo.")

if __name__ == '__main__':
    main()