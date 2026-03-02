import os
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import AuthError

class CloudBackup:
    """
    Classe para sincronizar arquivos locais com o Dropbox.
    """

    def __init__(self, access_token, local_folder, cloud_folder):
        """
        Inicializa a classe com o token de acesso, pasta local e pasta do Dropbox.

        :param access_token: Token de acesso ao Dropbox.
        :param local_folder: Caminho para a pasta local de fotos.
        :param cloud_folder: Caminho para a pasta no Dropbox.
        """
        self.dbx = dropbox.Dropbox(access_token)
        self.local_folder = local_folder
        self.cloud_folder = cloud_folder

    def upload_file(self, file_path, cloud_path):
        """
        Faz o upload de um arquivo para o Dropbox.

        :param file_path: Caminho do arquivo local.
        :param cloud_path: Caminho do arquivo no Dropbox.
        """
        with open(file_path, 'rb') as f:
            self.dbx.files_upload(f.read(), cloud_path, mode=WriteMode('overwrite'))

    def sync_files(self):
        """
        Sincroniza os arquivos da pasta local com o Dropbox.
        """
        for root, dirs, files in os.walk(self.local_folder):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, self.local_folder)
                cloud_file_path = os.path.join(self.cloud_folder, relative_path)

                # Cria a pasta no Dropbox se necessário
                cloud_dir = os.path.dirname(cloud_file_path)
                if cloud_dir and not self.dbx.files_list_folder(cloud_dir).entries:
                    self.dbx.files_create_folder_v2(cloud_dir)

                # Faz o upload do arquivo
                self.upload_file(local_file_path, cloud_file_path)
                print(f'Uploaded: {local_file_path} to {cloud_file_path}')

def main():
    """
    Função principal para executar o script de backup.
    """
    access_token = 'YOUR_ACCESS_TOKEN'
    local_folder = '/path/to/local/folder'
    cloud_folder = '/path/to/cloud/folder'

    backup = CloudBackup(access_token, local_folder, cloud_folder)
    backup.sync_files()

if __name__ == '__main__':
    main()