"""
Vasicek interest rate model.

Simulates a mean-reverting short rate process:
    dr = κ(θ − r) dt + σ dW
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_vasicek(r0: float, kappa: float, theta: float, sigma: float,
                     T: float = 1.0, N: int = 1000) -> tuple[np.ndarray, list[float]]:
    """
    Simulate a single Vasicek interest rate path.

    Args:
        r0:    Initial rate.
        kappa: Speed of mean reversion.
        theta: Long-term mean rate.
        sigma: Volatility.
        T:     Total time horizon.
        N:     Number of time steps.

    Returns:
        (time_grid, rates) tuple.
    """
    dt = T / N
    t = np.linspace(0, T, N + 1)
    rates = [r0]

    for _ in range(N):
        dr = kappa * (theta - rates[-1]) * dt + sigma * np.random.normal(0, np.sqrt(dt))
        rates.append(rates[-1] + dr)

    return t, rates


def plot_vasicek(t: np.ndarray, rates: list[float]):
    """Plot a single Vasicek rate path."""
    plt.figure(figsize=(10, 5))
    plt.plot(t, rates)
    plt.xlabel('Time (t)')
    plt.ylabel('Interest rate r(t)')
    plt.title('Vasicek Model Simulation')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    t, rates = simulate_vasicek(r0=1.3, kappa=0.9, theta=1.5, sigma=0.05)
    plot_vasicek(t, rates)
