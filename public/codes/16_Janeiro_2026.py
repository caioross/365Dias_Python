import random

def gerar_nick():
    """
    Gera um nome de usuário aleatório combinando um adjetivo e um substantivo.

    Returns:
        str: Um nome de usuário composto por um adjetivo e um substantivo.
    """
    adjetivos = [
        "Rápido", "Feroz", "Sábio", "Brilhante", "Destemido", "Valente",
        "Astuto", "Elegante", "Feroz", "Inovador", "Liberdade", "Misterioso",
        "Nobre", "Ouro", "Poderoso", "Quente", "Risada", "Sábio", "Trovão",
        "Vencedor", "Xenon", "Yoga", "Zumbido"
    ]
    
    substantivos = [
        "Dragão", "Falcão", "Grym", "Hulk", "Inferno", "Jaguar", "Kraken",
        "Leão", "Manticora", "Nebulosa", "Onyx", "Pégaso", "Quimera", "Raven",
        "Sátiro", "Tigre", "Urso", "Vampiro", "Wisp", "Xenon", "Yak", "Zorro"
    ]
    
    adjetivo = random.choice(adjetivos)
    substantivo = random.choice(substantivos)
    
    return f"{adjetivo}{substantivo}"

def main():
    """
    Função principal que gera e imprime um nome de usuário aleatório.
    """
    nick = gerar_nick()
    print(f"Seu novo nick de jogo é: {nick}")

if __name__ == '__main__':
    main()