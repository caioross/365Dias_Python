import random

def gerar_numeros_loteria():
    """
    Gera uma lista contendo 6 números aleatórios únicos entre 1 e 60.
    
    Returns:
        list: Uma lista de 6 números inteiros.
    """
    return random.sample(range(1, 61), 6)

def main():
    """
    Função principal que gera e exibe os números da loteria.
    """
    numeros_loteria = gerar_numeros_loteria()
    print("Números da loteria gerados:", sorted(numeros_loteria))

if __name__ == '__main__':
    main()