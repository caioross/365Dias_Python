
def adicionar(x, y):
    """
    Esta função retorna a soma de x e y.
    :param x: primeiro número
    :param y: segundo número
    :return: soma de x e y
    """
    return x + y

def subtrair(x, y):
    """
    Esta função retorna a subtração de x por y.
    :param x: primeiro número
    :param y: segundo número
    :return: subtração de x por y
    """
    return x - y

def multiplicar(x, y):
    """
    Esta função retorna a multiplicação de x por y.
    :param x: primeiro número
    :param y: segundo número
    :return: multiplicação de x por y
    """
    return x * y

def dividir(x, y):
    """
    Esta função retorna a divisão de x por y.
    :param x: primeiro número
    :param y: segundo número
    :return: divisão de x por y
    :raises ValueError: se y for igual a zero
    """
    if y == 0:
        # Se o segundo número for zero, levanta um erro para evitar divisão por zero
        raise ValueError("Divisão por zero não é permitida.")
    return x / y

def menu():
    """
    Esta função exibe o menu de opções para o usuário.
    """
    print("Selecione a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def main():
    """
    Função principal que executa o loop da calculadora.
    """
    while True:
        # Exibe o menu para o usuário
        menu()
        # Recebe a escolha do usuário como input
        escolha = input("Digite sua escolha (1/2/3/4): ")

        # Verifica se a escolha é válida (1, 2, 3 ou 4)
        if escolha in ['1', '2', '3', '4']:
            try:
                # Solicita ao usuário que insira dois números
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                # Se o usuário não inserir números válidos, exibe uma mensagem de erro
                print("Entrada inválida! Por favor, insira números válidos.")
                continue

            # Realiza a operação correspondente à escolha do usuário
            if escolha == '1':
                # Chama a função adicionar se a escolha for '1'
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                # Chama a função subtrair se a escolha for '2'
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                # Chama a função multiplicar se a escolha for '3'
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                try:
                    # Chama a função dividir se a escolha for '4'
                    print(f"{num1} / {num2} = {dividir(num1, num2)}")
                except ValueError as e:
                    # Trata o erro de divisão por zero e exibe uma mensagem de erro
                    print(e)
        else:
            # Se a escolha não for válida, exibe uma mensagem de erro
            print("Escolha inválida! Por favor, selecione uma opção válida.")

        # Pergunta ao usuário se deseja realizar outra operação
        proxima_operacao = input("Deseja realizar outra operação? (s/n): ")
        if proxima_operacao.lower() != 's':
            # Se a resposta for 'n', sai do loop e termina o programa
            break

if __name__ == "__main__":
    # Verifica se o script está sendo executado diretamente
    main()