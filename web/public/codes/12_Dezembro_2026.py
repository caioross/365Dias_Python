"""
monitor_saude_ssd_smart.py

Script para monitorar os atributos S.M.A.R.T. de um SSD e alertar se houver risco iminente de falha.
"""

import subprocess
import sys

def obter_smart_attributes(device):
    """
    Obtém os atributos S.M.A.R.T. de um dispositivo SSD.

    :param device: Nome do dispositivo (ex: /dev/sda)
    :return: Lista de atributos S.M.A.R.T.
    """
    try:
        output = subprocess.check_output(['smartctl', '-a', device]).decode('utf-8')
        return output
    except subprocess.CalledProcessError as e:
        print(f"Erro ao obter atributos S.M.A.R.T.: {e}", file=sys.stderr)
        return None

def analisar_risco_falha(attributes):
    """
    Analisa os atributos S.M.A.R.T. para identificar riscos iminentes de falha.

    :param attributes: Saída dos atributos S.M.A.R.T.
    :return: True se houver risco iminente, False caso contrário.
    """
    # Exemplo de análise simplificada (deve ser adaptado com base nos atributos específicos do SSD)
    if "Reallocated_Sector_Ct" in attributes and "1" in attributes:
        return True
    if "Pending_Sector_Ct" in attributes and "1" in attributes:
        return True
    return False

def main():
    """
    Função principal do script.
    """
    device = "/dev/sda"  # Substitua pelo dispositivo correto
    attributes = obter_smart_attributes(device)
    if attributes:
        if analisar_risco_falha(attributes):
            print("Risco iminente de falha detectado no SSD.")
        else:
            print("SSD está em boas condições.")

if __name__ == '__main__':
    main()