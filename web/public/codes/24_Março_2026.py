"""
Script para gerar um convite formatado para uma festa de aniversário.
O script solicita ao usuário os dados necessários e salva em um arquivo de texto.
"""

def obter_dados_usuario():
    """
    Solicita ao usuário os dados necessários para o convite.
    
    Returns:
        dict: Um dicionário contendo os dados do convite.
    """
    dados = {}
    dados['nome_aniversariante'] = input("Digite o nome do aniversariante: ")
    dados['data_aniversario'] = input("Digite a data do aniversário (dd/mm/yyyy): ")
    dados['hora'] = input("Digite a hora do evento (hh:mm): ")
    dados['local'] = input("Digite o local do evento: ")
    dados['convidados'] = input("Digite os nomes dos convidados separados por vírgula: ").split(',')
    
    return dados

def formatar_convite(dados):
    """
    Formata os dados do convite em um texto formatado.
    
    Args:
        dados (dict): Dicionário contendo os dados do convite.
    
    Returns:
        str: O convite formatado.
    """
    convidados_formatados = ', '.join(dados['convidados']).strip()
    convite = (
        f"Convite para o Aniversário de {dados['nome_aniversariante']}\n\n"
        f"Data: {dados['data_aniversario']}\n"
        f"Hora: {dados['hora']}\n"
        f"Local: {dados['local']}\n\n"
        f"Convidados: {convidados_formatados}\n"
    )
    return convite

def salvar_convite(convite, nome_arquivo='convite.txt'):
    """
    Salva o convite formatado em um arquivo de texto.
    
    Args:
        convite (str): O convite formatado.
        nome_arquivo (str): Nome do arquivo onde o convite será salvo.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(convite)
    print(f"Convite salvo com sucesso em {nome_arquivo}")

def main():
    """
    Função principal que executa o script.
    """
    dados = obter_dados_usuario()
    convite_formatado = formatar_convite(dados)
    salvar_convite(convite_formatado)

if __name__ == '__main__':
    main()