import os
import threading
import time

def ping_host(host):
    """
    Dispara um ping para o host especificado e retorna o status.

    :param host: O endereço do host a ser pingado.
    :return: Uma string indicando o status do ping.
    """
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    return f"Host {host} is {'up' if response == 0 else 'down'}"

def monitor_host(host, interval):
    """
    Monitora o host a cada intervalo de tempo especificado.

    :param host: O endereço do host a ser monitorado.
    :param interval: O intervalo de tempo entre os pings (em segundos).
    """
    while True:
        status = ping_host(host)
        print(status)
        time.sleep(interval)

def main():
    """
    Função principal que inicia a monitorização de múltiplos hosts.
    """
    hosts = ["8.8.8.8", "1.1.1.1", "google.com"]  # Adicione os hosts que deseja monitorar
    interval = 5  # Intervalo de tempo entre os pings (em segundos)

    threads = []
    for host in hosts:
        thread = threading.Thread(target=monitor_host, args=(host, interval))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()