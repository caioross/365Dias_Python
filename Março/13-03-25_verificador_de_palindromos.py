def remover_acentos_e_especiais(texto):
    """
    Função para remover acentos, caracteres especiais e espaços.
    :param texto: A string que será processada.
    :return: Texto limpo, sem acentos e sem caracteres especiais.
    """
    import unicodedata
    import re

    # Remover acentos e normalizar a string
    texto_normalizado = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    # Remover caracteres não alfanuméricos (como pontuação) e espaços
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto_normalizado)

    return texto_limpo.lower()  # Deixa tudo em minúsculo para garantir comparação correta


def verificar_palindromo(texto):
    """
    Função para verificar se um texto é um palíndromo.
    :param texto: O texto a ser verificado.
    :return: True se o texto for um palíndromo, False caso contrário.
    """
    texto_limpo = remover_acentos_e_especiais(texto)
    
    # Verifica se o texto limpo é igual ao texto limpo invertido
    return texto_limpo == texto_limpo[::-1]


def main():
    """
    Função principal que executa a verificação de palíndromos.
    """
    print("Verificador de Palíndromos")

    while True:
        # Solicita ao usuário que insira um texto
        texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

        # Verifica se o texto é um palíndromo
        if verificar_palindromo(texto):
            print(f'"{texto}" é um palíndromo!')
        else:
            print(f'"{texto}" não é um palíndromo.')

        # Pergunta se o usuário deseja realizar outra verificação
        continuar = input("Deseja verificar outro texto? (s/n): ")
        if continuar.lower() != 's':
            print("Obrigado por usar o verificador de palíndromos! Até logo!")
            break


if __name__ == "__main__":
    main()
