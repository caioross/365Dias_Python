def calcular_juros_compostos(principal, taxa_juros, tempo, num_periodos):
    """
    Função para calcular os juros compostos.
    :param principal: valor inicial (investimento ou empréstimo)
    :param taxa_juros: taxa de juros por período (em decimal, 10% seria 0.10)
    :param tempo: tempo total em anos
    :param num_periodos: número de períodos (ex: 12 para mensal, 4 para trimestral, etc.)
    :return: valor final após os juros compostos
    """
    # Fórmula dos juros compostos: A = P * (1 + r/n)^(n*t)
    montante = principal * (1 + taxa_juros / num_periodos) ** (num_periodos * tempo)
    return montante

def main():
    print("Calculadora de Juros Compostos")
    
    # Solicita os dados do usuário
    try:
        principal = float(input("Digite o valor principal (inicial): R$ "))
        taxa_juros = float(input("Digite a taxa de juros anual (em %): ")) / 100
        tempo = float(input("Digite o tempo total (em anos): "))
        num_periodos = int(input("Digite o número de períodos por ano (ex: 12 para mensal, 4 para trimestral): "))
    except ValueError:
        print("Por favor, insira valores válidos!")
        return

    # Calcula o valor final com juros compostos
    montante_final = calcular_juros_compostos(principal, taxa_juros, tempo, num_periodos)
    
    print(f"\nO valor final após {tempo} anos será: R$ {montante_final:.2f}")

if __name__ == "__main__":
    main()
