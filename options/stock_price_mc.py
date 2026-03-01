"""
Monte Carlo simulation of stock prices using geometric Brownian motion.

Simulates multiple price paths over a given number of trading days and
plots the results with the mean path highlighted.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

NUM_SIMULATIONS = 1000


def simulate_stock_prices(S0: float, mu: float, sigma: float,
                          n_days: int = 252) -> pd.DataFrame:
    """
    Simulate stock price paths via GBM.

    Args:
        S0:     Initial stock price.
        mu:     Daily drift (expected return).
        sigma:  Daily volatility.
        n_days: Number of trading days to simulate.

    Returns:
        DataFrame with shape (n_days+1, NUM_SIMULATIONS) plus a 'mean' column.
    """
    dt = 1 / n_days
    result = []

    for _ in range(NUM_SIMULATIONS):
        prices = [S0]
        for _ in range(n_days):
            z = np.random.normal()
            S_t = prices[-1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)
            prices.append(S_t)
        result.append(prices)

    df = pd.DataFrame(result).T
    df['mean'] = df.mean(axis=1)
    return df


def plot_simulation(df: pd.DataFrame, n_days: int = 252):
    """Plot a subset of simulated paths and the mean path."""
    plt.figure(figsize=(10, 5))
    plt.plot(df.iloc[:, :10], alpha=0.6)
    plt.plot(df['mean'], 'k', label='Mean Path', linewidth=2)
    plt.title('Monte Carlo Simulation of Stock Prices')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(f"Predicted mean stock price after {n_days} days: ${df['mean'].iloc[-1]:.2f}")


if __name__ == '__main__':
    df = simulate_stock_prices(S0=50, mu=0.0002, sigma=0.01)
    plot_simulation(df)
