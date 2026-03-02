"""
Script para gerar um QR Code que permite a conexão automática a uma rede Wi-Fi.
"""

import qrcode
from PIL import Image

def gerar_qr_code_wifi(ssid, password, security_type='WPA'):
    """
    Gera um QR Code para conexão automática a uma rede Wi-Fi.

    Args:
        ssid (str): Nome da rede Wi-Fi.
        password (str): Senha da rede Wi-Fi.
        security_type (str): Tipo de segurança da rede Wi-Fi (padrão é 'WPA').

    Returns:
        Image: Imagem do QR Code gerado.
    """
    wifi_data = f'WIFI:S:{ssid};T:{security_type};P:{password};;'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    """
    Função principal que gera um QR Code para uma rede Wi-Fi e salva a imagem.
    """
    ssid = input("Digite o nome da rede Wi-Fi: ")
    password = input("Digite a senha da rede Wi-Fi: ")
    security_type = input("Digite o tipo de segurança (padrão é WPA): ") or 'WPA'

    qr_code_image = gerar_qr_code_wifi(ssid, password, security_type)
    qr_code_image.save("wifi_qr_code.png")
    print("QR Code gerado e salvo como 'wifi_qr_code.png'.")

if __name__ == '__main__':
    main()