def converter_segundos(total_segundos):
    """
    Converte uma quantidade total de segundos em horas, minutos e segundos formatados.

    Args:
        total_segundos (int): O número total de segundos a serem convertidos.

    Returns:
        str: Uma string formatada com o tempo em horas, minutos e segundos.
    """
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return f"{horas:02}:{minutos:02}:{segundos:02}"

def main():
    """
    Função principal que solicita ao usuário uma quantidade de segundos e exibe o tempo convertido.
    """
    try:
        total_segundos = int(input("Digite a quantidade total de segundos: "))
        if total_segundos < 0:
            raise ValueError("O número de segundos não pode ser negativo.")
        tempo_formatado = converter_segundos(total_segundos)
        print(f"Tempo formatado: {tempo_formatado}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()