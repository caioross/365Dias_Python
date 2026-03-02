import json
import os

class Banco:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito de {valor}")
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque de {valor}")
            return True
        return False

    def exibir_saldo(self):
        return self.saldo

    def exibir_historico(self):
        return self.historico

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.conta = None

    def criar_conta(self, nome_conta, saldo_inicial=0):
        self.conta = Banco(nome_conta, saldo_inicial)

    def salvar_transacoes(self, arquivo):
        if self.conta:
            with open(arquivo, 'w') as file:
                json.dump(self.conta.historico, file)

    def carregar_transacoes(self, arquivo):
        if os.path.exists(arquivo):
            with open(arquivo, 'r') as file:
                self.conta.historico = json.load(file)

def main():
    usuarios = {}
    arquivo_usuarios = 'usuarios.json'

    if os.path.exists(arquivo_usuarios):
        with open(arquivo_usuarios, 'r') as file:
            usuarios = json.load(file)

    while True:
        print("\n1. Login\n2. Novo Usuário\n3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")

            if nome in usuarios and usuarios[nome]['senha'] == senha:
                usuario = Usuario(nome, senha)
                usuario.conta = Banco(usuarios[nome]['conta']['nome'], usuarios[nome]['conta']['saldo'])
                usuario.carregar_transacoes(f"{nome}_historico.json")

                while True:
                    print("\n1. Depositar\n2. Sacar\n3. Exibir Saldo\n4. Exibir Histórico\n5. Sair")
                    opcao_conta = input("Escolha uma opção: ")

                    if opcao_conta == '1':
                        valor = float(input("Digite o valor para depositar: "))
                        if usuario.conta.depositar(valor):
                            print("Depósito realizado com sucesso!")
                        else:
                            print("Valor inválido para depósito.")

                    elif opcao_conta == '2':
                        valor = float(input("Digite o valor para sacar: "))
                        if usuario.conta.sacar(valor):
                            print("Saque realizado com sucesso!")
                        else:
                            print("Saldo insuficiente ou valor inválido para saque.")

                    elif opcao_conta == '3':
                        print(f"Saldo atual: {usuario.conta.exibir_saldo()}")

                    elif opcao_conta == '4':
                        print("Histórico de transações:")
                        for transacao in usuario.conta.exibir_historico():
                            print(transacao)

                    elif opcao_conta == '5':
                        usuario.salvar_transacoes(f"{nome}_historico.json")
                        break

            else:
                print("Usuário ou senha incorretos.")

        elif opcao == '2':
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")

            if nome not in usuarios:
                usuarios[nome] = {'senha': senha, 'conta': {'nome': '', 'saldo': 0}}
                print("Usuário criado com sucesso!")
            else:
                print("Usuário já existe.")

        elif opcao == '3':
            with open(arquivo_usuarios, 'w') as file:
                json.dump(usuarios, file)
            break

if __name__ == '__main__':
    main()