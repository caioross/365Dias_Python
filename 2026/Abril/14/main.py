from datetime import datetime

def is_valid_date(day: int, month: int, year: int) -> bool:
    """
    Valida se a data fornecida existe no calendário, considerando anos bissextos.

    Args:
        day (int): O dia da data.
        month (int): O mês da data.
        year (int): O ano da data.

    Returns:
        bool: True se a data é válida, False caso contrário.
    """
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def main():
    """
    Função principal que solicita ao usuário uma data e verifica se ela é válida.
    """
    try:
        day = int(input("Digite o dia: "))
        month = int(input("Digite o mês: "))
        year = int(input("Digite o ano: "))

        if is_valid_date(day, month, year):
            print("A data é válida.")
        else:
            print("A data é inválida.")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para dia, mês e ano.")

if __name__ == '__main__':
    main()