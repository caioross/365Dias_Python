"""
calculo_consumo_energia.py

Este script estima o custo mensal de um eletrodoméstico com base em sua potência (em Watts)
e horas de uso. O usuário deve fornecer a potência do eletrodoméstico, as horas de uso por dia,
e o custo do kWh (quilowatt-hora) na sua região.
"""

def calcular_consumo_mensal(potencia_watts, horas_por_dia, dias_no_mes=30):
    """
    Calcula o consumo mensal de energia de um eletrodoméstico.

    :param potencia_watts: Potência do eletrodoméstico em Watts.
    :param horas_por_dia: Horas de uso do eletrodoméstico por dia.
    :param dias_no_mes: Número de dias no mês (padrão é 30).
    :return: Consumo mensal em kWh.
    """
    potencia_kwh = potencia_watts / 1000  # Convertendo Watts para kWh
    consumo_mensal = potencia_kwh * horas_por_dia * dias_no_mes
    return consumo_mensal

def calcular_custo_mensal(consumo_mensal, custo_kwh):
    """
    Calcula o custo mensal de energia de um eletrodoméstico.

    :param consumo_mensal: Consumo mensal em kWh.
    :param custo_kwh: Custo do kWh na região.
    :return: Custo mensal em reais.
    """
    custo_mensal = consumo_mensal * custo_kwh
    return custo_mensal

def main():
    """
    Função principal que executa o script.
    Solicita ao usuário as informações necessárias e exibe o custo mensal do eletrodoméstico.
    """
    try:
        potencia_watts = float(input("Digite a potência do eletrodoméstico em Watts: "))
        horas_por_dia = float(input("Digite as horas de uso por dia: "))
        custo_kwh = float(input("Digite o custo do kWh na sua região (em reais): "))

        consumo_mensal = calcular_consumo_mensal(potencia_watts, horas_por_dia)
        custo_mensal = calcular_custo_mensal(consumo_mensal, custo_kwh)

        print(f"O consumo mensal do eletrodoméstico é de {consumo_mensal:.2f} kWh.")
        print(f"O custo mensal do eletrodoméstico é de R$ {custo_mensal:.2f}.")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == '__main__':
    main()