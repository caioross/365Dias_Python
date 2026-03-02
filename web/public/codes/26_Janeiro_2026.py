def extrair_iniciais(nome_completo):
    """
    Extrai as letras iniciais de cada palavra em um nome completo.

    Args:
        nome_completo (str): O nome completo do usuário.

    Returns:
        str: Uma string contendo as iniciais de cada palavra no nome completo.
    """
    # Dividir o nome completo em palavras
    palavras = nome_completo.split()
    # Extrair a primeira letra de cada palavra e juntá-las
    iniciais = ''.join(palavra[0].upper() for palavra in palavras)
    return iniciais

def main():
    """
    Função principal que solicita ao usuário um nome completo,
    extrai as iniciais e exibe o resultado.
    """
    nome_completo = input("Digite o nome completo: ")
    iniciais = extrair_iniciais(nome_completo)
    print(f"Iniciais: {iniciais}")

if __name__ == '__main__':
    main()