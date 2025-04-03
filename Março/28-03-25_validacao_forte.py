import re

def validar_senha(senha):
    """
    Função para validar se a senha é forte.
    A senha será considerada forte se:
    - Contiver pelo menos 8 caracteres.
    - Contiver pelo menos uma letra maiúscula.
    - Contiver pelo menos uma letra minúscula.
    - Contiver pelo menos um número.
    - Contiver pelo menos um caractere especial.
    
    :param senha: A senha a ser validada.
    :return: True se a senha for forte, False caso contrário.
    """
    # Verificar comprimento mínimo de 8 caracteres
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return False
    
    # Verificar se contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        print("A senha deve conter pelo menos uma letra maiúscula.")
        return False
    
    # Verificar se contém pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        print("A senha deve conter pelo menos uma letra minúscula.")
        return False
    
    # Verificar se contém pelo menos um número
    if not re.search(r'[0-9]', senha):
        print("A senha deve conter pelo menos um número.")
        return False
    
    # Verificar se contém pelo menos um caractere especial
    if not re.search(r'[@$!%*?&]', senha):
        print("A senha deve conter pelo menos um caractere especial (@, $, !, %, *, ?, &).")
        return False
    
    # Se passar por todas as verificações, a senha é forte
    return True

def main():
    """
    Função principal que solicita a senha e valida a segurança.
    """
    senha = input("Digite a senha: ")

    if validar_senha(senha):
        print("A senha é forte!")
    else:
        print("A senha não é forte. Tente novamente.")

if __name__ == "__main__":
    main()
