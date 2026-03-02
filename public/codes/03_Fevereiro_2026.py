import os
from PIL import Image

def rename_photos_in_directory(directory, prefix='foto'):
    """
    Renomeia sequencialmente todos os arquivos de imagem em uma pasta.

    Args:
        directory (str): O caminho para o diretório contendo as imagens.
        prefix (str): O prefixo a ser usado nos novos nomes dos arquivos.

    Returns:
        None
    """
    # Verifica se o diretório existe
    if not os.path.exists(directory):
        raise ValueError(f"O diretório {directory} não existe.")

    # Lista todos os arquivos no diretório
    files = os.listdir(directory)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Renomeia os arquivos
    for index, old_name in enumerate(image_files, start=1):
        old_path = os.path.join(directory, old_name)
        new_name = f"{prefix}_{index}.jpg"
        new_path = os.path.join(directory, new_name)

        # Verifica se o arquivo é uma imagem válida antes de renomear
        try:
            with Image.open(old_path) as img:
                img.verify()  # Verifica se o arquivo é uma imagem válida
                os.rename(old_path, new_path)
        except Exception as e:
            print(f"Não foi possível renomear o arquivo {old_name}: {e}")

def main():
    """
    Função principal que executa o script de renomeação de fotos.
    """
    directory = input("Digite o caminho para o diretório contendo as imagens: ")
    try:
        rename_photos_in_directory(directory)
        print("Renomeação concluída com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()