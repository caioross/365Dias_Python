import time
import pyautogui

def simulate_clicks(clicks):
    """
    Simula cliques de mouse em coordenadas específicas da tela.

    Args:
        clicks (list of tuples): Uma lista de tuplas, onde cada tupla contém
            as coordenadas (x, y) e o intervalo de tempo (em segundos) entre
            os cliques.
    """
    for x, y, interval in clicks:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)

def main():
    """
    Função principal que define as coordenadas e intervalos de tempo
    para os cliques e chama a função de simulação.
    """
    # Exemplo de lista de cliques: [(x1, y1, intervalo1), (x2, y2, intervalo2), ...]
    clicks = [
        (100, 200, 1),  # Move para (100, 200) e clica, espera 1 segundo
        (300, 400, 2),  # Move para (300, 400) e clica, espera 2 segundos
        (500, 600, 1)   # Move para (500, 600) e clica, espera 1 segundo
    ]
    
    simulate_clicks(clicks)

if __name__ == '__main__':
    main()