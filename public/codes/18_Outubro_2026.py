"""
calculadora_pegada_carbono.py

Este script estima a emissão de CO2 baseada em quilômetros rodados e consumo de energia.
"""

def calcular_emissao_co2(km_rodados, consumo_energia, fator_emissao=0.2):
    """
    Calcula a emissão de CO2.

    Args:
        km_rodados (float): Quantidade de quilômetros rodados.
        consumo_energia (float): Consumo de energia em kWh por quilômetro.
        fator_emissao (float, optional): Fator de emissão de CO2 em kg CO2/kWh. Padrão é 0.2 kg CO2/kWh.

    Returns:
        float: Emissão de CO2 em kg.
    """
    emissao_co2 = km_rodados * consumo_energia * fator_emissao
    return emissao_co2

def main():
    """
    Função principal que executa o script.
    """
    km_rodados = float(input("Digite a quantidade de quilômetros rodados: "))
    consumo_energia = float(input("Digite o consumo de energia em kWh por quilômetro: "))

    emissao_co2 = calcular_emissao_co2(km_rodados, consumo_energia)
    print(f"A emissão de CO2 estimada é de {emissao_co2:.2f} kg.")

if __name__ == '__main__':
    main()