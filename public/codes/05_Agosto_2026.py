import re

def is_valid_e164(phone_number: str) -> bool:
    """
    Verifica se o número de telefone fornecido está no formato E.164.
    
    Args:
        phone_number (str): O número de telefone a ser validado.
        
    Returns:
        bool: True se o número está no formato E.164, False caso contrário.
    """
    # Expressão regular para o formato E.164: +[1-9][0-9]{1,14}
    e164_pattern = re.compile(r'^\+[1-9][0-9]{1,14}$')
    return bool(e164_pattern.match(phone_number))

def main():
    """
    Função principal que solicita ao usuário um número de telefone e verifica
    se ele está no formato E.164.
    """
    phone_number = input("Digite o número de telefone para validação: ")
    if is_valid_e164(phone_number):
        print("O número de telefone está no formato E.164.")
    else:
        print("O número de telefone NÃO está no formato E.164.")

if __name__ == '__main__':
    main()