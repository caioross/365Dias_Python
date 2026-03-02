import random
import string

def gerar_email_temporario():
    """
    Gera um endereço de e-mail aleatório.

    Returns:
        str: Um endereço de e-mail temporário no formato 'usuario@dominio.com'.
    """
    usuario = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    dominio = random.choice(['tempmail.com', 'mailinator.com', 'example.com', 'testmail.com'])
    return f"{usuario}@{dominio}"

def main():
    """
    Função principal que gera e exibe um endereço de e-mail temporário.
    """
    email = gerar_email_temporario()
    print(f"E-mail temporário gerado: {email}")

if __name__ == '__main__':
    main()