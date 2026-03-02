import argparse

def calcular_evolucao_capital(capital_inicial, taxa_cdi, tempo_meses):
    """
    Calcula a evolução de um capital baseado na taxa percentual do CDI e tempo em meses.

    Args:
        capital_inicial (float): O valor inicial do capital a ser investido.
        taxa_cdi (float): A taxa percentual do CDI (por exemplo, 12.5 para 12,5%).
        tempo_meses (int): O tempo em meses que o capital ficará investido.

    Returns:
        float: O valor do capital após a aplicação da taxa CDI por período.
    """
    taxa_cdi_decimal = taxa_cdi / 100
    fator_multiplicador = (1 + taxa_cdi_decimal) ** tempo_meses
    capital_final = capital_inicial * fator_multiplicador
    return capital_final

def main():
    """
    Função principal que executa o simulador de investimento CDI.
    """
    parser = argparse.ArgumentParser(description='Simula a evolução de um capital com base na taxa CDI.')
    parser.add_argument('capital_inicial', type=float, help='Capital inicial a ser investido')
    parser.add_argument('taxa_cdi', type=float, help='Taxa percentual do CDI')
    parser.add_argument('tempo_meses', type=int, help='Tempo em meses do investimento')

    args = parser.parse_args()

    capital_final = calcular_evolucao_capital(args.capital_inicial, args.taxa_cdi, args.tempo_meses)
    print(f'O capital final após {args.tempo_meses} meses será de R$ {capital_final:.2f}')

if __name__ == '__main__':
    main()