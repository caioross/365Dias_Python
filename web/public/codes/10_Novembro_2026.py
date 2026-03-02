import os
import shutil
from datetime import datetime

def move_files_to_date_based_folders(directory):
    """
    Move arquivos de um diretório para pastas baseadas na data de criação (Ano/Mês).

    Args:
        directory (str): O caminho do diretório onde os arquivos estão localizados.
    """
    # Verifica se o diretório existe
    if not os.path.exists(directory):
        print(f"O diretório {directory} não existe.")
        return

    # Itera sobre todos os arquivos no diretório
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Ignora se for um diretório
        if os.path.isdir(file_path):
            continue

        # Obtém a data de criação do arquivo
        try:
            creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
        except OSError:
            print(f"Não foi possível obter a data de criação para o arquivo: {file_path}")
            continue

        # Cria o caminho da pasta baseado na data de criação
        year_folder = os.path.join(directory, str(creation_time.year))
        month_folder = os.path.join(year_folder, str(creation_time.month).zfill(2))

        # Cria as pastas se elas não existirem
        os.makedirs(month_folder, exist_ok=True)

        # Move o arquivo para a pasta correta
        new_file_path = os.path.join(month_folder, filename)
        try:
            shutil.move(file_path, new_file_path)
            print(f"Arquivo movido para: {new_file_path}")
        except Exception as e:
            print(f"Erro ao mover o arquivo {file_path}: {e}")

def main():
    """
    Função principal que executa o script de organização de pastas.
    """
    # Defina o diretório onde os arquivos estão localizados
    target_directory = input("Digite o caminho do diretório a ser organizado: ")
    
    # Chama a função para organizar os arquivos
    move_files_to_date_based_folders(target_directory)

if __name__ == '__main__':
    main()