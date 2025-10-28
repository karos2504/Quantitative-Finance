import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

NUM_OF_SIMULATIONS = 1000

def stock_monte_carlo(S0, mu, sigma, N=252):
    dt = 1 / N  # time step (1 trading day = 1/252 year)
    result = []

    for _ in range(NUM_OF_SIMULATIONS):
        prices = [S0]
        for _ in range(N):
            # Generate one random normal shock
            z = np.random.normal()
            # Geometric Brownian Motion formula
            S_t = prices[-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
            prices.append(S_t)
        result.append(prices)
    
    # Convert results to DataFrame
    simulation_data = pd.DataFrame(result).T
    simulation_data['mean'] = simulation_data.mean(axis=1)

    # Plot results
    plt.figure(figsize=(10,5))
    plt.plot(simulation_data.iloc[:, :10])  # plot 10 random simulations
    plt.plot(simulation_data['mean'], 'k', label='Mean Path', linewidth=2)
    plt.title('Monte Carlo Simulation of Stock Prices')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    print('Predicted mean stock price after %d days: $%.2f' % (N, simulation_data["mean"].iloc[-1]))

if __name__ == '__main__':
    stock_monte_carlo(S0=50, mu=0.0002, sigma=0.01)
