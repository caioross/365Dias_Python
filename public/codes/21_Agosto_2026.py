import datetime
import holidays

def calcular_data_final(data_inicial, prazo_dias_uteis, feriados=None):
    """
    Calcula a data final de um prazo considerando apenas dias úteis e feriados nacionais.

    Args:
        data_inicial (datetime.date): A data inicial do prazo.
        prazo_dias_uteis (int): O número de dias úteis desejados.
        feriados (list, optional): Uma lista de feriados adicionais. Defaults to None.

    Returns:
        datetime.date: A data final do prazo.
    """
    if feriados is None:
        feriados = []

    # Converter feriados para datetime.date se necessário
    feriados = [datetime.date.fromisoformat(feriado) if isinstance(feriado, str) else feriado for feriado in feriados]

    data_corrente = data_inicial
    dias_uteis_contados = 0

    while dias_uteis_contados < prazo_dias_uteis:
        data_corrente += datetime.timedelta(days=1)
        if data_corrente.weekday() < 5 and data_corrente not in feriados:
            dias_uteis_contados += 1

    return data_corrente

def main():
    # Exemplo de uso
    data_inicial = datetime.date(2023, 10, 1)
    prazo_dias_uteis = 10
    feriados = ['2023-10-12', '2023-10-13']  # Exemplo de feriados adicionais

    data_final = calcular_data_final(data_inicial, prazo_dias_uteis, feriados)
    print(f"A data final do prazo é: {data_final}")

if __name__ == '__main__':
    main()