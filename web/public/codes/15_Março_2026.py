"""
testador_velocidade_internet.py

Este script realiza um teste básico de download e upload da conexão de internet atual.
Ele utiliza a biblioteca speedtest-cli para medir a velocidade da internet.

Para instalar a biblioteca speedtest-cli, use o comando:
pip install speedtest-cli

Uso:
python testador_velocidade_internet.py
"""

import speedtest

def testar_velocidade():
    """
    Realiza o teste de velocidade de download e upload.

    Retorna:
        dict: Um dicionário contendo a velocidade de download e upload em Mbps.
    """
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convertendo bytes para Mbps
    upload_speed = st.upload() / 1_000_000  # Convertendo bytes para Mbps

    return {
        'download': download_speed,
        'upload': upload_speed
    }

def main():
    """
    Função principal que executa o teste de velocidade e imprime os resultados.
    """
    resultados = testar_velocidade()
    print(f"Velocidade de Download: {resultados['download']:.2f} Mbps")
    print(f"Velocidade de Upload: {resultados['upload']:.2f} Mbps")

if __name__ == '__main__':
    main()