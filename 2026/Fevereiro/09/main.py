import re
from collections import Counter

def contar_palavras(texto):
    """
    Conta a frequência de cada palavra em um texto.

    Args:
        texto (str): O texto a ser analisado.

    Returns:
        Counter: Um objeto Counter com as palavras como chaves e suas frequências como valores.
    """
    # Usar expressões regulares para encontrar palavras, ignorando pontuação e maiúsculas/minúsculas
    palavras = re.findall(r'\b\w+\b', texto.lower())
    return Counter(palavras)

def exibir_ranking_palavras(frequencia, top_n=10):
    """
    Exibe o ranking das palavras mais comuns.

    Args:
        frequencia (Counter): Um objeto Counter com as frequências das palavras.
        top_n (int): O número de palavras mais comuns a serem exibidas.
    """
    print(f"Top {top_n} palavras mais comuns:")
    for palavra, freq in frequencia.most_common(top_n):
        print(f"{palavra}: {freq}")

def main():
    """
    Função principal que executa o script.
    """
    texto = input("Digite o texto para analisar: ")
    frequencia_palavras = contar_palavras(texto)
    exibir_ranking_palavras(frequencia_palavras)

if __name__ == '__main__':
    main()