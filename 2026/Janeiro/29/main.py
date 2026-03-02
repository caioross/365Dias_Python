import re

def is_valid_email(email):
    """
    Verifica se o email fornecido possui um formato válido.
    
    Um email válido deve conter um "@" seguido de pelo menos um caractere e um ponto,
    seguido de pelo menos duas letras para representar o domínio.
    
    Args:
    email (str): O email a ser validado.
    
    Returns:
    bool: True se o email for válido, False caso contrário.
    """
    # Expressão regular para validar o email
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(email_regex, email) is not None

def main():
    """
    Função principal que solicita ao usuário um email e verifica sua validade.
    """
    email = input("Digite o email para validação: ")
    if is_valid_email(email):
        print("O email é válido.")
    else:
        print("O email é inválido.")

if __name__ == '__main__':
    main()