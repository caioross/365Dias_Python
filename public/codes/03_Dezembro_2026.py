import os
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def load_pfx_certificate(file_path, password):
    """
    Load a PFX certificate from a file.

    :param file_path: Path to the PFX file.
    :param password: Password to decrypt the PFX file.
    :return: Loaded certificate.
    """
    with open(file_path, 'rb') as f:
        pfx_data = f.read()
    return x509.load_pkcs12(pfx_data, password=password, backend=default_backend()).certificate

def load_cer_certificate(file_path):
    """
    Load a CER certificate from a file.

    :param file_path: Path to the CER file.
    :return: Loaded certificate.
    """
    with open(file_path, 'rb') as f:
        cer_data = f.read()
    return x509.load_pem_x509_certificate(cer_data, backend=default_backend())

def validate_certificate(certificate):
    """
    Validate a certificate and extract the subject information.

    :param certificate: Loaded certificate object.
    :return: Dictionary containing the subject information.
    """
    subject = certificate.subject
    subject_info = {
        'common_name': subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value,
        'organization': subject.get_attributes_for_oid(x509.NameOID.ORGANIZATION_NAME)[0].value if subject.get_attributes_for_oid(x509.NameOID.ORGANIZATION_NAME) else None,
        'organizational_unit': subject.get_attributes_for_oid(x509.NameOID.ORGANIZATIONAL_UNIT_NAME)[0].value if subject.get_attributes_for_oid(x509.NameOID.ORGANIZATIONAL_UNIT_NAME) else None,
        'country': subject.get_attributes_for_oid(x509.NameOID.COUNTRY_NAME)[0].value if subject.get_attributes_for_oid(x509.NameOID.COUNTRY_NAME) else None
    }
    return subject_info

def main():
    """
    Main function to validate a certificate and display the subject information.
    """
    file_path = input("Enter the path to the certificate file (.pfx or .cer): ")
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    if file_path.lower().endswith('.pfx'):
        password = input("Enter the password to decrypt the PFX file: ").encode()
        try:
            certificate = load_pfx_certificate(file_path, password)
        except Exception as e:
            print(f"Error loading PFX certificate: {e}")
            return
    elif file_path.lower().endswith('.cer'):
        try:
            certificate = load_cer_certificate(file_path)
        except Exception as e:
            print(f"Error loading CER certificate: {e}")
            return
    else:
        print("Unsupported file format. Please provide a .pfx or .cer file.")
        return

    subject_info = validate_certificate(certificate)
    print("\nCertificate Information:")
    for key, value in subject_info.items():
        if value:
            print(f"{key.replace('_', ' ').capitalize()}: {value}")

if __name__ == '__main__':
    main()