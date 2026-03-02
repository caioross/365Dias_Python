import time
import msvcrt  # Usado para detectar a pressão de uma tecla no Windows

def iniciar_cronometro():
    """
    Inicia um cronômetro no terminal que conta o tempo até que o usuário pressione uma tecla para parar.
    """
    print("Cronômetro iniciado. Pressione qualquer tecla para parar.")
    start_time = time.time()
    
    while True:
        if msvcrt.kbhit():  # Verifica se uma tecla foi pressionada
            break
        elapsed_time = time.time() - start_time
        print(f"Tempo decorrido: {elapsed_time:.2f} segundos", end='\r')
        time.sleep(0.1)  # Atualiza a cada 0.1 segundos

    print("\nCronômetro parado.")

def main():
    iniciar_cronometro()

if __name__ == '__main__':
    main()