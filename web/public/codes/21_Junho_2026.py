import random

def sorteio_amigo_secreto(participantes):
    """
    Realiza o sorteio de amigo secreto garantindo que ninguém tire a si mesmo.

    Args:
        participantes (list): Lista de nomes dos participantes.

    Returns:
        dict: Um dicionário onde as chaves são os participantes e os valores são seus respectivos amigos secretos.
    """
    if len(participantes) < 2:
        raise ValueError("Deve haver pelo menos dois participantes para realizar o sorteio.")

    random.shuffle(participantes)
    sorteio = {}
    n = len(participantes)

    for i in range(n):
        sorteio[participantes[i]] = participantes[(i + 1) % n]

    return sorteio

def main():
    participantes = input("Digite os nomes dos participantes separados por vírgula: ").split(',')
    participantes = [nome.strip() for nome in participantes]

    try:
        resultado_sorteio = sorteio_amigo_secreto(participantes)
        for participante, amigo_secreto in resultado_sorteio.items():
            print(f"{participante} é o amigo secreto de {amigo_secreto}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()