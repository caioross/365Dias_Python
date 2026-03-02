import sys

def check_python_version(major, minor):
    """
    Verifica se a versão atual do Python é compatível com a versão especificada.

    Args:
        major (int): O número major da versão do Python.
        minor (int): O número minor da versão do Python.

    Returns:
        bool: True se a versão do Python é compatível, False caso contrário.
    """
    current_major, current_minor = sys.version_info.major, sys.version_info.minor
    return current_major > major or (current_major == major and current_minor >= minor)

def main():
    """
    Função principal que verifica a compatibilidade da versão do Python.
    """
    required_major = 3
    required_minor = 8

    if not check_python_version(required_major, required_minor):
        print(f"Este script requer Python {required_major}.{required_minor} ou superior.")
        sys.exit(1)

    print(f"Compatível com Python {sys.version_info.major}.{sys.version_info.minor}")

if __name__ == '__main__':
    main()