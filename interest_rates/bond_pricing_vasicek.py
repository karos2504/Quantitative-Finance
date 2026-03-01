"""
Bond pricing using the Vasicek interest rate model.

Simulates many short-rate paths via the Vasicek SDE, integrates each
path to get a discount factor, and prices the bond as the mean discounted
face value.
"""

import numpy as np
import pandas as pd

NUM_SIMULATIONS = 1000
NUM_STEPS = 200


def price_bond_vasicek(face_value: float, r0: float, kappa: float,
                       theta: float, sigma: float, T: float = 1.0) -> float:
    """
    Monte Carlo bond price under the Vasicek model.

    Args:
        face_value: Bond's face (par) value.
        r0:         Initial short rate.
        kappa:      Mean-reversion speed.
        theta:      Long-term mean rate.
        sigma:      Rate volatility.
        T:          Time to maturity (years).

    Returns:
        Estimated bond price.
    """
    dt = T / NUM_STEPS
    result = []

    for _ in range(NUM_SIMULATIONS):
        rates = [r0]
        for _ in range(NUM_STEPS):
            dr = kappa * (theta - rates[-1]) * dt + sigma * np.random.normal(0, np.sqrt(dt))
            rates.append(rates[-1] + dr)
        result.append(rates)

    simulation_data = pd.DataFrame(result).T
    integral_sum = simulation_data.sum() * dt
    discount_factors = np.exp(-integral_sum)

    return face_value * np.mean(discount_factors)


if __name__ == '__main__':
    price = price_bond_vasicek(
        face_value=1000, r0=0.1, kappa=0.3, theta=0.1, sigma=0.03,
    )
    print(f"Bond price (Vasicek MC): ${price:.2f}")
