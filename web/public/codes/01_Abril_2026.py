import random

def lançar_moeda(probabilidade_cara):
    """
    Simula o lançamento de uma moeda viciada.

    Args:
        probabilidade_cara (float): A probabilidade de obter 'cara', deve estar entre 0 e 1.

    Returns:
        str: 'cara' se a moeda cair em 'cara', 'coroa' caso contrário.
    """
    if not (0 <= probabilidade_cara <= 1):
        raise ValueError("A probabilidade deve estar entre 0 e 1")

    return 'cara' if random.random() < probabilidade_cara else 'coroa'

def main():
    """
    Função principal que executa o simulador de lançamento de moeda viciada.
    Solicita ao usuário a probabilidade de obter 'cara' e simula o lançamento.
    """
    try:
        probabilidade_cara = float(input("Digite a probabilidade de obter 'cara' (entre 0 e 1): "))
        resultado = lançar_moeda(probabilidade_cara)
        print(f"O resultado do lançamento foi: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()