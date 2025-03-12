def celsius_para_fahrenheit(celsius):
    """
    Função para converter temperatura de Celsius para Fahrenheit.
    :param celsius: Temperatura em graus Celsius
    :return: Temperatura convertida para Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """
    Função para converter temperatura de Fahrenheit para Celsius.
    :param fahrenheit: Temperatura em graus Fahrenheit
    :return: Temperatura convertida para Celsius
    """
    return (fahrenheit - 32) * 5/9

def menu():
    """
    Função para exibir o menu de opções de conversão de temperatura.
    """
    print("Escolha a conversão desejada:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Sair")

def main():
    """
    Função principal que executa o conversor de temperatura.
    """
    while True:
        menu()
        
        # Solicita a escolha do usuário
        escolha = input("Digite sua escolha (1/2/3): ")

        if escolha == '1' or escolha == '2':
            try:
                # Solicita a temperatura a ser convertida
                temperatura = float(input("Digite a temperatura: "))
                
                if escolha == '1':
                    # Converte de Celsius para Fahrenheit
                    resultado = celsius_para_fahrenheit(temperatura)
                    print(f"{temperatura}°C é igual a {resultado:.2f}°F.")
                
                elif escolha == '2':
                    # Converte de Fahrenheit para Celsius
                    resultado = fahrenheit_para_celsius(temperatura)
                    print(f"{temperatura}°F é igual a {resultado:.2f}°C.")
            
            except ValueError:
                # Se o valor inserido não for válido, exibe uma mensagem de erro
                print("Por favor, insira um número válido para a temperatura.")
        
        elif escolha == '3':
            print("Obrigado por usar o conversor de temperatura! Até logo!")
            break
        
        else:
            print("Opção inválida! Por favor, selecione uma opção válida.")
        
        # Pergunta se o usuário deseja realizar outra conversão
        continuar = input("Deseja realizar outra conversão? (s/n): ")
        if continuar.lower() != 's':
            print("Obrigado por usar o conversor de temperatura! Até logo!")
            break

if __name__ == "__main__":
    main()
