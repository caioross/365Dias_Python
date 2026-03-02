import math

def is_golden_ratio(dim1, dim2, tolerance=0.01):
    """
    Verifica se a proporção entre duas dimensões está próxima da proporção áurea (phi).
    
    Args:
    dim1 (float): A primeira dimensão.
    dim2 (float): A segunda dimensão.
    tolerance (float): A tolerância aceitável para a comparação com a proporção áurea.
    
    Returns:
    bool: True se a proporção está próxima da proporção áurea, False caso contrário.
    """
    if dim1 <= 0 or dim2 <= 0:
        raise ValueError("As dimensões devem ser maiores que zero.")
    
    phi = (1 + math.sqrt(5)) / 2
    ratio = max(dim1, dim2) / min(dim1, dim2)
    
    return abs(ratio - phi) <= tolerance

def main():
    """
    Função principal que solicita ao usuário as dimensões e verifica se elas seguem a proporção áurea.
    """
    try:
        dim1 = float(input("Digite a primeira dimensão: "))
        dim2 = float(input("Digite a segunda dimensão: "))
        
        if is_golden_ratio(dim1, dim2):
            print("As dimensões seguem a proporção áurea.")
        else:
            print("As dimensões não seguem a proporção áurea.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()