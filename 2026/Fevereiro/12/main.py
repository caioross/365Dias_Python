import time
from datetime import datetime, timedelta

def agendar_lembrete(mensagem, intervalo_minutos):
    """
    Agenda um lembrete no terminal após um intervalo de tempo especificado.

    Args:
        mensagem (str): A mensagem do lembrete.
        intervalo_minutos (int): O intervalo de tempo em minutos para agendar o lembrete.
    """
    tempo_agendamento = datetime.now() + timedelta(minutes=intervalo_minutos)
    print(f"Lembrete agendado para {tempo_agendamento.strftime('%Y-%m-%d %H:%M:%S')}")

    time.sleep(intervalo_minutos * 60)
    print("\nLembrete:")
    print(mensagem)

def main():
    """
    Função principal que solicita ao usuário a mensagem e o intervalo de tempo,
    e então chama a função para agendar o lembrete.
    """
    mensagem = input("Digite a mensagem do lembrete: ")
    try:
        intervalo_minutos = int(input("Digite o intervalo de tempo em minutos: "))
        if intervalo_minutos < 0:
            raise ValueError("O intervalo de tempo deve ser um número não negativo.")
        agendar_lembrete(mensagem, intervalo_minutos)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()