import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm

class StockData:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def download_data(self):
        self.data = yf.download(tickers=self.ticker, start=self.start_date, end=self.end_date, auto_adjust=False)['Adj Close']
    
    def calculate_returns(self):
        self.data['Returns'] = np.log(self.data / self.data.shift(1))
        return self.data['Returns'].dropna()
    
    def show_data(self):
        returns = self.calculate_returns()
        print(self.data)
        
        # Calculate statistics for returns
        mean = returns.mean()
        std = returns.std()
        
        # Plot histogram with density and normal distribution overlay
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(returns, bins=50, density=True, alpha=0.6, color='b', label='Returns Histogram')
        
        # Normal distribution curve (overlay)
        x = np.linspace(mean - 5 * std, mean + 5 * std, 100)
        ax.plot(x, norm.pdf(x, mean, std), 'r-', lw=2, label='Normal Distribution')
        
        # Adding labels and title
        ax.set_xlabel('Returns')
        ax.set_ylabel('Density')
        ax.set_title(f'Returns Distribution for {self.ticker} ({self.start_date} to {self.end_date})')
        ax.legend()
        plt.show()

if __name__ == '__main__':
    stock_data = StockData('AAPL', '2010-01-01', '2025-01-01')
    stock_data.download_data()
    stock_data.show_data()