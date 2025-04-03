import random
import string

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_caracteres_especiais=True):
    """
    Função para gerar uma senha segura com base nas opções personalizadas fornecidas.
    
    :param comprimento: Comprimento da senha (padrão é 12).
    :param incluir_maiusculas: Se True, inclui letras maiúsculas na senha (padrão é True).
    :param incluir_minusculas: Se True, inclui letras minúsculas na senha (padrão é True).
    :param incluir_numeros: Se True, inclui números na senha (padrão é True).
    :param incluir_caracteres_especiais: Se True, inclui caracteres especiais na senha (padrão é True).
    :return: Senha gerada de acordo com os parâmetros fornecidos.
    """
    # Definindo os conjuntos de caracteres possíveis
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiais:
        caracteres += string.punctuation
    
    # Garantir que a senha tenha pelo menos um caractere de cada tipo, caso desejado
    senha = []
    if incluir_maiusculas:
        senha.append(random.choice(string.ascii_uppercase))
    if incluir_minusculas:
        senha.append(random.choice(string.ascii_lowercase))
    if incluir_numeros:
        senha.append(random.choice(string.digits))
    if incluir_caracteres_especiais:
        senha.append(random.choice(string.punctuation))
    
    # Preencher o restante da senha com caracteres aleatórios
    senha += random.choices(caracteres, k=comprimento - len(senha))
    
    # Embaralhar a senha gerada para maior segurança
    random.shuffle(senha)
    
    # Retornar a senha como uma string
    return ''.join(senha)

def main():
    """
    Função principal que solicita os parâmetros e gera a senha.
    """
    print("Gerador de Senhas Seguras")
    
    comprimento = int(input("Digite o comprimento da senha (padrão é 12): ") or 12)
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_caracteres_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'
    
    # Gerar a senha com base nas opções fornecidas
    senha_gerada = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_caracteres_especiais)
    
    print("\nSenha Gerada:", senha_gerada)

if __name__ == "__main__":
    main()
