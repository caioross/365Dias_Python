def calcular_idade_equivalente(porte, idade_cachorro):
    """
    Calcula a idade equivalente em anos humanos de um cachorro com base em seu porte.

    Args:
        porte (str): O porte do cachorro. Pode ser 'pequeno', 'médio' ou 'grande'.
        idade_cachorro (int): A idade do cachorro em anos.

    Returns:
        float: A idade equivalente em anos humanos.
    """
    if porte == 'pequeno':
        return idade_cachorro * 4
    elif porte == 'médio':
        return idade_cachorro * 5
    elif porte == 'grande':
        return idade_cachorro * 6
    else:
        raise ValueError("Porte inválido. Escolha entre 'pequeno', 'médio' ou 'grande'.")

def main():
    """
    Função principal que solicita ao usuário o porte e a idade do cachorro,
    calcula a idade equivalente em anos humanos e exibe o resultado.
    """
    porte = input("Digite o porte do cachorro (pequeno, médio, grande): ")
    try:
        idade_cachorro = int(input("Digite a idade do cachorro em anos: "))
        idade_equivalente = calcular_idade_equivalente(porte, idade_cachorro)
        print(f"A idade equivalente em anos humanos é: {idade_equivalente}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()