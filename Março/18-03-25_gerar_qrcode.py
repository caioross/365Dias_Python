import qrcode
from PIL import Image

def gerar_qr_code(dado, nome_arquivo="qrcode.png"):
    """
    Função para gerar um QR Code com os dados fornecidos e salvar em um arquivo.
    :param dado: O dado que será codificado no QR Code (por exemplo, uma URL).
    :param nome_arquivo: Nome do arquivo de saída (por padrão será "qrcode.png").
    """
    try:
        # Cria o objeto QR Code com os dados fornecidos
        qr = qrcode.QRCode(
            version=1,  # Tamanho do QR Code (1 é o menor)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
            box_size=10,  # Tamanho de cada box (bloco) do QR Code
            border=4,  # Espessura da borda
        )

        # Adiciona o dado ao QR Code
        qr.add_data(dado)
        qr.make(fit=True)  # Ajusta o QR Code ao tamanho do dado

        # Cria uma imagem a partir do QR Code
        img = qr.make_image(fill='black', back_color='white')

        # Salva a imagem do QR Code em um arquivo
        img.save(nome_arquivo)
        print(f"QR Code gerado com sucesso! Arquivo salvo como '{nome_arquivo}'")
        img.show()  # Exibe a imagem gerada
    except Exception as e:
        print(f"Erro ao gerar o QR Code: {e}")

if __name__ == "__main__":
    # Solicita ao usuário o dado a ser codificado
    dado = input("Digite o dado ou URL para gerar o QR Code: ")
    nome_arquivo = input("Digite o nome do arquivo para salvar (exemplo: qr_code.png): ")

    # Gera o QR Code
    gerar_qr_code(dado, nome_arquivo)
