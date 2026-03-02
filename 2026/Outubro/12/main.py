import os
import time
import shutil

def calcular_velocidade_leitura(pasta):
    """
    Calcula a velocidade de leitura de uma pasta em MB/s.

    Args:
        pasta (str): O caminho da pasta para a qual a velocidade de leitura será medida.

    Returns:
        float: A velocidade de leitura em MB/s.
    """
    tamanho_arquivo = 1024 * 1024  # 1 MB
    arquivo_temporario = os.path.join(pasta, 'tempfile.tmp')

    # Cria um arquivo temporário de 1 MB
    with open(arquivo_temporario, 'wb') as f:
        f.write(os.urandom(tamanho_arquivo))

    # Mede o tempo para ler o arquivo
    inicio = time.time()
    with open(arquivo_temporario, 'rb') as f:
        f.read()
    fim = time.time()

    # Remove o arquivo temporário
    os.remove(arquivo_temporario)

    # Calcula a velocidade de leitura em MB/s
    tempo_decorrido = fim - inicio
    velocidade_leitura = tamanho_arquivo / tempo_decorrido / (1024 * 1024)
    return velocidade_leitura

def main():
    """
    Função principal que mede a velocidade de leitura de várias pastas.
    """
    pastas = [
        '/path/to/first/directory',
        '/path/to/second/directory',
        '/path/to/third/directory'
    ]

    for pasta in pastas:
        if os.path.exists(pasta):
            velocidade = calcular_velocidade_leitura(pasta)
            print(f"Velocidade de leitura para {pasta}: {velocidade:.2f} MB/s")
        else:
            print(f"Pasta {pasta} não existe.")

if __name__ == '__main__':
    main()