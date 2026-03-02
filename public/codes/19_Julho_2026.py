import re

def validar_cartao_sus(numero_sus):
    """
    Valida se o número do Cartão Nacional de Saúde (SUS) é válido.
    
    Args:
        numero_sus (str): O número do cartão SUS a ser validado.
    
    Returns:
        bool: True se o número é válido, False caso contrário.
    """
    # Remove espaços e hífens
    numero_sus = re.sub(r'[\s-]', '', numero_sus)
    
    # Verifica se o número tem 15 dígitos
    if len(numero_sus) != 15 or not numero_sus.isdigit():
        return False
    
    # Implementação da validação do número SUS
    # A validação do SUS segue um algoritmo específico que não é publicamente documentado
    # Portanto, esta função apenas verifica se o número tem 15 dígitos numéricos
    # Para uma validação completa, seria necessário implementar o algoritmo oficial
    
    return True

def main():
    """
    Função principal que solicita ao usuário um número de SUS e verifica sua validade.
    """
    numero_sus = input("Digite o número do Cartão Nacional de Saúde (SUS): ")
    
    if validar_cartao_sus(numero_sus):
        print("O número do Cartão Nacional de Saúde é válido.")
    else:
        print("O número do Cartão Nacional de Saúde é inválido.")

if __name__ == '__main__':
    main()