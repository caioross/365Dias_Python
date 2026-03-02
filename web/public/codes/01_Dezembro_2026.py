"""
calendario_advento_python.py

Este script implementa um calendário de advento onde cada dia revela um desafio de código ou curiosidade sobre Python.
"""

import datetime

def get_daily_challenge(day):
    """
    Retorna o desafio ou curiosidade para o dia especificado.

    Args:
        day (int): O dia do calendário de advento.

    Returns:
        str: A descrição do desafio ou curiosidade.
    """
    challenges = {
        1: "Escreva uma função que inverte uma string.",
        2: "Crie uma função que verifica se um número é primo.",
        3: "Implemente um algoritmo de ordenação (ex: Bubble Sort).",
        4: "Explique o que é um decorador em Python e forneça um exemplo.",
        5: "Escreva um script que leia um arquivo e conte o número de palavras.",
        6: "Crie uma função que gera números aleatórios dentro de um intervalo especificado.",
        7: "Explique o que é um generator em Python e forneça um exemplo.",
        8: "Escreva uma função que calcula o fatorial de um número.",
        9: "Implemente uma classe que represente um ponto 2D e forneça métodos para calcular a distância entre dois pontos.",
        10: "Explique o que é o GIL (Global Interpreter Lock) em Python.",
        11: "Crie uma função que verifica se duas strings são anagramas.",
        12: "Explique o que é um módulo em Python e forneça um exemplo de como importá-lo.",
        13: "Escreva um script que leia um arquivo CSV e converta-o em um dicionário.",
        14: "Crie uma função que encontra o maior número em uma lista.",
        15: "Explique o que é o Duck Typing em Python.",
        16: "Escreva uma função que calcula a média de uma lista de números.",
        17: "Implemente uma função que verifica se uma string é um palíndromo.",
        18: "Explique o que é um context manager em Python e forneça um exemplo.",
        19: "Crie uma função que gera números Fibonacci até um limite especificado.",
        20: "Explique o que é o Monkey Patching em Python.",
        21: "Escreva um script que leia um arquivo JSON e imprima os dados.",
        22: "Crie uma função que encontra o menor número em uma lista.",
        23: "Explique o que é um namespace em Python.",
        24: "Escreva uma função que calcula a mediana de uma lista de números.",
        25: "Implemente uma função que verifica se um número é um quadrado perfeito.",
        26: "Explique o que é o Monkey Patching em Python.",
        27: "Escreva um script que leia um arquivo XML e imprima os dados.",
        28: "Crie uma função que encontra o segundo maior número em uma lista.",
        29: "Explique o que é um closure em Python.",
        30: "Escreva uma função que calcula a moda de uma lista de números."
    }
    return challenges.get(day, "Desafio ainda não disponível.")

def main():
    """
    Função principal que executa o calendário de advento.
    """
    today = datetime.date.today()
    day_of_advent = today.day

    if 1 <= day_of_advent <= 30:
        challenge = get_daily_challenge(day_of_advent)
        print(f"Desafio do Dia {day_of_advent}:\n{challenge}")
    else:
        print("Ainda não é tempo do calendário de advento ou o dia está fora do intervalo.")

if __name__ == '__main__':
    main()