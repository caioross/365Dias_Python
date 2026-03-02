import string

def eh_palindromo(frase):
    """
    Verifica se a frase fornecida é um palíndromo, ignorando pontuação e espaços.

    Args:
        frase (str): A frase a ser verificada.

    Returns:
        bool: True se a frase é um palíndromo, False caso contrário.
    """
    # Remove espaços e pontuação, e converte para minúsculas
    cleaned_frase = ''.join(char.lower() for char in frase if char.isalnum())
    
    # Verifica se a frase limpa é igual à sua reversa
    return cleaned_frase == cleaned_frase[::-1]

def main():
    """
    Função principal que solicita ao usuário uma frase e verifica se é um palíndromo.
    """
    frase = input("Digite uma frase: ")
    if eh_palindromo(frase):
        print("A frase é um palíndromo.")
    else:
        print("A frase não é um palíndromo.")

if __name__ == '__main__':
    main()