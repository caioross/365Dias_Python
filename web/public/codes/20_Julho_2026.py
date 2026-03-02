import os
import shutil

def organize_downloads(download_path, document_types, image_types, video_types):
    """
    Organiza arquivos na pasta Downloads movendo-os para subpastas baseadas em suas extensões.

    :param download_path: Caminho para a pasta Downloads.
    :param document_types: Lista de extensões para arquivos de documentos.
    :param image_types: Lista de extensões para arquivos de imagens.
    :param video_types: Lista de extensões para arquivos de vídeos.
    """
    # Dicionário mapeando extensões para pastas
    extension_folders = {
        'documentos': document_types,
        'imagens': image_types,
        'vídeos': video_types
    }

    # Cria pastas se elas não existirem
    for folder in extension_folders:
        folder_path = os.path.join(download_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move arquivos para as pastas corretas
    for filename in os.listdir(download_path):
        file_path = os.path.join(download_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            for folder, extensions in extension_folders.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(download_path, folder, filename))
                    break

def main():
    download_path = os.path.expanduser("~/Downloads")
    document_types = ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx']
    image_types = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    video_types = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']

    organize_downloads(download_path, document_types, image_types, video_types)
    print("Arquivos organizados com sucesso!")

if __name__ == '__main__':
    main()