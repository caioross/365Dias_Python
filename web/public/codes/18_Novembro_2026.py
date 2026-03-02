import socket

def check_minecraft_server(host, port):
    """
    Verifica se um servidor de Minecraft está online e retorna o número de jogadores conectados.

    Args:
        host (str): O endereço IP ou hostname do servidor Minecraft.
        port (int): A porta do servidor Minecraft.

    Returns:
        tuple: Um tuple contendo um booleano indicando se o servidor está online e um inteiro com o número de jogadores conectados.
    """
    try:
        # Cria um socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define um timeout para a conexão
        sock.settimeout(5)
        # Conecta ao servidor
        sock.connect((host, port))
        # Envia o comando de status
        sock.send(b'\xFE\x01')
        # Recebe a resposta
        data = sock.recv(1024)
        # Fecha a conexão
        sock.close()

        # Decodifica a resposta
        decoded_data = data.decode('utf-16be')[1:].split('\x00')
        # Extrai o número de jogadores
        player_count = int(decoded_data[1].split(';')[0])
        return True, player_count

    except (socket.timeout, ConnectionRefusedError):
        return False, 0

def main():
    """
    Função principal que verifica o status do servidor Minecraft e imprime o número de jogadores conectados.
    """
    host = 'localhost'  # Substitua pelo endereço IP ou hostname do seu servidor
    port = 25565        # Porta padrão do Minecraft

    is_online, player_count = check_minecraft_server(host, port)
    if is_online:
        print(f"O servidor está online com {player_count} jogador(es) conectado(s).")
    else:
        print("O servidor está offline.")

if __name__ == '__main__':
    main()