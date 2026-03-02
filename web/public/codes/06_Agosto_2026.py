import random
import time
import threading

# Constantes
ASSET_NAMES = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB']
MIN_PRICE = 50
MAX_PRICE = 1500
PRICE_CHANGE_STEP = 5
MAX_ASSETS = 10

# Estado global
assets = {name: random.randint(MIN_PRICE, MAX_PRICE) for name in ASSET_NAMES}
user_assets = {name: 0 for name in ASSET_NAMES}
stop_thread = False

def update_prices():
    global assets
    while not stop_thread:
        for asset in assets:
            change = random.choice([-PRICE_CHANGE_STEP, PRICE_CHANGE_STEP])
            new_price = max(MIN_PRICE, min(MAX_PRICE, assets[asset] + change))
            assets[asset] = new_price
        time.sleep(1)

def display_menu():
    print("\n=== Simulador de Mercado Financeiro ===")
    print("Ativos disponíveis:")
    for name, price in assets.items():
        print(f"{name}: ${price}")
    print("\nComandos:")
    print("1. Comprar ativo")
    print("2. Ver portfólio")
    print("3. Sair")

def buy_asset():
    asset_name = input("Digite o nome do ativo para comprar: ").strip().upper()
    if asset_name not in assets:
        print("Ativo inválido.")
        return
    try:
        quantity = int(input("Digite a quantidade para comprar: "))
        if quantity <= 0:
            print("Quantidade deve ser positiva.")
            return
        if user_assets[asset_name] + quantity > MAX_ASSETS:
            print(f"Limite máximo de {MAX_ASSETS} ativos por tipo excedido.")
            return
        user_assets[asset_name] += quantity
        print(f"Comprado {quantity} unidades de {asset_name}.")
    except ValueError:
        print("Quantidade inválida.")

def show_portfolio():
    print("\n=== Seu Portfólio ===")
    for name, quantity in user_assets.items():
        if quantity > 0:
            print(f"{name}: {quantity} unidades")

def main():
    global stop_thread
    price_thread = threading.Thread(target=update_prices)
    price_thread.start()

    while True:
        display_menu()
        choice = input("Escolha uma opção: ").strip()
        if choice == '1':
            buy_asset()
        elif choice == '2':
            show_portfolio()
        elif choice == '3':
            stop_thread = True
            price_thread.join()
            print("Saindo do simulador.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()