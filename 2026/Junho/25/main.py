import itertools

def calcular_probabilidade(soma_desejada, numero_de_dados, faces_do_dado=6):
    """
    Calcula a probabilidade de obter uma soma específica ao lançar múltiplos dados.

    Args:
        soma_desejada (int): A soma que se deseja obter.
        numero_de_dados (int): O número de dados a serem lançados.
        faces_do_dado (int, optional): O número de faces em cada dado. Padrão é 6.

    Returns:
        float: A probabilidade de obter a soma desejada.
    """
    # Gera todas as possíveis combinações de lançamentos dos dados
    combinacoes = list(itertools.product(range(1, faces_do_dado + 1), repeat=numero_de_dados))
    
    # Conta quantas combinações resultam na soma desejada
    sucesso = sum(1 for combinacao in combinacoes if sum(combinacao) == soma_desejada)
    
    # Calcula a probabilidade
    probabilidade = sucesso / len(combinacoes)
    
    return probabilidade

def main():
    """
    Função principal que solicita ao usuário a soma desejada, o número de dados e calcula a probabilidade.
    """
    try:
        soma_desejada = int(input("Digite a soma desejada: "))
        numero_de_dados = int(input("Digite o número de dados: "))
        faces_do_dado = int(input("Digite o número de faces em cada dado (padrão é 6): ") or 6)
        
        probabilidade = calcular_probabilidade(soma_desejada, numero_de_dados, faces_do_dado)
        print(f"A probabilidade de obter a soma {soma_desejada} com {numero_de_dados} dados é {probabilidade:.2%}")
    
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira valores numéricos válidos.")

if __name__ == '__main__':
    main()