"""
analisador_uso_bandwidth.py

Script para monitorar a quantidade de dados enviados e recebidos pela placa de rede.
"""

import psutil

def get_network_usage():
    """
    Obtém a quantidade de dados enviados e recebidos pela placa de rede.

    Returns:
        tuple: Uma tupla contendo o número de bytes enviados e recebidos.
    """
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_recv = net_io.bytes_recv
    return bytes_sent, bytes_recv

def main():
    """
    Função principal que executa o monitoramento da utilização de banda.
    """
    try:
        while True:
            sent, received = get_network_usage()
            print(f"Bytes enviados: {sent}, Bytes recebidos: {received}")
            # Adicione aqui a lógica para pausar ou encerrar o loop conforme necessário
    except KeyboardInterrupt:
        print("Monitoramento interrompido pelo usuário.")

if __name__ == '__main__':
    main()