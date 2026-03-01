"""
Ornstein-Uhlenbeck (OU) process simulation.

    dx = θ(μ − x) dt + σ dW

A continuous-time mean-reverting stochastic process used to model
interest rates and other financial quantities.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_ou(theta: float = 1.2, mu: float = 0.5, sigma: float = 0.3,
                dt: float = 0.1, n: int = 1000) -> np.ndarray:
    """
    Simulate an OU process starting at x(0) = 0.

    Returns:
        Array of length n+1 containing x(t) values.
    """
    x = np.zeros(n + 1)
    for i in range(1, n + 1):
        x[i] = x[i - 1] + theta * (mu - x[i - 1]) * dt + sigma * np.random.normal(0, np.sqrt(dt))
    return x


def plot_ou(x: np.ndarray, dt: float = 0.1):
    """Plot the OU process trajectory."""
    t = np.linspace(0, dt * len(x), len(x))
    plt.figure(figsize=(10, 5))
    plt.plot(t, x)
    plt.xlabel('Time (t)')
    plt.ylabel('x(t)')
    plt.title('Ornstein-Uhlenbeck Process')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    data = simulate_ou()
    plot_ou(data)
