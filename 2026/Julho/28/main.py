import ssl
import socket
from datetime import datetime, timedelta

def get_ssl_expiry_date(hostname, port=443):
    """
    Obtém a data de expiração do certificado SSL de um host.

    :param hostname: Nome do host (site) para verificar o certificado SSL.
    :param port: Número da porta a ser usada para a conexão SSL (padrão é 443).
    :return: Data de expiração do certificado como um objeto datetime.
    """
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
    return expiry_date

def check_ssl_expiry(hostname, days_threshold=30):
    """
    Verifica se a data de expiração do certificado SSL está perto do fim.

    :param hostname: Nome do host (site) para verificar o certificado SSL.
    :param days_threshold: Número de dias antes da expiração para considerar como "perto do fim".
    :return: True se a expiração estiver perto do fim, False caso contrário.
    """
    expiry_date = get_ssl_expiry_date(hostname)
    days_until_expiry = (expiry_date - datetime.now()).days
    return days_until_expiry <= days_threshold

def main():
    """
    Função principal que verifica a validade do certificado SSL de um site e avisa se estiver perto do fim.
    """
    hostname = 'example.com'  # Substitua pelo hostname desejado
    if check_ssl_expiry(hostname):
        print(f"Aviso: O certificado SSL de {hostname} expira em menos de 30 dias.")
    else:
        print(f"O certificado SSL de {hostname} está válido por mais de 30 dias.")

if __name__ == '__main__':
    main()