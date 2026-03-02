import pyperclip
import time
import os

class ClipboardMonitor:
    """
    Classe para monitorar a área de transferência e salvar o histórico de textos copiados.
    """
    
    def __init__(self, log_file='clipboard_history.log'):
        """
        Inicializa o monitor com um arquivo de log especificado.
        
        :param log_file: Nome do arquivo onde o histórico será salvo.
        """
        self.log_file = log_file
        self.last_copied = ""

    def get_clipboard_content(self):
        """
        Obtém o conteúdo atual da área de transferência.
        
        :return: Conteúdo da área de transferência.
        """
        return pyperclip.paste()

    def save_to_log(self, content):
        """
        Salva o conteúdo fornecido para o arquivo de log.
        
        :param content: Conteúdo a ser salvo.
        """
        with open(self.log_file, 'a', encoding='utf-8') as file:
            file.write(content + '\n')

    def monitor(self, interval=1):
        """
        Monitora continuamente a área de transferência e salva o conteúdo se houver uma mudança.
        
        :param interval: Intervalo de tempo entre as verificações (em segundos).
        """
        while True:
            current_content = self.get_clipboard_content()
            if current_content != self.last_copied:
                self.save_to_log(current_content)
                self.last_copied = current_content
            time.sleep(interval)

def main():
    """
    Função principal para iniciar o monitoramento da área de transferência.
    """
    monitor = ClipboardMonitor()
    print("Monitoramento da área de transferência iniciado. Pressione Ctrl+C para parar.")
    try:
        monitor.monitor()
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido.")

if __name__ == '__main__':
    main()