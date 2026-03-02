"""
monitor_temperatura_cpu.py

Script para monitorar e exibir a temperatura atual dos núcleos do processador.
"""

import psutil

def get_cpu_temperature():
    """
    Obtém a temperatura do processador.

    Returns:
        float: Temperatura do processador em graus Celsius.
    """
    temps = psutil.sensors_temperatures()
    if 'coretemp' in temps:
        core_temp = temps['coretemp']
        # Retorna a temperatura média de todos os núcleos
        return sum(temp.current for temp in core_temp) / len(core_temp)
    else:
        raise RuntimeError("Não foi possível obter a temperatura do processador.")

def main():
    """
    Função principal que exibe a temperatura atual do processador.
    """
    try:
        temperature = get_cpu_temperature()
        print(f"Temperatura atual do processador: {temperature:.2f}°C")
    except Exception as e:
        print(f"Erro ao obter a temperatura do processador: {e}")

if __name__ == '__main__':
    main()