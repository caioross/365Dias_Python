import random

def gerar_nome_equipe():
    """
    Gera um nome de equipe combinando uma cor e um animal aleatoriamente.

    Returns:
        str: Um nome de equipe no formato 'CorAnimal'.
    """
    cores = ['Vermelho', 'Azul', 'Verde', 'Amarelo', 'Roxo', 'Laranja', 'Preto', 'Branco', 'Cinza', 'Dourado']
    animais = ['Leão', 'Tigre', 'Elefante', 'Girafa', 'Panda', 'Tubarão', 'Águia', 'Pinguim', 'Urso', 'Cachorro']

    cor = random.choice(cores)
    animal = random.choice(animais)

    return f'{cor}{animal}'

def main():
    """
    Função principal que gera e imprime um nome de equipe.
    """
    nome_equipe = gerar_nome_equipe()
    print(f'Nome da equipe: {nome_equipe}')

if __name__ == '__main__':
    main()