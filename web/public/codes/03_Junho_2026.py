import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re

def gerar_nuvem_palavras(texto):
    """
    Gera uma imagem WordCloud (nuvem de palavras) a partir de um texto fornecido.

    Args:
        texto (str): O texto do qual a nuvem de palavras será gerada.

    Returns:
        None: A função exibe a imagem da WordCloud.
    """
    # Limpeza do texto: remover pontuação e converter para minúsculas
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = texto.lower()

    # Tokenização: dividir o texto em palavras
    palavras = texto.split()

    # Contagem de palavras
    frequencia_palavras = Counter(palavras)

    # Criação da WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(frequencia_palavras)

    # Exibição da WordCloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def main():
    """
    Função principal que carrega um texto e gera a nuvem de palavras.
    """
    # Exemplo de texto: substitua pelo conteúdo do livro ou artigo desejado
    texto_exemplo = """
    Python é uma linguagem de programação de alto nível, interpretada e de propósito geral. 
    Foi criada por Guido van Rossum e lançada pela primeira vez em 1991. Python é conhecida por sua sintaxe clara e legível, 
    o que a torna uma ótima linguagem para iniciantes. Ela é amplamente utilizada em desenvolvimento web, ciência de dados, 
    inteligência artificial e automação.
    """

    gerar_nuvem_palavras(texto_exemplo)

if __name__ == '__main__':
    main()