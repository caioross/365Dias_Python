import random

def gerar_poema(versos, rimas):
    """
    Gera um poema combinando versos e rimas pré-definidas.

    Args:
        versos (list): Uma lista de versos que podem ser usados no poema.
        rimas (list): Uma lista de rimas que podem ser usadas no poema.

    Returns:
        str: Um poema gerado aleatoriamente.
    """
    poema = []
    for _ in range(4):  # Gera um poema com 4 versos
        verso = random.choice(versos)
        rima = random.choice(rimas)
        poema.append(f"{verso} {rima}")
    return "\n".join(poema)

def main():
    """
    Função principal que define os versos e rimas e chama a função para gerar um poema.
    """
    versos = [
        "O sol se põe no céu azul",
        "As flores dançam no vento",
        "As estrelas brilham na noite",
        "O mar suspira com a maré"
    ]
    
    rimas = [
        "e o dia se vai",
        "em cores de luz",
        "iluminando o caminho",
        "e trazendo paz"
    ]
    
    poema_gerado = gerar_poema(versos, rimas)
    print(poema_gerado)

if __name__ == '__main__':
    main()