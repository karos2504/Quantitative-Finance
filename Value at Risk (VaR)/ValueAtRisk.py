import numpy as np
import datetime
import yfinance as yf
from scipy.stats import norm

class VaRCalculator:
    def __init__(self, stock, start_date, end_date, confidence_level, position):
        self.stock = stock
        self.start_date = start_date
        self.end_date = end_date
        self.confidence_level = confidence_level
        self.position = position
        self.stock_data = self.download_data()
        self.returns = self.calculate_returns()
        self.mu = self.returns.mean()
        self.sigma = self.returns.std()

    def download_data(self):
        data = yf.download(self.stock, start=self.start_date, end=self.end_date, auto_adjust=False)
        return data['Adj Close']

    def calculate_returns(self):
        returns = np.log(self.stock_data / self.stock_data.shift(1)).dropna()
        return returns

    def calculate_var_n(self, n):
        z_score = norm.ppf(1 - self.confidence_level)
        var = self.position * (self.mu * n - self.sigma * np.sqrt(n) * z_score)
        return var

    def display_results(self, n):
        print(f"Mean Daily Return (mu): {self.mu.iloc[0]:.4f}")
        print(f"Daily Volatility (sigma): {self.sigma.iloc[0]:.4f}")
        print(f"Value at Risk (VaR) for {self.stock} over {n} day(s) at {int(self.confidence_level*100)}% confidence: ${self.calculate_var_n(n).iloc[0]:,.2f}")

if __name__ == '__main__':
    stock = 'AAPL'
    start_date = datetime.datetime(2015, 1, 1)
    end_date = datetime.datetime(2025, 1, 1)
    confidence_level = 0.99
    position = 1e6  # $1 million
    n = 1  # VaR tomorrow

    var_calculator = VaRCalculator(stock, start_date, end_date, confidence_level, position)
    var_calculator.display_results(n)
