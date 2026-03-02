import whois

def is_domain_available(domain):
    """
    Verifica se um domínio está disponível para registro usando consulta WHOIS.

    Args:
        domain (str): O domínio a ser verificado.

    Returns:
        bool: True se o domínio estiver disponível, False caso contrário.
    """
    try:
        w = whois.whois(domain)
        return w.domain_name is None
    except whois.parser.PywhoisError:
        return True

def main():
    """
    Função principal que solicita ao usuário um domínio e verifica sua disponibilidade.
    """
    domain = input("Digite o domínio que deseja verificar (.com.br ou .com): ")
    if is_domain_available(domain):
        print(f"O domínio {domain} está disponível para registro.")
    else:
        print(f"O domínio {domain} já está registrado.")

if __name__ == '__main__':
    main()