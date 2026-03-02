import datetime
import pytz

def get_current_time_in_cities():
    """
    Retorna a hora atual em cinco cidades diferentes do mundo.
    
    Returns:
        dict: Um dicionário com nomes das cidades como chaves e as horas atuais como valores.
    """
    cities = {
        'New_York': 'America/New_York',
        'London': 'Europe/London',
        'Tokyo': 'Asia/Tokyo',
        'Sydney': 'Australia/Sydney',
        'Mumbai': 'Asia/Kolkata'
    }
    
    current_times = {}
    for city, timezone_str in cities.items():
        timezone = pytz.timezone(timezone_str)
        current_time = datetime.datetime.now(timezone)
        current_times[city] = current_time.strftime('%Y-%m-%d %H:%M:%S')
    
    return current_times

def main():
    """
    Função principal que obtém e imprime a hora atual em cinco cidades diferentes.
    """
    current_times = get_current_time_in_cities()
    for city, time in current_times.items():
        print(f"A hora atual em {city} é: {time}")

if __name__ == '__main__':
    main()