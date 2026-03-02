import re

def extrair_numeros_telefone(texto):
    """
    Extrai números de telefone de um texto usando expressões regulares.

    Args:
        texto (str): O texto do qual os números de telefone devem ser extraídos.

    Returns:
        list: Uma lista de números de telefone encontrados no texto.
    """
    # Padrão para encontrar números de telefone no formato (XX) XXXX-XXXX
    padrao = r'\(\d{2}\) \d{4}-\d{4}'
    # Encontrar todos os números de telefone que correspondem ao padrão
    numeros_encontrados = re.findall(padrao, texto)
    return numeros_encontrados

def main():
    """
    Função principal do script.
    """
    texto = """
    Entre em contato conosco:
    (11) 1234-5678
    (22) 9876-5432
    (33) 1111-2222
    """
    numeros_telefone = extrair_numeros_telefone(texto)
    print("Números de telefone encontrados:")
    for numero in numeros_telefone:
        print(numero)

if __name__ == '__main__':
    main()