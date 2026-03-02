"""
Script para validar a chave de acesso de uma Nota Fiscal Eletrônica (NF-e).

Este script verifica se a chave de acesso da NF-e possui 44 dígitos e se está no formato correto.
"""

def is_valid_nfe_key(key: str) -> bool:
    """
    Verifica se a chave de acesso da NF-e é válida.

    Args:
        key (str): A chave de acesso da NF-e.

    Returns:
        bool: True se a chave é válida, False caso contrário.
    """
    # Verifica se a chave tem exatamente 44 caracteres
    if len(key) != 44:
        return False
    
    # Verifica se todos os caracteres são dígitos
    if not key.isdigit():
        return False
    
    return True

def main():
    """
    Função principal do script.
    Solicita ao usuário uma chave de acesso e verifica sua validade.
    """
    key = input("Digite a chave de acesso da NF-e: ")
    if is_valid_nfe_key(key):
        print("A chave de acesso é válida.")
    else:
        print("A chave de acesso é inválida.")

if __name__ == '__main__':
    main()