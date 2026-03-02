import random

def monty_hall_game(switch_doors):
    """
    Simula uma única rodada do jogo Monty Hall.

    :param switch_doors: Booleano indicando se o jogador quer trocar de porta.
    :return: Booleano indicando se o jogador ganhou.
    """
    doors = [0, 0, 1]  # Uma porta tem um carro (1) e duas têm cabras (0)
    random.shuffle(doors)  # Embaralha as portas

    # O jogador escolhe uma porta aleatoriamente
    player_choice = random.randint(0, 2)

    # O apresentador revela uma porta com cabra que não foi escolhida pelo jogador
    revealed_door = [i for i in range(3) if i != player_choice and doors[i] == 0][0]

    # Se o jogador optar por trocar, escolhe a outra porta que não foi revelada
    if switch_doors:
        player_choice = [i for i in range(3) if i != player_choice and i != revealed_door][0]

    # Retorna True se o jogador escolheu a porta com o carro
    return doors[player_choice] == 1

def simulate_monty_hall(trials, switch_doors):
    """
    Realiza uma série de simulações do jogo Monty Hall.

    :param trials: Número de rodadas a serem simuladas.
    :param switch_doors: Booleano indicando se o jogador deve sempre trocar de porta.
    :return: Taxa de vitória.
    """
    wins = 0
    for _ in range(trials):
        if monty_hall_game(switch_doors):
            wins += 1
    return wins / trials

def main():
    """
    Função principal que executa o simulador do jogo Monty Hall.
    """
    trials = 10000  # Número de rodadas para simulação
    switch_doors = True  # Decide se o jogador deve trocar de porta

    win_rate = simulate_monty_hall(trials, switch_doors)
    print(f"Taxa de vitória ao {'trocar' if switch_doors else 'não trocar'} de porta: {win_rate:.2%}")

if __name__ == '__main__':
    main()