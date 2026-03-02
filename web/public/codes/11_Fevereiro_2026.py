class ContaBancaria:
    def __init__(self, titular, saldo=0):
        """
        Inicializa uma nova instância de ContaBancaria.

        :param titular: Nome do titular da conta.
        :param saldo: Saldo inicial da conta (padrão é 0).
        """
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """
        Deposita um valor na conta.

        :param valor: Valor a ser depositado.
        :return: None
        """
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """
        Realiza um saque na conta.

        :param valor: Valor a ser sacado.
        :return: None
        """
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")

    def consultar_saldo(self):
        """
        Consulta o saldo atual da conta.

        :return: None
        """
        print(f"Saldo atual: R${self.saldo:.2f}")


def main():
    """
    Função principal que executa o simulador de banco terminal.
    """
    print("Bem-vindo ao Simulador de Banco Terminal!")
    titular = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(titular)

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Consultar Saldo")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.consultar_saldo()
        elif opcao == '4':
            print("Saindo do simulador. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == '__main__':
    main()