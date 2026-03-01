"""
Analytical (parametric) Value at Risk.

Uses the variance-covariance method under the assumption of normally
distributed returns.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
from scipy.stats import norm

from utils.data import download_stock_data, calculate_log_returns


class VaRAnalytical:
    """Compute VaR using the parametric (normal) approach."""

    def __init__(self, stock: str, start: str, end: str,
                 confidence: float = 0.95, position: float = 1e6):
        """
        Args:
            stock:      Ticker symbol.
            start/end:  Date range for historical returns.
            confidence: Confidence level (e.g. 0.95 for 95%).
            position:   Dollar value of the portfolio position.
        """
        self.stock = stock
        self.confidence = confidence
        self.position = position

        prices = download_stock_data(stock, start, end)
        returns = calculate_log_returns(prices).iloc[:, 0]
        self.mu = returns.mean()
        self.sigma = returns.std()

    def calculate_var(self, n_days: int = 1) -> float:
        """
        Compute the n-day VaR.

        Args:
            n_days: Holding period in days.

        Returns:
            Dollar VaR (positive number = potential loss).
        """
        z = norm.ppf(1 - self.confidence)
        return self.position * (self.mu * n_days - self.sigma * np.sqrt(n_days) * z)

    def display(self, n_days: int = 1):
        """Print VaR results."""
        var = self.calculate_var(n_days)
        print(f"Stock:       {self.stock}")
        print(f"μ (daily):   {self.mu:.6f}")
        print(f"σ (daily):   {self.sigma:.6f}")
        print(f"VaR ({int(self.confidence * 100)}%, {n_days}d): ${var:,.2f}")


if __name__ == '__main__':
    model = VaRAnalytical('AAPL', '2015-01-01', '2026-01-01',
                          confidence=0.95, position=1_000_000)
    model.display(n_days=1)
