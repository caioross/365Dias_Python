import ipaddress

def calcular_mascara_broadcast(ip_cidr):
    """
    Calcula a máscara de sub-rede e o IP de broadcast a partir de um endereço CIDR.

    Args:
        ip_cidr (str): Endereço IP no formato CIDR (por exemplo, '192.168.1.0/24').

    Returns:
        tuple: Uma tupla contendo a máscara de sub-rede e o IP de broadcast.
    """
    try:
        rede = ipaddress.ip_network(ip_cidr, strict=False)
        mascara_sub_rede = rede.netmask
        ip_broadcast = rede.broadcast_address
        return mascara_sub_rede, ip_broadcast
    except ValueError as e:
        raise ValueError(f"Endereço CIDR inválido: {e}")

def main():
    """
    Função principal que solicita ao usuário um endereço CIDR e exibe a máscara de sub-rede e o IP de broadcast.
    """
    ip_cidr = input("Digite o endereço IP no formato CIDR (por exemplo, '192.168.1.0/24'): ")
    try:
        mascara, broadcast = calcular_mascara_broadcast(ip_cidr)
        print(f"Máscara de sub-rede: {mascara}")
        print(f"IP de broadcast: {broadcast}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()