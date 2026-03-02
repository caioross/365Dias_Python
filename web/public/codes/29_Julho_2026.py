"""
Simulador de Urna Eletrônica V2

Este script simula uma urna eletrônica onde os eleitores podem votar em candidatos.
Cada candidato possui um número e um nome. O script exibe uma foto do candidato
e registra os votos. No final, gera um relatório com a porcentagem de votos de cada candidato.
"""

import os

# Dados dos candidatos
candidatos = {
    1: {"nome": "João Silva", "foto": "joao_silva.jpg"},
    2: {"nome": "Maria Santos", "foto": "maria_santos.jpg"},
    3: {"nome": "Carlos Pereira", "foto": "carlos_pereira.jpg"},
}

# Função para exibir a foto do candidato (simulação)
def exibir_foto(candidato):
    foto = candidato.get("foto", "default.jpg")
    print(f"Exibindo foto do candidato: {foto}")

# Função para votar
def votar():
    print("Lista de candidatos:")
    for numero, candidato in candidatos.items():
        print(f"{numero} - {candidato['nome']}")
    
    voto = int(input("Digite o número do candidato para votar: "))
    if voto in candidatos:
        candidato = candidatos[voto]
        exibir_foto(candidato)
        print(f"Voto computado para {candidato['nome']}")
        return voto
    else:
        print("Número inválido. Voto não computado.")
        return None

# Função para gerar relatório
def gerar_relatorio(votos):
    total_votos = len(votos)
    print("\nRelatório de Votos:")
    for numero, candidato in candidatos.items():
        votos_candidato = votos.count(numero)
        porcentagem = (votos_candidato / total_votos) * 100 if total_votos > 0 else 0
        print(f"{candidato['nome']}: {votos_candidato} votos ({porcentagem:.2f}%)")

# Função principal
def main():
    votos = []
    while True:
        voto = votar()
        if voto is not None:
            votos.append(voto)
        continuar = input("Deseja continuar votando? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    gerar_relatorio(votos)

# Bloco principal
if __name__ == '__main__':
    main()