import qrcode
from PIL import Image
import base64
import json

def generate_pix_qr_code(payload):
    """
    Gera um QR Code para recebimento via Pix e retorna o código "Copia e Cola" e a imagem do QR Code.

    Args:
        payload (dict): Dicionário contendo os dados do Pix.

    Returns:
        tuple: Uma tupla contendo o código "Copia e Cola" e a imagem do QR Code (PIL Image).
    """
    # Convertendo o payload para JSON
    payload_json = json.dumps(payload, separators=(',', ':'))

    # Codificando o payload em base64
    payload_base64 = base64.b64encode(payload_json.encode('utf-8')).decode('utf-8')

    # Criando o código "Copia e Cola"
    pix_copia_e_cola = f"pix:{payload_base64}"

    # Gerando o QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(pix_copia_e_cola)
    qr.make(fit=True)

    # Criando a imagem do QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    return pix_copia_e_cola, img

def main():
    """
    Função principal que gera um QR Code Pix e salva a imagem.
    """
    # Exemplo de payload para Pix
    payload = {
        "de": "MERCHANT",
        "chave": "merchant@domain.com",
        "txid": "12345678901234567890",
        "valor": "100.00",
        "info": "Pagamento de serviços"
    }

    # Gerando o QR Code Pix
    pix_copia_e_cola, qr_code_image = generate_pix_qr_code(payload)

    # Exibindo o código "Copia e Cola"
    print("Código 'Copia e Cola':")
    print(pix_copia_e_cola)

    # Salvando a imagem do QR Code
    qr_code_image.save("qr_code_pix.png")
    print("QR Code salvo como 'qr_code_pix.png'")

if __name__ == '__main__':
    main()