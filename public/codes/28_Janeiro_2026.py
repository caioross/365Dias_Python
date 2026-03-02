"""
Script para verificar se uma frase contém palavras censuradas de uma lista pré-definida.
"""

def contem_palavras_proibidas(frase, palavras_proibidas):
    """
    Verifica se a frase contém alguma palavra da lista de palavras proibidas.

    Args:
        frase (str): A frase a ser verificada.
        palavras_proibidas (list): A lista de palavras proibidas.

    Returns:
        bool: True se a frase contém palavras proibidas, False caso contrário.
    """
    palavras_frase = frase.lower().split()
    for palavra in palavras_frase:
        if palavra in palavras_proibidas:
            return True
    return False

def main():
    """
    Função principal do script.
    """
    frase = input("Digite uma frase: ")
    palavras_proibidas = ['censura', 'proibido', 'fora', 'leis', 'regulamento']
    
    if contem_palavras_proibidas(frase, palavras_proibidas):
        print("A frase contém palavras proibidas.")
    else:
        print("A frase não contém palavras proibidas.")

if __name__ == '__main__':
    main()