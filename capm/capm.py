"""
Capital Asset Pricing Model (CAPM).

Downloads stock and market data, computes beta via covariance and linear
regression, and visualises the CAPM regression line.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils.data import download_stock_data

RISK_FREE_RATE = 0.05
MONTHS_IN_YEAR = 12


class CAPM:
    """CAPM calculator comparing a stock to a market index."""

    def __init__(self, stock: str, market: str, start: str, end: str):
        self.stock = stock
        self.market = market
        self.start = start
        self.end = end
        self.data: pd.DataFrame | None = None

    def initialize(self):
        """Download prices, resample to monthly, and compute log returns."""
        prices = download_stock_data([self.stock, self.market], self.start, self.end)
        monthly = prices.resample('ME').last()

        self.data = pd.DataFrame({
            's_adjclose': monthly[self.stock],
            'm_adjclose': monthly[self.market],
        })
        self.data[['s_returns', 'm_returns']] = np.log(
            self.data[['s_adjclose', 'm_adjclose']]
        ).diff()
        self.data = self.data.dropna()

    def calculate_beta(self) -> float:
        """Compute beta from the covariance formula."""
        cov = np.cov(self.data['s_returns'], self.data['m_returns'])
        beta = cov[0, 1] / np.var(self.data['m_returns'])
        print(f"Beta (covariance): {beta:.4f}")
        return beta

    def regression(self):
        """Fit a linear regression, print expected return, and plot."""
        beta, alpha = np.polyfit(self.data['m_returns'], self.data['s_returns'], deg=1)
        expected_return = RISK_FREE_RATE + beta * (
            self.data['m_returns'].mean() * MONTHS_IN_YEAR - RISK_FREE_RATE
        )

        print(f"Beta (regression):  {beta:.4f}")
        print(f"Expected return:    {expected_return:.4f}")
        self._plot_regression(alpha, beta)

    def _plot_regression(self, alpha: float, beta: float):
        """Scatter plot of returns with the CAPM regression line."""
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.scatter(self.data['m_returns'], self.data['s_returns'], label='Data Points')
        ax.plot(self.data['m_returns'],
                beta * self.data['m_returns'] + alpha,
                color='red', label='CAPM Line')
        ax.set_title('Capital Asset Pricing Model — Alpha & Beta')
        ax.set_xlabel(r'Market return $R_m$', fontsize=14)
        ax.set_ylabel(r'Stock return $R_a$', fontsize=14)
        ax.text(0.08, 0.05, r'$R_a = \beta \cdot R_m + \alpha$', fontsize=14)
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    model = CAPM(stock='IBM', market='^GSPC', start='2010-01-01', end='2025-01-01')
    model.initialize()
    model.calculate_beta()
    model.regression()
