import random
from datetime import datetime, timedelta

def gerar_horario_aleatorio(inicio, fim):
    """
    Gera um horário aleatório dentro de um intervalo especificado.

    :param inicio: Hora de início do intervalo (datetime.time).
    :param fim: Hora de término do intervalo (datetime.time).
    :return: Horário aleatório dentro do intervalo (datetime.time).
    """
    delta = timedelta(hours=fim.hour - inicio.hour, minutes=fim.minute - inicio.minute)
    segundos = random.randint(0, int(delta.total_seconds()))
    return (datetime.min + timedelta(seconds=segundos)).time()

def gerar_espelho_ponto(quantidade_dias):
    """
    Gera um espelho de ponto com horários aleatórios para uma quantidade especificada de dias.

    :param quantidade_dias: Número de dias para gerar o espelho de ponto.
    :return: Lista de strings representando o espelho de ponto.
    """
    horario_entrada = datetime.strptime('08:00', '%H:%M').time()
    horario_intervalo = datetime.strptime('12:00', '%H:%M').time()
    horario_volta = datetime.strptime('13:00', '%H:%M').time()
    horario_saida = datetime.strptime('18:00', '%H:%M').time()

    espelho_ponto = []

    for dia in range(1, quantidade_dias + 1):
        data = datetime.now().replace(day=dia, hour=0, minute=0, second=0, microsecond=0)
        entrada = gerar_horario_aleatorio(horario_entrada, horario_intervalo)
        intervalo = gerar_horario_aleatorio(horario_intervalo, horario_volta)
        volta = gerar_horario_aleatorio(horario_volta, horario_saida)
        saida = gerar_horario_aleatorio(horario_volta, horario_saida)

        linha = f"{data.strftime('%d/%m/%Y')} - Entrada: {entrada.strftime('%H:%M')} - Intervalo: {intervalo.strftime('%H:%M')} - Volta: {volta.strftime('%H:%M')} - Saída: {saida.strftime('%H:%M')}"
        espelho_ponto.append(linha)

    return espelho_ponto

def salvar_espelho_ponto_em_arquivo(espelho_ponto, nome_arquivo):
    """
    Salva o espelho de ponto em um arquivo de texto.

    :param espelho_ponto: Lista de strings representando o espelho de ponto.
    :param nome_arquivo: Nome do arquivo onde salvar o espelho de ponto.
    """
    with open(nome_arquivo, 'w') as arquivo:
        for linha in espelho_ponto:
            arquivo.write(linha + '\n')

def main():
    """
    Função principal que gera e salva o espelho de ponto.
    """
    quantidade_dias = 30  # Gera um mês com 30 dias
    espelho_ponto = gerar_espelho_ponto(quantidade_dias)
    nome_arquivo = 'espelho_ponto.txt'
    salvar_espelho_ponto_em_arquivo(espelho_ponto, nome_arquivo)
    print(f"Espelho de ponto gerado e salvo em {nome_arquivo}")

if __name__ == '__main__':
    main()