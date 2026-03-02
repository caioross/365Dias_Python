import xml.etree.ElementTree as ET

def validar_xml(caminho_arquivo):
    """
    Valida se um arquivo XML está bem formatado.

    Args:
        caminho_arquivo (str): O caminho para o arquivo XML que será validado.

    Returns:
        bool: True se o arquivo XML estiver bem formatado, False caso contrário.
    """
    try:
        # Tenta parsear o arquivo XML
        ET.parse(caminho_arquivo)
        return True
    except ET.ParseError:
        # Se houver um erro de parsing, o XML está mal formatado
        return False

def main():
    """
    Função principal que solicita o caminho do arquivo XML e verifica sua validade.
    """
    caminho_arquivo = input("Digite o caminho do arquivo XML: ")
    if validar_xml(caminho_arquivo):
        print("O arquivo XML está bem formatado.")
    else:
        print("O arquivo XML está mal formatado.")

if __name__ == '__main__':
    main()