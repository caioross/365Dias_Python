import re

def validar_expressao_regular(padrao, texto):
    """
    Valida a expressão regular fornecida contra o texto e retorna os grupos capturados.

    Args:
        padrao (str): A expressão regular a ser testada.
        texto (str): O texto a ser validado contra a expressão regular.

    Returns:
        list: Uma lista de grupos capturados se a expressão regular corresponder ao texto, caso contrário, None.
    """
    try:
        match = re.match(padrao, texto)
        if match:
            return match.groups()
        return None
    except re.error as e:
        print(f"Erro na expressão regular: {e}")
        return None

def main():
    """
    Função principal que solicita ao usuário uma expressão regular e um texto para validação.
    """
    padrao = input("Digite a expressão regular: ")
    texto = input("Digite o texto para validação: ")

    grupos = validar_expressao_regular(padrao, texto)
    if grupos:
        print("Grupos capturados:", grupos)
    else:
        print("Nenhum grupo capturado ou expressão regular inválida.")

if __name__ == '__main__':
    main()