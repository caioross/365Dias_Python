def validar_titulo_abnt(titulo: str) -> bool:
    """
    Valida se um título de artigo segue as normas ABNT:
    1. A primeira letra de cada palavra é capitalizada.
    2. O título tem pelo menos 10 caracteres.
    3. O título não termina com um ponto final.

    :param titulo: O título do artigo a ser validado.
    :return: True se o título está correto, False caso contrário.
    """
    # Verifica se o título tem pelo menos 10 caracteres
    if len(titulo) < 10:
        return False

    # Verifica se a primeira letra de cada palavra é capitalizada
    if titulo != titulo.title():
        return False

    # Verifica se o título não termina com um ponto final
    if titulo.endswith('.'):
        return False

    return True

def main():
    """
    Função principal que solicita ao usuário um título de artigo e verifica
    se ele está de acordo com as normas ABNT.
    """
    titulo = input("Digite o título do artigo: ")
    if validar_titulo_abnt(titulo):
        print("O título está correto de acordo com as normas ABNT.")
    else:
        print("O título não está correto de acordo com as normas ABNT.")

if __name__ == '__main__':
    main()