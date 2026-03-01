"""
Black-Scholes analytical option pricing model.

Computes European call and put option prices using the closed-form solution.
"""

import numpy as np
from scipy import stats


def _d1_d2(S: float, E: float, T: float, r: float, sigma: float) -> tuple[float, float]:
    """Compute the d1 and d2 parameters of the Black-Scholes formula."""
    d1 = (np.log(S / E) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1, d2


def call_option_price(S: float, E: float, T: float, r: float, sigma: float) -> float:
    """
    Black-Scholes European call option price.

    Args:
        S:     Current stock price.
        E:     Strike price.
        T:     Time to expiration (years).
        r:     Risk-free interest rate.
        sigma: Volatility of the underlying.
    """
    d1, d2 = _d1_d2(S, E, T, r, sigma)
    return S * stats.norm.cdf(d1) - E * np.exp(-r * T) * stats.norm.cdf(d2)


def put_option_price(S: float, E: float, T: float, r: float, sigma: float) -> float:
    """
    Black-Scholes European put option price.

    Args:
        S:     Current stock price.
        E:     Strike price.
        T:     Time to expiration (years).
        r:     Risk-free interest rate.
        sigma: Volatility of the underlying.
    """
    d1, d2 = _d1_d2(S, E, T, r, sigma)
    return -S * stats.norm.cdf(-d1) + E * np.exp(-r * T) * stats.norm.cdf(-d2)


if __name__ == '__main__':
    S0, E, T, r, sigma = 100, 100, 1, 0.05, 0.2

    print(f"Call option price: ${call_option_price(S0, E, T, r, sigma):.4f}")
    print(f"Put  option price: ${put_option_price(S0, E, T, r, sigma):.4f}")
