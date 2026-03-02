"""
gerador_palavras_cruzadas_base.py

Este script organiza uma lista de palavras em uma grade simples para jogos de passatempo.
"""

def criar_grade(palavras):
    """
    Cria uma grade simples com as palavras fornecidas.

    Args:
        palavras (list): Uma lista de palavras a serem organizadas na grade.

    Returns:
        list: Uma lista de listas representando a grade.
    """
    if not palavras:
        return []

    # Determina o tamanho da grade como o maior comprimento de palavra
    tamanho_grade = max(len(palavra) for palavra in palavras)
    grade = [[' ' for _ in range(tamanho_grade)] for _ in range(tamanho_grade)]

    # Coloca cada palavra na grade
    for i, palavra in enumerate(palavras):
        for j, letra in enumerate(palavra):
            grade[i][j] = letra

    return grade

def imprimir_grade(grade):
    """
    Imprime a grade de palavras de forma formatada.

    Args:
        grade (list): A grade de palavras a ser impressa.
    """
    for linha in grade:
        print(' '.join(linha))

def main():
    """
    Função principal que gera e imprime uma grade de palavras cruzadas.
    """
    palavras = ["python", "cruzado", "script", "grade", "organiza"]
    grade = criar_grade(palavras)
    imprimir_grade(grade)

if __name__ == '__main__':
    main()