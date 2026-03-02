import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature

def load_public_key(key_path):
    """
    Carrega a chave pública a partir de um arquivo PEM.

    :param key_path: Caminho para o arquivo da chave pública.
    :return: Objeto de chave pública.
    :raises FileNotFoundError: Se o arquivo da chave pública não for encontrado.
    :raises ValueError: Se o arquivo não contiver uma chave pública válida.
    """
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"O arquivo de chave pública '{key_path}' não foi encontrado.")
    
    with open(key_path, 'rb') as key_file:
        public_key = load_pem_public_key(key_file.read())
    
    return public_key

def verify_signature(public_key, signature, message):
    """
    Verifica se a assinatura digital é válida para a mensagem fornecida.

    :param public_key: Objeto de chave pública.
    :param signature: Assinatura digital a ser verificada.
    :param message: Mensagem original que foi assinada.
    :return: True se a assinatura for válida, False caso contrário.
    :raises InvalidSignature: Se a assinatura for inválida.
    """
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

def main():
    """
    Função principal que carrega a chave pública, a assinatura e a mensagem,
    e verifica a validade da assinatura.
    """
    key_path = 'public_key.pem'
    signature_path = 'signature.bin'
    message_path = 'message.txt'

    try:
        public_key = load_public_key(key_path)

        with open(signature_path, 'rb') as sig_file:
            signature = sig_file.read()

        with open(message_path, 'rb') as msg_file:
            message = msg_file.read()

        if verify_signature(public_key, signature, message):
            print("A assinatura é válida.")
        else:
            print("A assinatura é inválida.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()