"""
Script para simular uma urna eletrônica onde os usuários podem votar em candidatos.
O script permite que os usuários votem e exibe o resultado final após a votação.
"""

def votar(candidatos, voto):
    """
    Registra um voto para um candidato específico.

    Args:
        candidatos (dict): Um dicionário com nomes de candidatos como chaves e contagem de votos como valores.
        voto (str): O nome do candidato para quem o usuário está votando.
    """
    if voto in candidatos:
        candidatos[voto] += 1
    else:
        print("Candidato não encontrado. Voto não contabilizado.")

def exibir_resultados(candidatos):
    """
    Exibe os resultados da votação.

    Args:
        candidatos (dict): Um dicionário com nomes de candidatos como chaves e contagem de votos como valores.
    """
    print("Resultados da Eleição:")
    for candidato, votos in candidatos.items():
        print(f"{candidato}: {votos} votos")

def main():
    """
    Função principal que controla o fluxo da simulação da urna eletrônica.
    """
    candidatos = {
        "João": 0,
        "Maria": 0,
        "Carlos": 0
    }

    print("Bem-vindo à Urna Eletrônica!")
    print("Candidatos disponíveis: João, Maria, Carlos")
    print("Digite 'fim' para encerrar a votação e ver os resultados.")

    while True:
        voto = input("Digite o nome do candidato para quem deseja votar: ").strip()
        if voto.lower() == 'fim':
            break
        votar(candidatos, voto)

    exibir_resultados(candidatos)

if __name__ == '__main__':
    main()