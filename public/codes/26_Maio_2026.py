"""
testador_frequencia_processador.py

Este script monitora a variação da velocidade de clock do processador em tempo real.
"""

import time
import psutil

def get_cpu_frequency():
    """
    Obtém a frequência atual do processador.

    Returns:
        float: Frequência do processador em MHz.
    """
    return psutil.cpu_freq().current

def monitor_cpu_frequency(interval=1):
    """
    Monitora a variação da frequência do processador em tempo real.

    Args:
        interval (int): Intervalo de tempo entre as medições em segundos.
    """
    print("Monitorando a frequência do processador...")
    try:
        while True:
            current_frequency = get_cpu_frequency()
            print(f"Frequência atual do processador: {current_frequency:.2f} MHz")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido pelo usuário.")

def main():
    """
    Função principal que inicia o monitoramento da frequência do processador.
    """
    monitor_cpu_frequency()

if __name__ == '__main__':
    main()