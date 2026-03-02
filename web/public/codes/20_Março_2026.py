"""
Calculadora de Horas Trabalhadas

Este script permite que o usuário insira o número de horas e minutos trabalhados
em vários dias do mês e calcula a soma total de horas e minutos trabalhados.
"""

def obter_horas_e_minutos():
    """
    Solicita ao usuário que insira horas e minutos trabalhados.
    
    Returns:
        tuple: Um tuple contendo as horas e minutos inseridos pelo usuário.
    """
    while True:
        try:
            horas = int(input("Digite as horas trabalhadas: "))
            minutos = int(input("Digite os minutos trabalhados: "))
            if 0 <= horas <= 23 and 0 <= minutos <= 59:
                return horas, minutos
            else:
                print("Horas e minutos devem estar no intervalo válido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")

def somar_horas_e_minutos(horas1, minutos1, horas2, minutos2):
    """
    Soma duas combinações de horas e minutos.
    
    Args:
        horas1 (int): Primeiro valor de horas.
        minutos1 (int): Primeiro valor de minutos.
        horas2 (int): Segundo valor de horas.
        minutos2 (int): Segundo valor de minutos.
    
    Returns:
        tuple: Um tuple contendo a soma total de horas e minutos.
    """
    total_minutos = minutos1 + minutos2
    horas_extra = total_minutos // 60
    minutos_restantes = total_minutos % 60
    total_horas = horas1 + horas2 + horas_extra
    return total_horas, minutos_restantes

def main():
    """
    Função principal que executa o script.
    """
    print("Calculadora de Horas Trabalhadas")
    print("Digite as horas e minutos trabalhados para cada dia do mês.")
    
    total_horas = 0
    total_minutos = 0
    
    while True:
        horas, minutos = obter_horas_e_minutos()
        total_horas, total_minutos = somar_horas_e_minutos(total_horas, total_minutos, horas, minutos)
        
        continuar = input("Deseja adicionar mais horas (s/n)? ").strip().lower()
        if continuar != 's':
            break
    
    print(f"\nTotal de horas trabalhadas no mês: {total_horas} horas e {total_minutos} minutos.")

if __name__ == '__main__':
    main()