import time
import os

def tail_file(file_path):
    """
    Monitora um arquivo de log em tempo real, imprimindo novas linhas à medida que elas são escritas.

    :param file_path: Caminho para o arquivo de log a ser monitorado.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não existe.")

    with open(file_path, 'r') as file:
        # Move o cursor para o final do arquivo
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Aguarda um pouco antes de tentar novamente
                continue
            print(line, end='')  # Imprime a nova linha sem adicionar um novo \n

def main():
    """
    Função principal que inicia o monitoramento do arquivo de log.
    """
    log_file_path = 'path/to/your/logfile.log'  # Substitua pelo caminho real do seu arquivo de log
    try:
        tail_file(log_file_path)
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()