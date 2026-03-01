"""
Monte Carlo option pricing using geometric Brownian motion.

Reduces code duplication between call/put by using a shared _simulate() method.
"""

import numpy as np


class OptionPricingMC:
    """Monte Carlo pricer for European call and put options."""

    def __init__(self, S0: float, E: float, T: float, rf: float,
                 sigma: float, iterations: int = 100_000):
        """
        Args:
            S0:         Initial stock price.
            E:          Strike price.
            T:          Time to expiration (years).
            rf:         Risk-free interest rate.
            sigma:      Volatility.
            iterations: Number of Monte Carlo paths.
        """
        self.S0 = S0
        self.E = E
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.iterations = iterations

    def _simulate_terminal_prices(self) -> np.ndarray:
        """Simulate terminal stock prices via GBM."""
        z = np.random.normal(0, 1, self.iterations)
        return self.S0 * np.exp(
            (self.rf - 0.5 * self.sigma ** 2) * self.T
            + self.sigma * np.sqrt(self.T) * z
        )

    def _discount(self, payoffs: np.ndarray) -> float:
        """Discount the mean payoff to present value."""
        return np.exp(-self.rf * self.T) * np.mean(payoffs)

    def call_option_price(self) -> float:
        """Monte Carlo price for a European call."""
        S_T = self._simulate_terminal_prices()
        return self._discount(np.maximum(S_T - self.E, 0))

    def put_option_price(self) -> float:
        """Monte Carlo price for a European put."""
        S_T = self._simulate_terminal_prices()
        return self._discount(np.maximum(self.E - S_T, 0))


if __name__ == '__main__':
    model = OptionPricingMC(S0=100, E=100, T=1, rf=0.05, sigma=0.2)
    print(f"Call option (MC): ${model.call_option_price():.2f}")
    print(f"Put  option (MC): ${model.put_option_price():.2f}")
