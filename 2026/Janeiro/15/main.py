import random

def embaralhar_itens(itens):
    """
    Embaralha aleatoriamente a lista de itens fornecida.

    Args:
    itens (list): A lista de itens a serem embaralhados.

    Returns:
    list: A lista de itens embaralhada.
    """
    random.shuffle(itens)
    return itens

def main():
    """
    Função principal que solicita uma lista de itens ao usuário, embaralha-os e exibe a lista embaralhada.
    """
    itens = input("Digite os itens separados por vírgula: ").split(',')
    itens = [item.strip() for item in itens]  # Remove espaços em branco
    itens_embaralhados = embaralhar_itens(itens)
    print("Itens embaralhados:", itens_embaralhados)

if __name__ == '__main__':
    main()