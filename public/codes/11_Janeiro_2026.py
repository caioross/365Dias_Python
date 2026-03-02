def reverso_de_string(texto):
    """
    Recebe uma palavra ou frase e retorna a versão reversa, ignorando espaços extras.

    :param texto: str - A palavra ou frase a ser revertida.
    :return: str - A versão reversa da palavra ou frase.
    """
    # Remove espaços extras e inverte a string
    return ' '.join(texto.split()[::-1])

def main():
    """
    Função principal que solicita ao usuário uma palavra ou frase e exibe a versão reversa.
    """
    entrada = input("Digite uma palavra ou frase: ")
    resultado = reverso_de_string(entrada)
    print(f"Reverso: {resultado}")

if __name__ == '__main__':
    main()