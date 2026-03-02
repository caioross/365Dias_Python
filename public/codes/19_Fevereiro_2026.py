import re

def calcular_fortaleza_senha(senha):
    """
    Calcula a fortaleza de uma senha com base em seu tamanho e variedade de caracteres.

    Args:
        senha (str): A senha a ser avaliada.

    Returns:
        int: Uma nota de segurança entre 0 e 100, onde 0 é muito fraca e 100 é muito forte.
    """
    tamanho = len(senha)
    tem_letras_minusculas = re.search(r'[a-z]', senha) is not None
    tem_letras_maiusculas = re.search(r'[A-Z]', senha) is not None
    tem_digitos = re.search(r'\d', senha) is not None
    tem_caracteres_especiais = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha) is not None

    nota = 0

    # Avalia o tamanho da senha
    if tamanho >= 8:
        nota += 20
    elif tamanho >= 6:
        nota += 10

    # Avalia a presença de diferentes tipos de caracteres
    if tem_letras_minusculas:
        nota += 20
    if tem_letras_maiusculas:
        nota += 20
    if tem_digitos:
        nota += 20
    if tem_caracteres_especiais:
        nota += 20

    return min(nota, 100)

def main():
    """
    Função principal que solicita uma senha ao usuário e exibe sua nota de segurança.
    """
    senha = input("Digite a senha para avaliar a fortaleza: ")
    nota = calcular_fortaleza_senha(senha)
    print(f"A senha '{senha}' tem uma nota de segurança de {nota}.")

if __name__ == '__main__':
    main()