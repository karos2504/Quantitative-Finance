"""
Monte Carlo Value at Risk.

Simulates future stock prices via geometric Brownian motion to estimate
the VaR at a given confidence level.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np

from utils.data import download_stock_data, calculate_log_returns


class VaRMonteCarlo:
    """Compute VaR using Monte Carlo simulation."""

    def __init__(self, stock: str, start: str, end: str,
                 position: float = 1e6, confidence: float = 0.95,
                 n_days: int = 1, iterations: int = 100_000):
        self.stock = stock
        self.position = position
        self.confidence = confidence
        self.n_days = n_days
        self.iterations = iterations

        prices = download_stock_data(stock, start, end)
        returns = calculate_log_returns(prices).iloc[:, 0]
        self.mu = returns.mean()
        self.sigma = returns.std()

    def simulate(self) -> float:
        """Run the MC simulation and return the dollar VaR."""
        z = np.random.normal(0, 1, self.iterations)
        S_T = self.position * np.exp(
            self.n_days * (self.mu - 0.5 * self.sigma ** 2)
            + self.sigma * np.sqrt(self.n_days) * z
        )
        S_T.sort()
        percentile = np.percentile(S_T, (1 - self.confidence) * 100)
        return self.position - percentile

    def display(self):
        """Print MC VaR results."""
        var = self.simulate()
        print(f"Stock:           {self.stock}")
        print(f"μ (daily):       {self.mu:.6f}")
        print(f"σ (daily):       {self.sigma:.6f}")
        print(f"VaR MC ({int(self.confidence * 100)}%, {self.n_days}d): ${var:,.2f}")


if __name__ == '__main__':
    model = VaRMonteCarlo('C', '2015-01-01', '2026-01-01',
                          position=1_000_000, confidence=0.95,
                          n_days=1, iterations=100_000)
    model.display()
