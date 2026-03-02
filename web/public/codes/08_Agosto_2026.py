import socket

def check_port(host, port):
    """
    Verifica se a porta especificada está aberta no host fornecido.

    :param host: O endereço IP ou nome do host a ser verificado.
    :param port: O número da porta a ser verificada.
    :return: True se a porta estiver aberta, False caso contrário.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        return result == 0

def main():
    """
    Função principal que verifica a disponibilidade das portas 80, 443 e 3306 em um servidor ou IP.
    """
    host = input("Digite o endereço IP ou nome do host: ")
    ports_to_check = [80, 443, 3306]

    for port in ports_to_check:
        if check_port(host, port):
            print(f"Porta {port} está aberta.")
        else:
            print(f"Porta {port} está fechada.")

if __name__ == '__main__':
    main()