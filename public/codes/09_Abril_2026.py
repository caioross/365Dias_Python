import re

def validar_titulo_eleitor(titulo: str) -> bool:
    """
    Valida se o formato numérico do Título de Eleitor brasileiro é válido.
    
    O Título de Eleitor brasileiro deve ter 12 dígitos, onde os 8 primeiros são 
    números sequenciais e os 4 últimos são um dígito verificador.
    
    Args:
        titulo (str): O número do Título de Eleitor a ser validado.
    
    Returns:
        bool: True se o formato é válido, False caso contrário.
    """
    # Remove espaços e verifica se o título tem 12 dígitos
    titulo = titulo.replace(" ", "")
    if not re.match(r'^\d{12}$', titulo):
        return False
    
    # Verifica se os 8 primeiros dígitos são sequenciais
    primeiro_parte = titulo[:8]
    if primeiro_parte in ('00000000', '11111111', '22222222', '33333333', '44444444',
                          '55555555', '66666666', '77777777', '88888888', '99999999'):
        return False
    
    return True

def main():
    """
    Função principal que solicita ao usuário um título de eleitor e verifica sua validade.
    """
    titulo = input("Digite o número do Título de Eleitor: ")
    if validar_titulo_eleitor(titulo):
        print("O Título de Eleitor é válido.")
    else:
        print("O Título de Eleitor é inválido.")

if __name__ == '__main__':
    main()