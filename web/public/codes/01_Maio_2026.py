import random

def gerar_cartela_bingo():
    """
    Gera uma cartela de bingo aleatória de 5x5 seguindo as regras tradicionais.
    
    Retorna:
        list: Uma lista de listas representando a cartela de bingo.
    """
    cartela = []
    intervalos = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]
    letras = ['B', 'I', 'N', 'G', 'O']
    
    for intervalo, letra in zip(intervalos, letras):
        numeros = random.sample(range(intervalo[0], intervalo[1] + 1), 5)
        cartela.append([letra + str(numero).zfill(2) for numero in numeros])
    
    return cartela

def imprimir_cartela(cartela):
    """
    Imprime a cartela de bingo de forma formatada.
    
    Args:
        cartela (list): A cartela de bingo a ser impressa.
    """
    for linha in cartela:
        print(" | ".join(linha))
        print("-" * (len(linha) * 5))

def main():
    """
    Função principal que gera e imprime uma cartela de bingo.
    """
    cartela = gerar_cartela_bingo()
    imprimir_cartela(cartela)

if __name__ == '__main__':
    main()