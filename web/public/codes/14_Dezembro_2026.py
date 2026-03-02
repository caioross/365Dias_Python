"""
gerador_template_email_marketing.py

Script para gerar um template HTML responsivo para campanhas de e-mail marketing.
O template inclui botões e imagens.
"""

from datetime import datetime

def gerar_template_email():
    """
    Gera um template HTML responsivo para campanhas de e-mail marketing.
    
    Returns:
        str: Um string contendo o código HTML do template.
    """
    template = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Campanha de E-mail Marketing</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                padding: 20px 0;
            }}
            .content {{
                padding: 20px;
            }}
            .footer {{
                text-align: center;
                padding: 10px 0;
                background-color: #f9f9f9;
                margin-top: 20px;
            }}
            .button {{
                display: inline-block;
                padding: 10px 20px;
                background-color: #007BFF;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
            }}
            .button:hover {{
                background-color: #0056b3;
            }}
            img {{
                max-width: 100%;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Bem-vindo à nossa Newsletter</h1>
                <p>Data: {datetime.now().strftime('%d/%m/%Y')}</p>
            </div>
            <div class="content">
                <p>Olá, [Nome do Cliente]!</p>
                <p>Estamos muito felizes em compartilhar com você as últimas novidades e ofertas exclusivas.</p>
                <img src="https://via.placeholder.com/600x200" alt="Oferta Exclusiva">
                <p>Clique no botão abaixo para aproveitar!</p>
                <a href="#" class="button">Aproveitar Oferta</a>
            </div>
            <div class="footer">
                <p>© 2023 Nome da Empresa. Todos os direitos reservados.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return template

def salvar_template_em_arquivo(template, nome_arquivo):
    """
    Salva o template HTML em um arquivo.
    
    Args:
        template (str): O template HTML a ser salvo.
        nome_arquivo (str): O nome do arquivo onde o template será salvo.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(template)

def main():
    """
    Função principal que gera e salva o template de e-mail.
    """
    template = gerar_template_email()
    nome_arquivo = 'template_email_marketing.html'
    salvar_template_em_arquivo(template, nome_arquivo)
    print(f'Template salvo como {nome_arquivo}')

if __name__ == '__main__':
    main()