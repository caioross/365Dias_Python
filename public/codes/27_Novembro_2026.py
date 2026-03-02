"""
gerador_grafico_velas_stocks.py

Este script é responsável por gerar um gráfico de Candlestick para análise técnica de ações.
Utiliza a biblioteca matplotlib para plotar o gráfico e pandas_datareader para obter os dados de ações.
"""

import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

def fetch_stock_data(stock_symbol, start_date, end_date):
    """
    Fetches stock data for a given symbol within a specified date range.

    Args:
        stock_symbol (str): The stock symbol (e.g., 'AAPL' for Apple Inc.).
        start_date (datetime): The start date for the data retrieval.
        end_date (datetime): The end date for the data retrieval.

    Returns:
        DataFrame: A pandas DataFrame containing the stock data.
    """
    return web.DataReader(stock_symbol, 'yahoo', start_date, end_date)

def plot_candlestick_chart(stock_data):
    """
    Plots a candlestick chart for the given stock data.

    Args:
        stock_data (DataFrame): The stock data to plot.
    """
    fig, ax = plt.subplots()
    ax.plot(stock_data.index, stock_data['Close'], label='Close Price')
    ax.fill_between(stock_data.index, stock_data['Low'], stock_data['High'], color='gray', alpha=0.5)
    ax.legend()
    plt.title('Candlestick Chart for Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to execute the script.
    Fetches stock data and plots the candlestick chart.
    """
    stock_symbol = 'AAPL'  # Example stock symbol
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)

    stock_data = fetch_stock_data(stock_symbol, start_date, end_date)
    plot_candlestick_chart(stock_data)

if __name__ == '__main__':
    main()