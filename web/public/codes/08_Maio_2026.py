import psutil
import time
import os

def get_ram_usage():
    """
    Retorna o percentual de uso da RAM.
    
    Returns:
        float: Percentual de uso da RAM.
    """
    return psutil.virtual_memory().percent

def notify_user(message):
    """
    Envia uma notificação ao usuário.
    
    Args:
        message (str): Mensagem da notificação.
    """
    if os.name == 'nt':  # Windows
        os.system(f'echo {message} | powershell -c "Add-Type -TypeDefinition \'using System; using System.Windows.Forms; public class Notifier {{ public static void Show(string message) {{ MessageBox.Show(message); }} }}\'; [Notifier]::Show(\'{message}\');"')
    elif os.name == 'posix':  # macOS/Linux
        os.system(f'notify-send "Alerta de Uso de RAM" "{message}"')

def monitor_ram_usage(threshold):
    """
    Monitora o uso de RAM e envia uma notificação se o uso ultrapassar o limite definido.
    
    Args:
        threshold (float): Limite percentual de uso da RAM.
    """
    while True:
        ram_usage = get_ram_usage()
        if ram_usage > threshold:
            notify_user(f"Uso de RAM está acima do limite: {ram_usage}%")
        time.sleep(60)  # Verifica a cada minuto

def main():
    """
    Função principal que inicia o monitoramento do uso de RAM.
    """
    threshold = 80.0  # Define o limite de uso de RAM em percentual
    monitor_ram_usage(threshold)

if __name__ == '__main__':
    main()