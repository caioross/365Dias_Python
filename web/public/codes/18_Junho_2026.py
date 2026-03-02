import os
import time
import subprocess

def monitor_file_change(file_path, command):
    """
    Monitora um arquivo específico e executa um comando quando o arquivo é alterado.

    :param file_path: Caminho para o arquivo a ser monitorado.
    :param command: Comando a ser executado quando o arquivo é alterado.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não existe.")

    # Obter o timestamp inicial do arquivo
    initial_mtime = os.path.getmtime(file_path)
    print(f"Monitorando o arquivo: {file_path}")

    try:
        while True:
            # Verificar o timestamp atual do arquivo
            current_mtime = os.path.getmtime(file_path)
            
            # Comparar o timestamp atual com o inicial
            if current_mtime != initial_mtime:
                print("Detectada alteração no arquivo. Executando o comando...")
                subprocess.run(command, shell=True, check=True)
                # Atualizar o timestamp inicial para o atual
                initial_mtime = current_mtime
            
            # Esperar por um intervalo antes de verificar novamente
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoramento interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    """
    Função principal que configura o arquivo a ser monitorado e o comando a ser executado.
    """
    file_path = 'caminho/para/seu/arquivo.txt'  # Substitua pelo caminho do seu arquivo
    command = 'echo "Arquivo alterado!"'  # Substitua pelo comando que você deseja executar

    monitor_file_change(file_path, command)

if __name__ == '__main__':
    main()