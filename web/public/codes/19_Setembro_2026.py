"""
gerador_diagrama_fluxo_txt.py

Este script permite criar fluxogramas simples usando setas e caixas feitas de caracteres ASCII.
"""

def criar_caixa(texto):
    """
    Cria uma caixa de texto usando caracteres ASCII.

    :param texto: O texto a ser exibido dentro da caixa.
    :return: Uma string representando a caixa.
    """
    borda_superior = '+' + '-' * (len(texto) + 2) + '+'
    linha_meio = f'| {texto} |'
    borda_inferior = borda_superior
    return f'{borda_superior}\n{linha_meio}\n{borda_inferior}\n'

def criar_conexao():
    """
    Cria uma linha de conexão usando caracteres ASCII.

    :return: Uma string representando a linha de conexão.
    """
    return '   |\n'

def criar_seta():
    """
    Cria uma seta usando caracteres ASCII.

    :return: Uma string representando a seta.
    """
    return '   v\n'

def main():
    """
    Função principal que gera um fluxograma simples.
    """
    etapas = [
        "Início",
        "Processamento 1",
        "Decisão",
        "Processamento 2",
        "Fim"
    ]

    diagrama = ""
    for i, etapa in enumerate(etapas):
        diagrama += criar_caixa(etapa)
        if i < len(etapas) - 1:
            if etapa == "Decisão":
                diagrama += criar_seta()
                diagrama += criar_caixa("Sim")
                diagrama += criar_conexao()
                diagrama += criar_caixa("Não")
                diagrama += criar_seta()
            else:
                diagrama += criar_conexao()

    print(diagrama)

if __name__ == '__main__':
    main()