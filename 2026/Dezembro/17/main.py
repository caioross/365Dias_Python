import qrcode
from PIL import Image

def generate_qr_code(data, filename):
    """
    Gera um QR Code com base nos dados fornecidos e salva em um arquivo.

    Args:
        data (str): O URL ou dados que o QR Code deve redirecionar.
        filename (str): O nome do arquivo onde o QR Code será salvo.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    """
    Função principal que gera um QR Code para um serviço de redirecionamento próprio.
    """
    redirect_url = "https://seuservicoderedirecionamento.com"
    output_filename = "qrcode.png"
    generate_qr_code(redirect_url, output_filename)
    print(f"QR Code gerado e salvo como {output_filename}")

if __name__ == '__main__':
    main()