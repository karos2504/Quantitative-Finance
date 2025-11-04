import numpy as np
import datetime
import yfinance as yf

class ValueAtRiskMonteCarlo:
    def __init__(self, stock, start_date, end_date, S, confidence_level, n, iterations):
        self.stock = stock
        self.start_date = start_date
        self.end_date = end_date
        self.S = S
        self.confidence_level = confidence_level
        self.n = n
        self.iterations = iterations
        self.stock_data = self.download_data()
        self.returns = self.calculate_returns()
        self.mu = self.returns.mean().item()
        self.sigma = self.returns.std().item()

    def download_data(self):
        data = yf.download(self.stock, start=self.start_date, end=self.end_date, auto_adjust=False)
        return data['Adj Close']

    def calculate_returns(self):
        returns = np.log(self.stock_data / self.stock_data.shift(1)).dropna()
        return returns

    def simulation(self):
        # Generate 1D array of random normal variables
        rand = np.random.normal(0, 1, self.iterations)
        # Calculate stock prices using the geometric Brownian motion formula
        stock_price = self.S * np.exp(self.n * (self.mu - 0.5 * self.sigma ** 2) + self.sigma * np.sqrt(self.n) * rand)
        # Sort the stock prices
        stock_price = np.sort(stock_price)
        # Calculate the VaR percentile
        percentile = np.percentile(stock_price, (1 - self.confidence_level) * 100)
        return self.S - percentile
    
    def display_results(self):
        var = self.simulation()
        print(f"Mean Daily Return (mu): {self.mu:.4f}")
        print(f"Daily Volatility (sigma): {self.sigma:.4f}")
        print(f"Value at Risk (VaR) with Monte-Carlo simulation for {self.stock} over {self.n} day(s) at {int(self.confidence_level*100)}% confidence: ${var:,.2f}")

if __name__ == "__main__":
    stock = 'C'  # Citigroup stock
    S = 1e6  # Investment amount
    c = 0.99  # Confidence level: 99%
    n = 1  # 1 day
    iterations = 100000  # Number of paths in the Monte-Carlo simulation

    # Historical data to approximate mean and standard deviation
    start_date = datetime.datetime(2015, 1, 1)
    end_date = datetime.datetime(2025, 1, 1)

    # Create and run the model
    model = ValueAtRiskMonteCarlo(stock, start_date, end_date, S, c, n, iterations)
    model.display_results()
