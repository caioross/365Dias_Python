"""
Gerador de Lista de Afazeres CLI

Este script permite que o usuário crie, visualize, edite e exclua tarefas de uma lista de afazeres.
O script roda totalmente no terminal e utiliza uma interface de linha de comando (CLI) para interagir com o usuário.
"""

import json
import os

# Caminho para o arquivo onde as tarefas serão armazenadas
TAREFAS_ARQUIVO = 'tarefas.json'

def carregar_tarefas():
    """
    Carrega as tarefas do arquivo JSON.
    Retorna uma lista de tarefas ou uma lista vazia se o arquivo não existir.
    """
    if os.path.exists(TAREFAS_ARQUIVO):
        with open(TAREFAS_ARQUIVO, 'r') as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas(tarefas):
    """
    Salva a lista de tarefas no arquivo JSON.
    """
    with open(TAREFAS_ARQUIVO, 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def listar_tarefas(tarefas):
    """
    Lista todas as tarefas com seus respectivos índices.
    """
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for index, tarefa in enumerate(tarefas):
        print(f"{index}: {tarefa}")

def adicionar_tarefa(tarefas):
    """
    Adiciona uma nova tarefa à lista.
    """
    tarefa = input("Digite a nova tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada com sucesso.")
    else:
        print("Tarefa não pode ser vazia.")

def editar_tarefa(tarefas):
    """
    Edita uma tarefa existente na lista.
    """
    listar_tarefas(tarefas)
    try:
        index = int(input("Digite o índice da tarefa que deseja editar: "))
        if 0 <= index < len(tarefas):
            nova_tarefa = input("Digite a nova tarefa: ").strip()
            if nova_tarefa:
                tarefas[index] = nova_tarefa
                salvar_tarefas(tarefas)
                print("Tarefa editada com sucesso.")
            else:
                print("Tarefa não pode ser vazia.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def excluir_tarefa(tarefas):
    """
    Exclui uma tarefa da lista.
    """
    listar_tarefas(tarefas)
    try:
        index = int(input("Digite o índice da tarefa que deseja excluir: "))
        if 0 <= index < len(tarefas):
            tarefas.pop(index)
            salvar_tarefas(tarefas)
            print("Tarefa excluída com sucesso.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    """
    Função principal que controla o fluxo do programa.
    """
    tarefas = carregar_tarefas()
    while True:
        print("\nMenu:")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Editar tarefa")
        print("4. Excluir tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            listar_tarefas(tarefas)
        elif opcao == '2':
            adicionar_tarefa(tarefas)
        elif opcao == '3':
            editar_tarefa(tarefas)
        elif opcao == '4':
            excluir_tarefa(tarefas)
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    main()