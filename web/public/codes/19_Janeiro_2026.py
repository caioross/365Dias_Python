import random

def escolher_cara_ou_coroa():
    """
    Escolhe aleatoriamente entre 'Cara' ou 'Coroa'.

    Returns:
        str: 'Cara' ou 'Coroa'
    """
    return random.choice(['Cara', 'Coroa'])

def main():
    """
    Função principal que executa o simulador de Cara ou Coroa.
    """
    resultado = escolher_cara_ou_coroa()
    print(f"O resultado é: {resultado}")

if __name__ == '__main__':
    main()