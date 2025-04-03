import psutil
import time

def monitorar_cpu_memoria(intervalo=1):
    """
    Função para monitorar o uso de CPU e memória do sistema.
    
    :param intervalo: Tempo (em segundos) entre cada leitura de uso de CPU e memória.
    """
    print("Monitorando o uso de CPU e memória...\n")
    try:
        while True:
            # Obter o uso de CPU (em porcentagem)
            uso_cpu = psutil.cpu_percent(intervalo)

            # Obter o uso de memória (em porcentagem)
            uso_memoria = psutil.virtual_memory().percent

            # Exibir os resultados
            print(f"Uso de CPU: {uso_cpu}% | Uso de Memória: {uso_memoria}%")
            
            # Espera o próximo intervalo
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido.")

def main():
    """
    Função principal que inicia o monitoramento de CPU e memória.
    """
    intervalo = int(input("Digite o intervalo de monitoramento (em segundos): ") or 1)
    
    monitorar_cpu_memoria(intervalo)

if __name__ == "__main__":
    main()
