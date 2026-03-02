import requests

def get_exchange_rates():
    """
    Fetches the latest exchange rates for Real (BRL), Dollar (USD), and Euro (EUR).
    
    Returns:
        dict: A dictionary containing the exchange rates with 'BRL', 'USD', and 'EUR' as keys.
    """
    url = "https://api.exchangeratesapi.io/latest?base=USD&symbols=BRL,EUR"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    rates = data.get('rates', {})
    rates['USD'] = 1.0  # Base currency is USD
    return rates

def convert_currency(amount, from_currency, to_currency, rates):
    """
    Converts an amount from one currency to another using the provided exchange rates.
    
    Args:
        amount (float): The amount of currency to convert.
        from_currency (str): The currency code to convert from.
        to_currency (str): The currency code to convert to.
        rates (dict): A dictionary containing the exchange rates.
    
    Returns:
        float: The converted amount.
    """
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency code provided.")
    
    converted_amount = amount * (rates[to_currency] / rates[from_currency])
    return converted_amount

def main():
    """
    Main function to handle user input and perform currency conversion.
    """
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency code to convert from (BRL, USD, EUR): ").upper()
        to_currency = input("Enter the currency code to convert to (BRL, USD, EUR): ").upper()
        
        rates = get_exchange_rates()
        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()