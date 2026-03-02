"""
gerador_assinatura_email.py

Script para gerar um código HTML para uma assinatura de e-mail personalizada,
incluindo uma foto e links para redes sociais.
"""

def gerar_assinatura_html(nome, cargo, email, telefone, foto_url, redes_sociais):
    """
    Gera um código HTML para uma assinatura de e-mail personalizada.

    :param nome: Nome do assinante.
    :param cargo: Cargo do assinante.
    :param email: Endereço de e-mail do assinante.
    :param telefone: Número de telefone do assinante.
    :param foto_url: URL da foto do assinante.
    :param redes_sociais: Dicionário com nomes das redes sociais como chaves e URLs como valores.
    :return: Código HTML da assinatura de e-mail.
    """
    html = f"""
    <div style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; text-align: center;">
        <img src="{foto_url}" alt="Foto de {nome}" style="border-radius: 50%; width: 100px; height: 100px;">
        <h2>{nome}</h2>
        <p><strong>Cargo:</strong> {cargo}</p>
        <p><strong>E-mail:</strong> <a href="mailto:{email}">{email}</a></p>
        <p><strong>Telefone:</strong> {telefone}</p>
        <div>
            {''.join(f'<a href="{url}" target="_blank" style="margin: 0 10px;"><img src="https://img.icons8.com/color/48/{social}.png" alt="{social}"/></a>' for social, url in redes_sociais.items())}
        </div>
    </div>
    """
    return html

def main():
    """
    Função principal para demonstrar o uso do gerador de assinatura de e-mail.
    """
    nome = "João Silva"
    cargo = "Engenheiro de Software"
    email = "joao.silva@example.com"
    telefone = "(12) 3456-7890"
    foto_url = "https://example.com/joao_silva.jpg"
    redes_sociais = {
        "linkedin": "https://www.linkedin.com/in/joaosilva",
        "github": "https://github.com/joaosilva",
        "twitter": "https://twitter.com/joaosilva"
    }

    assinatura_html = gerar_assinatura_html(nome, cargo, email, telefone, foto_url, redes_sociais)
    print(assinatura_html)

if __name__ == '__main__':
    main()