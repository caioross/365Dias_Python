import random
import time
from datetime import datetime

def generate_sensor_data():
    """
    Gera dados simulados de temperatura e umidade para um sensor IoT.

    Returns:
        dict: Um dicionário contendo a temperatura e a umidade.
    """
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(30.0, 70.0), 2)
    timestamp = datetime.now().isoformat()
    
    return {
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity
    }

def main():
    """
    Função principal que simula o fluxo de dados de um sensor IoT.
    """
    try:
        while True:
            data = generate_sensor_data()
            print(data)
            time.sleep(2)  # Simula um intervalo de 2 segundos entre as medições
    except KeyboardInterrupt:
        print("\nSimulação interrompida pelo usuário.")

if __name__ == '__main__':
    main()