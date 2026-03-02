"""
monitor_temperatura_hd_ssd.py

Script para monitorar a temperatura do disco rígido ou SSD usando S.M.A.R.T.
Alerta se a temperatura ultrapassar os níveis de segurança definidos.

Requisitos:
- smartmontools instalados no sistema
- Permissões de root para executar smartctl
"""

import subprocess
import sys

def get_smart_data(device):
    """
    Executa o comando smartctl para obter dados SMART do dispositivo.

    :param device: Nome do dispositivo (ex: /dev/sda)
    :return: Saída do comando smartctl como string
    """
    try:
        result = subprocess.run(['sudo', 'smartctl', '-a', device], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao obter dados SMART: {e.stderr}", file=sys.stderr)
        sys.exit(1)

def parse_temperature(smart_data):
    """
    Parseia a saída do smartctl para extrair a temperatura do disco.

    :param smart_data: String contendo os dados SMART
    :return: Temperatura do disco como int, ou None se não encontrado
    """
    for line in smart_data.splitlines():
        if 'Temperature_Celsius' in line:
            return int(line.split()[1])
    return None

def check_temperature(device, threshold):
    """
    Verifica se a temperatura do dispositivo está acima do limite.

    :param device: Nome do dispositivo (ex: /dev/sda)
    :param threshold: Limite de temperatura seguro
    :return: True se a temperatura estiver acima do limite, False caso contrário
    """
    smart_data = get_smart_data(device)
    temperature = parse_temperature(smart_data)
    if temperature is not None:
        return temperature > threshold
    return False

def main():
    """
    Função principal para monitorar a temperatura do disco.
    """
    device = '/dev/sda'  # Substitua pelo dispositivo correto
    temperature_threshold = 60  # Limite de temperatura seguro em Celsius

    if check_temperature(device, temperature_threshold):
        print(f"Alerta: A temperatura do disco {device} está acima do limite seguro ({temperature_threshold}°C).")
    else:
        print(f"A temperatura do disco {device} está dentro do limite seguro.")

if __name__ == '__main__':
    main()