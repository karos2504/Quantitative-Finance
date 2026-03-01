"""
Wiener process (Brownian motion) simulation.

    W(0) = 0,  dW ~ N(0, dt)
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_wiener(dt: float = 0.01, n: int = 1000,
                    x0: float = 0.0) -> tuple[np.ndarray, np.ndarray]:
    """
    Simulate a Wiener process.

    Args:
        dt: Time step size.
        n:  Number of steps.
        x0: Initial value W(0).

    Returns:
        (time_grid, W) tuple.
    """
    t = np.linspace(0, n * dt, n + 1)
    W = np.zeros(n + 1)
    W[0] = x0
    W[1:] = x0 + np.cumsum(np.random.normal(0, np.sqrt(dt), n))
    return t, W


def plot_wiener(t: np.ndarray, W: np.ndarray):
    """Plot a Wiener process trajectory."""
    plt.figure(figsize=(10, 5))
    plt.plot(t, W)
    plt.xlabel('Time (t)')
    plt.ylabel('W(t)')
    plt.title('Simulated Wiener Process')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    t, W = simulate_wiener(dt=0.01, n=1000)
    plot_wiener(t, W)
