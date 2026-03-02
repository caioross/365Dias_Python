"""
Gerador de Cartão de Visitas em Formato de ASCII Art

Este script formata informações de contato em uma moldura artística de caracteres ASCII.
"""

def gerar_cartao_visitas(nome, cargo, empresa, telefone, email):
    """
    Gera um cartão de visitas em formato de ASCII art.

    :param nome: Nome do contato
    :param cargo: Cargo do contato
    :param empresa: Empresa do contato
    :param telefone: Telefone do contato
    :param email: Email do contato
    :return: Uma string contendo o cartão de visitas formatado
    """
    # Define a largura do cartão
    largura = 40
    # Cria a moldura superior
    cartao = '+' + '-' * (largura - 2) + '+\n'
    # Adiciona as informações formatadas
    cartao += f'|{nome.center(largura - 2)}|\n'
    cartao += f'|{cargo.center(largura - 2)}|\n'
    cartao += f'|{empresa.center(largura - 2)}|\n'
    cartao += f'|{telefone.center(largura - 2)}|\n'
    cartao += f'|{email.center(largura - 2)}|\n'
    # Cria a moldura inferior
    cartao += '+' + '-' * (largura - 2) + '+\n'
    return cartao

def main():
    """
    Função principal que gera e imprime o cartão de visitas.
    """
    # Informações de contato
    nome = "João da Silva"
    cargo = "Engenheiro de Software"
    empresa = "Tech Innovations"
    telefone = "(11) 98765-4321"
    email = "joao.silva@techinnovations.com"

    # Gera o cartão de visitas
    cartao_visitas = gerar_cartao_visitas(nome, cargo, empresa, telefone, email)

    # Imprime o cartão de visitas
    print(cartao_visitas)

if __name__ == '__main__':
    main()