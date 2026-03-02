def calcular_regra_de_tres(a, b, c):
    """
    Calcula o quarto termo da regra de três simples.

    Parâmetros:
    a (float): O primeiro termo da proporção.
    b (float): O segundo termo da proporção.
    c (float): O terceiro termo da proporção.

    Retorna:
    float: O quarto termo da proporção.
    """
    if b == 0:
        raise ValueError("O segundo termo (b) não pode ser zero.")
    
    return (c * a) / b

def main():
    """
    Função principal que solicita os valores ao usuário e exibe o resultado da regra de três.
    """
    print("Resolvendo problemas de regra de três simples.")
    
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        
        resultado = calcular_regra_de_tres(a, b, c)
        print(f"O valor de d é: {resultado}")
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()