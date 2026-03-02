import qrcode
from PIL import Image

def gerar_qr_code_wifi(ssid, senha, tipo_seguranca='WPA'):
    """
    Gera um QR Code para conexão Wi-Fi.

    Args:
        ssid (str): Nome da rede Wi-Fi.
        senha (str): Senha da rede Wi-Fi.
        tipo_seguranca (str): Tipo de segurança da rede (padrão é 'WPA').

    Returns:
        Image: Imagem do QR Code gerada.
    """
    dados_wifi = f'WIFI:S:{ssid};T:{tipo_seguranca};P:{senha};;'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dados_wifi)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    """
    Função principal que gera um QR Code para conexão Wi-Fi e salva a imagem.
    """
    ssid = input("Digite o nome da rede Wi-Fi: ")
    senha = input("Digite a senha da rede Wi-Fi: ")
    tipo_seguranca = input("Digite o tipo de segurança (padrão é WPA): ") or 'WPA'

    qr_code_image = gerar_qr_code_wifi(ssid, senha, tipo_seguranca)
    qr_code_image.save("qr_code_wifi.png")
    print("QR Code gerado e salvo como 'qr_code_wifi.png'.")

if __name__ == '__main__':
    main()