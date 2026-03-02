import datetime
import math

def calcular_posicao_planeta(dia, mes, ano, planeta):
    """
    Calcula a posição relativa de um planeta em relação ao sol em uma data específica.
    
    Args:
    dia (int): Dia do mês.
    mes (int): Mês do ano.
    ano (int): Ano.
    planeta (str): Nome do planeta.
    
    Returns:
    tuple: Posição relativa do planeta em coordenadas (x, y).
    """
    # Posições aproximadas dos planetas em relação ao sol (em graus)
    posicoes_iniciais = {
        'mercúrio': 0,
        'vênus': 36,
        'terra': 72,
        'marte': 108,
        'júpiter': 144,
        'saturno': 180,
        'urano': 216,
        'netuno': 252
    }
    
    # Velocidades aproximadas dos planetas (em graus por dia)
    velocidades = {
        'mercúrio': 4.15,
        'vênus': 1.62,
        'terra': 0.99,
        'marte': 0.53,
        'júpiter': 0.08,
        'saturno': 0.03,
        'urano': 0.01,
        'netuno': 0.006
    }
    
    # Data de referência
    data_referencia = datetime.date(2023, 1, 1)
    data_escolhida = datetime.date(ano, mes, dia)
    
    # Cálculo do número de dias entre a data de referência e a data escolhida
    delta_days = (data_escolhida - data_referencia).days
    
    # Cálculo da posição do planeta
    posicao = posicoes_iniciais[planeta] + velocidades[planeta] * delta_days
    
    # Normalização da posição para estar entre 0 e 360 graus
    posicao = posicao % 360
    
    # Conversão da posição polar para cartesiana
    x = math.cos(math.radians(posicao))
    y = math.sin(math.radians(posicao))
    
    return (x, y)

def main():
    """
    Função principal que executa o simulador do sistema solar.
    """
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    planeta = input("Digite o nome do planeta: ").lower()
    
    if planeta not in ['mercúrio', 'vênus', 'terra', 'marte', 'júpiter', 'saturno', 'urano', 'netuno']:
        print("Planeta inválido. Escolha entre mercúrio, vênus, terra, marte, júpiter, saturno, urano ou netuno.")
        return
    
    posicao = calcular_posicao_planeta(dia, mes, ano, planeta)
    print(f"A posição relativa de {planeta} em relação ao sol em {dia}/{mes}/{ano} é: {posicao}")

if __name__ == '__main__':
    main()