def ordenar_lista(numeros):
    """
    Ordena uma lista de números em ordem crescente e decrescente.

    Args:
        numeros (list): Uma lista de números desordenados.

    Returns:
        tuple: Uma tupla contendo duas listas - a primeira em ordem crescente e a segunda em ordem decrescente.
    """
    if not isinstance(numeros, list):
        raise ValueError("O argumento deve ser uma lista de números.")
    
    numeros_crescente = sorted(numeros)
    numeros_decrescente = sorted(numeros, reverse=True)
    
    return numeros_crescente, numeros_decrescente

def main():
    """
    Função principal que recebe uma série de números desordenados, os ordena e imprime os resultados.
    """
    try:
        # Exemplo de lista de números desordenados
        numeros = [5, 2, 9, 1, 5, 6]
        
        # Obtendo as listas ordenadas
        crescente, decrescente = ordenar_lista(numeros)
        
        # Imprimindo os resultados
        print("Ordem Crescente:", crescente)
        print("Ordem Decrescente:", decrescente)
    
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == '__main__':
    main()