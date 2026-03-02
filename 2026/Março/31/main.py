import re

def extrair_dominios_emails(emails):
    """
    Extrai os domínios de uma lista de e-mails.

    Args:
        emails (list): Uma lista de strings, onde cada string é um e-mail.

    Returns:
        list: Uma lista de strings, onde cada string é um domínio extraído dos e-mails.
    """
    dominios = []
    dominio_padrao = re.compile(r'@([\w.]+)')

    for email in emails:
        match = dominio_padrao.search(email)
        if match:
            dominios.append(match.group(1))

    return dominios

def main():
    emails = [
        "usuario1@gmail.com",
        "usuario2@outlook.com",
        "usuario3@yahoo.com",
        "usuario4@hotmail.com"
    ]

    dominios = extrair_dominios_emails(emails)
    print("Domínios extraídos:", dominios)

if __name__ == '__main__':
    main()