"""
Script para gerar uma representação visual de um mapa mental a partir de uma lista de ideias.
As ideias são organizadas em uma estrutura hierárquica usando recuos e linhas.
"""

def gerar_mapa_mental(ideias):
    """
    Gera uma representação visual de um mapa mental.

    :param ideias: Lista de tuplas onde cada tupla contém a profundidade e o texto da ideia.
    :return: String contendo o mapa mental formatado.
    """
    mapa = []
    for profundidade, texto in ideias:
        recuo = '  ' * profundidade
        mapa.append(f"{recuo}- {texto}")
    return '\n'.join(mapa)

def main():
    """
    Função principal que define as ideias e chama a função para gerar o mapa mental.
    """
    ideias = [
        (0, "Projeto de Software"),
        (1, "Análise Requisitos"),
        (2, "Entrevistas com Stakeholders"),
        (2, "Documentação de Requisitos"),
        (1, "Design"),
        (2, "Arquitetura"),
        (2, "Interface do Usuário"),
        (1, "Desenvolvimento"),
        (2, "Backend"),
        (2, "Frontend"),
        (1, "Testes"),
        (2, "Testes Unitários"),
        (2, "Testes de Integração"),
        (0, "Lançamento"),
    ]

    mapa_gerado = gerar_mapa_mental(ideias)
    print(mapa_gerado)

if __name__ == '__main__':
    main()