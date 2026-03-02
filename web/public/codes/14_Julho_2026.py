import math

def permutacao(n, k):
    """
    Calcula o número de permutações de n elementos tomados k a k.
    
    Args:
    n (int): O número total de elementos.
    k (int): O número de elementos a serem arranjados.
    
    Returns:
    int: O número de permutações.
    """
    if k > n:
        return 0
    return math.perm(n, k)

def arranjo(n, k):
    """
    Calcula o número de arranjos de n elementos tomados k a k.
    
    Args:
    n (int): O número total de elementos.
    k (int): O número de elementos a serem arranjados.
    
    Returns:
    int: O número de arranjos.
    """
    if k > n:
        return 0
    return math.factorial(n) // math.factorial(n - k)

def combinacao(n, k):
    """
    Calcula o número de combinações de n elementos tomados k a k.
    
    Args:
    n (int): O número total de elementos.
    k (int): O número de elementos a serem combinados.
    
    Returns:
    int: O número de combinações.
    """
    if k > n:
        return 0
    return math.comb(n, k)

def main():
    print("Calculadora Matemática Discreta")
    n = int(input("Digite o número total de elementos (n): "))
    k = int(input("Digite o número de elementos para permutar/arranjar/combinar (k): "))
    
    print(f"Permutações de {n} elementos tomados {k} a {k}: {permutacao(n, k)}")
    print(f"Arranjos de {n} elementos tomados {k} a {k}: {arranjo(n, k)}")
    print(f"Combinações de {n} elementos tomados {k} a {k}: {combinacao(n, k)}")

if __name__ == '__main__':
    main()