"""
simulador_logica_portas_and_or.py

Interface que permite montar circuitos lógicos simples usando portas AND e OR,
e ver o resultado booleano.
"""

def porta_and(a, b):
    """
    Realiza a operação lógica AND entre dois valores booleanos.

    Args:
        a (bool): Primeiro valor booleano.
        b (bool): Segundo valor booleano.

    Returns:
        bool: Resultado da operação AND.
    """
    return a and b

def porta_or(a, b):
    """
    Realiza a operação lógica OR entre dois valores booleanos.

    Args:
        a (bool): Primeiro valor booleano.
        b (bool): Segundo valor booleano.

    Returns:
        bool: Resultado da operação OR.
    """
    return a or b

def montar_circuito_and_or(a, b, c):
    """
    Monta um circuito lógico simples que primeiro aplica a porta AND entre
    os dois primeiros valores e depois aplica a porta OR com o terceiro valor.

    Args:
        a (bool): Primeiro valor booleano.
        b (bool): Segundo valor booleano.
        c (bool): Terceiro valor booleano.

    Returns:
        bool: Resultado do circuito lógico.
    """
    resultado_and = porta_and(a, b)
    resultado_final = porta_or(resultado_and, c)
    return resultado_final

def main():
    """
    Função principal que demonstra o uso do simulador de circuitos lógicos.
    """
    print("Simulador de Circuitos Lógicos (AND/OR)")
    a = bool(input("Digite o valor booleano para A (True/False): "))
    b = bool(input("Digite o valor booleano para B (True/False): "))
    c = bool(input("Digite o valor booleano para C (True/False): "))

    resultado = montar_circuito_and_or(a, b, c)
    print(f"Resultado do circuito: {resultado}")

if __name__ == '__main__':
    main()