"""
Geometric Brownian Motion (GBM) simulation.

    S(t) = S₀ · exp[(μ − ½σ²)t + σW(t)]

Used to model stock price dynamics under the risk-neutral measure.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_gbm(S0: float, mu: float = 0.1, sigma: float = 0.05,
                 T: float = 2.0, N: int = 1000) -> tuple[np.ndarray, np.ndarray]:
    """
    Simulate a single GBM price path.

    Args:
        S0:    Initial stock price.
        mu:    Drift (annualised return).
        sigma: Volatility.
        T:     Time horizon (years).
        N:     Number of time steps.

    Returns:
        (time_grid, price_path) tuple.
    """
    dt = T / N
    t = np.linspace(0, T, N + 1)

    W = np.random.standard_normal(N)
    W = np.insert(W, 0, 0)
    W = np.cumsum(W) * np.sqrt(dt)

    X = (mu - 0.5 * sigma ** 2) * t + sigma * W
    S = S0 * np.exp(X)

    return t, S


def plot_gbm(S0: float = 1.0, n_paths: int = 1, **kwargs):
    """Simulate and plot one or more GBM paths."""
    plt.figure(figsize=(10, 5))
    for _ in range(n_paths):
        t, S = simulate_gbm(S0, **kwargs)
        plt.plot(t, S, alpha=0.7)

    plt.xlabel('Time (t)')
    plt.ylabel('Stock Price S(t)')
    plt.title(f'Geometric Brownian Motion ({n_paths} path{"s" if n_paths > 1 else ""})')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_gbm(S0=1.0, n_paths=5)
