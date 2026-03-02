def contar_caracteres_sem_espaco(texto):
    """
    Conta o número total de caracteres em um texto, desconsiderando espaços em branco.

    Args:
        texto (str): O texto a ser analisado.

    Returns:
        int: O número total de caracteres, excluindo espaços.
    """
    return len(texto.replace(" ", ""))

def main():
    """
    Função principal que solicita ao usuário um texto e exibe a contagem de caracteres sem espaços.
    """
    texto = input("Digite o texto: ")
    resultado = contar_caracteres_sem_espaco(texto)
    print(f"O número total de caracteres (sem espaços) é: {resultado}")

if __name__ == '__main__':
    main()