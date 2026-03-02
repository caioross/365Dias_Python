import random

def gerar_paragrafo_lorem_ipsum(num_palavras):
    """
    Gera um parágrafo de texto "Lorem Ipsum" com uma quantidade específica de palavras.

    Args:
        num_palavras (int): O número de palavras que o parágrafo deve conter.

    Returns:
        str: Um parágrafo de texto "Lorem Ipsum".
    """
    # Lista de palavras Lorem Ipsum
    lorem_ipsum_words = [
        'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit',
        'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore',
        'magna', 'aliqua', 'ut', 'enim', 'ad', 'minim', 'veniam', 'quis', 'nostrud',
        'exercitation', 'ullamco', 'laboris', 'nisi', 'ut', 'aliquip', 'ex', 'ea',
        'commodo', 'consequat', 'duis', 'aute', 'irure', 'dolor', 'in', 'reprehenderit',
        'in', 'voluptate', 'velit', 'esse', 'cillum', 'dolore', 'eu', 'fugiat', 'nulla',
        'pariatur', 'excepteur', 'sint', 'occaecat', 'cupidatat', 'non', 'proident',
        'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt', 'mollit', 'anim', 'id',
        'est', 'laborum'
    ]

    # Seleciona aleatoriamente as palavras para formar o parágrafo
    paragrafo = ' '.join(random.sample(lorem_ipsum_words, num_palavras))
    return paragrafo

def main():
    """
    Função principal que solicita ao usuário a quantidade de palavras e gera o parágrafo.
    """
    try:
        num_palavras = int(input("Digite o número de palavras para o parágrafo: "))
        if num_palavras <= 0:
            raise ValueError("O número de palavras deve ser maior que zero.")
        
        paragrafo = gerar_paragrafo_lorem_ipsum(num_palavras)
        print("\nParágrafo gerado:")
        print(paragrafo)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()