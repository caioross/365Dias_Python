"""
analisador_sentimento_texto.py

Este script classifica uma frase como positiva, negativa ou neutra
baseada em palavras-chave predefinidas.
"""

def classificar_sentimento(frase):
    """
    Classifica uma frase como positiva, negativa ou neutra.

    Args:
        frase (str): A frase a ser classificada.

    Returns:
        str: A classificação do sentimento ('Positivo', 'Negativo', 'Neutro').
    """
    palavras_positivas = {'ótimo', 'excelente', 'bom', 'ótima', 'maravilhoso'}
    palavras_negativas = {'ruim', 'péssimo', 'triste', 'frustrado', 'insatisfeito'}
    palavras_neutras = {'ok', 'normal', 'mediocre', 'aceitável', 'satisfatório'}

    palavras_frase = set(frase.lower().split())

    if palavras_frase.intersection(palavras_positivas):
        return 'Positivo'
    elif palavras_frase.intersection(palavras_negativas):
        return 'Negativo'
    elif palavras_frase.intersection(palavras_neutras):
        return 'Neutro'
    else:
        return 'Neutro'

def main():
    """
    Função principal que solicita uma frase ao usuário e imprime a classificação
    do sentimento.
    """
    frase = input("Digite uma frase: ")
    sentimento = classificar_sentimento(frase)
    print(f"A frase é: {sentimento}")

if __name__ == '__main__':
    main()