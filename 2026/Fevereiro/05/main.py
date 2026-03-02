import random
import string

def gerar_senha():
    """
    Gera uma senha aleatória de 8 caracteres, alternando entre letras e números.

    Returns:
        str: Senha gerada
    """
    if random.choice([True, False]):
        # Começa com letra
        senha = [random.choice(string.ascii_letters)]
    else:
        # Começa com número
        senha = [random.choice(string.digits)]

    for _ in range(1, 8):
        if senha[-1] in string.ascii_letters:
            senha.append(random.choice(string.digits))
        else:
            senha.append(random.choice(string.ascii_letters))

    return ''.join(senha)

def main():
    """
    Função principal que gera e imprime uma senha aleatória.
    """
    senha = gerar_senha()
    print(f"Senha gerada: {senha}")

if __name__ == '__main__':
    main()