import numpy as np
import pandas as pd

NUM_OF_SIMULATIONS = 1000
NUM_OF_POINTS = 200

def monte_carlo_simulation(x, r0, kappa, theta, sigma, T=1):
    dt = T / NUM_OF_POINTS
    result = []

    for _ in range(NUM_OF_SIMULATIONS):
        rates = [r0]
        for _ in range(NUM_OF_POINTS):
            dr = kappa * (theta - rates[-1]) * dt + sigma * np.random.normal(0, np.sqrt(dt))
            rates.append(rates[-1] + dr)
        result.append(rates)

    simulation_data = pd.DataFrame(result).T

    # Integral of r(t) over time
    integral_sum = simulation_data.sum() * dt
    # Present value of future cash flow
    present_integral_sum = np.exp(-integral_sum)
    # Bond price is the mean PV times face value
    bond_price = x * np.mean(present_integral_sum)

    return bond_price

if __name__ == '__main__':
    bond_price = monte_carlo_simulation(1000, 0.1, 0.3, 0.1, 0.03)
    print(f'Bond price based on Monte-Carlo simulation: ${bond_price:.2f}')
