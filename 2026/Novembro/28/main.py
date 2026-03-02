import random

def gerar_clima():
    """
    Gera uma descrição de clima aleatória para uso em RPGs de mesa.
    
    Returns:
        str: Uma descrição de clima.
    """
    climas = [
        "ensolarado",
        "nuvem coberta",
        "chuva torrencial",
        "vento forte",
        "neblina densa",
        "tempestade elétrica",
        "sol poente",
        "lua cheia",
        "inverno rigoroso",
        "verão intenso"
    ]
    return random.choice(climas)

def gerar_visibilidade(clima):
    """
    Gera uma descrição de visibilidade baseada no clima.
    
    Args:
        clima (str): A descrição do clima.
        
    Returns:
        str: Uma descrição de visibilidade.
    """
    visibilidades = {
        "ensolarado": "Visibilidade excelente, tudo está claro.",
        "nuvem coberta": "Visibilidade ruim, as nuvens estão cobrindo a maior parte do céu.",
        "chuva torrencial": "Visibilidade muito baixa, a chuva está caindo em torrents.",
        "vento forte": "Visibilidade boa, mas o vento forte pode dificultar a visão.",
        "neblina densa": "Visibilidade extremamente baixa, a neblina está muito densa.",
        "tempestade elétrica": "Visibilidade muito baixa, a tempestade está em plena intensidade.",
        "sol poente": "Visibilidade excelente, o sol está se pondo, criando um lindo pôr do sol.",
        "lua cheia": "Visibilidade excelente, a lua cheia ilumina o céu.",
        "inverno rigoroso": "Visibilidade boa, mas o inverno rigoroso pode criar neve ou neblina.",
        "verão intenso": "Visibilidade excelente, o verão intenso pode criar reflexos no chão."
    }
    return visibilidades.get(clima, "Visibilidade normal.")

def main():
    """
    Função principal que gera e exibe a descrição do clima e visibilidade.
    """
    clima = gerar_clima()
    visibilidade = gerar_visibilidade(clima)
    print(f"Clima: {clima.capitalize()}")
    print(f"Visibilidade: {visibilidade}")

if __name__ == '__main__':
    main()