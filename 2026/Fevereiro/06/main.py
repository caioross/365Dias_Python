import os
import shutil
from datetime import datetime

def backup_incremental(source_dir, backup_dir):
    """
    Realiza um backup incremental, copiando apenas os arquivos novos ou modificados
    da pasta de origem para a pasta de destino de backup.

    :param source_dir: Caminho para a pasta de origem.
    :param backup_dir: Caminho para a pasta de destino de backup.
    """
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(source_file, source_dir)
            backup_file = os.path.join(backup_dir, relative_path)

            # Cria diretórios necessários no backup_dir
            os.makedirs(os.path.dirname(backup_file), exist_ok=True)

            # Verifica se o arquivo já existe no backup_dir e se é mais novo
            if not os.path.exists(backup_file) or os.path.getmtime(source_file) > os.path.getmtime(backup_file):
                shutil.copy2(source_file, backup_file)
                print(f"Copiado: {source_file} -> {backup_file}")

def main():
    source_directory = 'caminho/para/pasta/origem'
    backup_directory = 'caminho/para/pasta/backup'
    backup_incremental(source_directory, backup_directory)

if __name__ == '__main__':
    main()