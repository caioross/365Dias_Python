import os
import struct
import sys

def is_executable(file_path):
    """
    Verifica se o arquivo é executável.

    :param file_path: Caminho do arquivo a ser verificado.
    :return: True se o arquivo é executável, False caso contrário.
    """
    return os.access(file_path, os.X_OK)

def get_architecture(file_path):
    """
    Determina a arquitetura do arquivo binário executável.

    :param file_path: Caminho do arquivo binário executável.
    :return: Arquitetura do arquivo ('32-bit' ou '64-bit') ou None se não puder determinar.
    """
    try:
        with open(file_path, 'rb') as f:
            # Lê os primeiros 4 bytes do arquivo
            header = f.read(4)
            if header == b'\x7fELF':
                # Lê o byte que indica a classe (32-bit ou 64-bit)
                f.seek(4)
                class_ = f.read(1)
                if class_ == b'\x01':
                    return '32-bit'
                elif class_ == b'\x02':
                    return '64-bit'
    except (IOError, OSError) as e:
        print(f"Erro ao ler o arquivo: {e}", file=sys.stderr)
    return None

def main():
    """
    Função principal que verifica se um arquivo é executável e qual é a sua arquitetura.
    """
    if len(sys.argv) != 2:
        print("Uso: python verificador_arquivo_executavel.py <caminho_do_arquivo>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"O arquivo '{file_path}' não existe.")
        sys.exit(1)

    if is_executable(file_path):
        architecture = get_architecture(file_path)
        if architecture:
            print(f"O arquivo '{file_path}' é executável e tem arquitetura {architecture}.")
        else:
            print(f"O arquivo '{file_path}' é executável, mas não foi possível determinar a arquitetura.")
    else:
        print(f"O arquivo '{file_path}' não é executável.")

if __name__ == '__main__':
    main()