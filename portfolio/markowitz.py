"""
Markowitz Mean-Variance Portfolio Optimization.

Downloads stock data, generates random portfolios, and finds the optimal
portfolio that maximises the Sharpe ratio using scipy optimisation.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimization

from utils.data import download_stock_data, calculate_log_returns

# Constants
NUM_TRADING_DAYS = 252
NUM_PORTFOLIOS = 10_000
STOCKS = ['AAPL', 'WMT', 'TSLA', 'GE', 'AMZN', 'DB']
START_DATE = '2010-01-01'
END_DATE = '2026-01-01'


# ----- Portfolio Metrics -----

def portfolio_statistics(weights: np.ndarray, returns) -> np.ndarray:
    """Return [annualised_return, annualised_volatility, sharpe_ratio]."""
    port_return = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    port_vol = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))
    return np.array([port_return, port_vol, port_return / port_vol])


def _neg_sharpe(weights, returns):
    """Objective function for optimiser (minimise negative Sharpe)."""
    return -portfolio_statistics(weights, returns)[2]


# ----- Random Portfolio Generation -----

def generate_random_portfolios(returns):
    """Generate NUM_PORTFOLIOS random weight allocations."""
    n = len(STOCKS)
    weights_list, means, risks = [], [], []

    for _ in range(NUM_PORTFOLIOS):
        w = np.random.random(n)
        w /= w.sum()
        stats = portfolio_statistics(w, returns)
        weights_list.append(w)
        means.append(stats[0])
        risks.append(stats[1])

    return np.array(weights_list), np.array(means), np.array(risks)


# ----- Optimisation -----

def optimize_portfolio(returns):
    """Find the maximum-Sharpe-ratio portfolio via SLSQP."""
    n = len(STOCKS)
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    bounds = tuple((0, 1) for _ in range(n))
    x0 = np.full(n, 1 / n)

    return optimization.minimize(
        fun=_neg_sharpe, x0=x0, args=returns,
        method='SLSQP', bounds=bounds, constraints=constraints,
    )


# ----- Visualisation -----

def plot_portfolios(means, risks, optimum=None, returns=None):
    """Scatter plot of random portfolios coloured by Sharpe ratio."""
    plt.figure(figsize=(10, 6))
    plt.scatter(risks, means, c=means / risks, marker='o', alpha=0.6)
    plt.colorbar(label='Sharpe Ratio')

    if optimum is not None and returns is not None:
        opt_stats = portfolio_statistics(optimum['x'], returns)
        plt.scatter(opt_stats[1], opt_stats[0], c='g', marker='*', s=300,
                    label='Optimal Portfolio')
        plt.legend()

    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.title('Markowitz Portfolio Optimization')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ----- Main -----

if __name__ == '__main__':
    prices = download_stock_data(STOCKS, START_DATE, END_DATE)
    log_returns = calculate_log_returns(prices)

    # Show price history
    prices.plot(figsize=(10, 5), title='Stock Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Random portfolios
    weights, means, risks = generate_random_portfolios(log_returns)

    # Optimise
    optimum = optimize_portfolio(log_returns)
    opt_ret, opt_vol, opt_sharpe = portfolio_statistics(optimum['x'], log_returns)

    print("Optimal Weights:", optimum['x'].round(3))
    print(f"Expected Return: {opt_ret:.4f}  |  Volatility: {opt_vol:.4f}  |  Sharpe: {opt_sharpe:.4f}")

    # Plot
    plot_portfolios(means, risks, optimum, log_returns)
