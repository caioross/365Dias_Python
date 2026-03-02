import re

def validar_rg(rg):
    """
    Valida o formato do RG (Registro Geral) brasileiro.
    
    O formato padrão do RG é 99.999.999-X, onde X pode ser um dígito ou uma letra.
    
    Args:
        rg (str): O número do RG a ser validado.
    
    Returns:
        bool: True se o RG for válido, False caso contrário.
    """
    padrao_rg = re.compile(r'^\d{2}\.\d{3}\.\d{3}-[A-Za-z0-9]$')
    return bool(padrao_rg.match(rg))

def validar_reservista(reservista):
    """
    Valida o formato do número do Reservista brasileiro.
    
    O formato padrão do Reservista é 99.999.999-X, onde X pode ser um dígito ou uma letra.
    
    Args:
        reservista (str): O número do Reservista a ser validado.
    
    Returns:
        bool: True se o número do Reservista for válido, False caso contrário.
    """
    padrao_reservista = re.compile(r'^\d{2}\.\d{3}\.\d{3}-[A-Za-z0-9]$')
    return bool(padrao_reservista.match(reservista))

def main():
    """
    Função principal que solicita ao usuário um documento para validar e exibe o resultado.
    """
    documento = input("Digite o documento (RG ou Reservista) para validar: ")
    
    if validar_rg(documento):
        print("O documento é um RG válido.")
    elif validar_reservista(documento):
        print("O documento é um número de Reservista válido.")
    else:
        print("O documento não é válido.")

if __name__ == '__main__':
    main()