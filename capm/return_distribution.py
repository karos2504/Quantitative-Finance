"""
Normal distribution analysis of stock returns.

Downloads stock data, computes log returns, and overlays a
normal distribution curve on the returns histogram.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from utils.data import download_stock_data, calculate_log_returns


class ReturnDistribution:
    """Analyse and visualise the normal distribution of stock returns."""

    def __init__(self, ticker: str, start: str, end: str):
        self.ticker = ticker
        self.start = start
        self.end = end
        self.returns = None

    def initialize(self):
        """Download prices and compute log returns."""
        prices = download_stock_data(self.ticker, self.start, self.end)
        self.returns = calculate_log_returns(prices).iloc[:, 0]

    def plot(self):
        """Histogram of returns with a normal distribution overlay."""
        mu, sigma = self.returns.mean(), self.returns.std()

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(self.returns, bins=50, density=True, alpha=0.6, color='steelblue',
                label='Returns Histogram')

        x = np.linspace(mu - 5 * sigma, mu + 5 * sigma, 200)
        ax.plot(x, norm.pdf(x, mu, sigma), 'r-', lw=2, label='Normal Distribution')

        ax.set_xlabel('Returns')
        ax.set_ylabel('Density')
        ax.set_title(f'Returns Distribution — {self.ticker} ({self.start} to {self.end})')
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    model = ReturnDistribution('AAPL', '2010-01-01', '2026-01-01')
    model.initialize()
    model.plot()
