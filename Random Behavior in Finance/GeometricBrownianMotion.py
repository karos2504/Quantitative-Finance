import matplotlib.pyplot as plt
import numpy as np

# S0: The initial stock price at time (t = 0)
# T: The total time of the simulation
# N: The number of discrete time steps for the simulation
# mu: The drift or mean return of the stock
# sigma: The volatility or standard deviation of the stock returns
def simulate_geometric_random_walk(S0, T=2, N=1000, mu=0.1, sigma=0.05):
    dt = T/N
    t = np.linspace(0, T, N+1)
    # Standard normal distribution N(0,1)
    W = np.random.standard_normal(size=N)
    W = np.insert(W, 0, 0)
    # N(0,dt) = sqrt(dt) * N(0,1)
    W = np.cumsum(W) * np.sqrt(dt)
    X = (mu - 0.5 * sigma ** 2) * t + sigma * W
    S = S0 * np.exp(X)
    return t, S

def plot_simulation(t, S, n_paths=1):
    plt.figure(figsize=(8, 5))
    for i in range(n_paths):
        if n_paths > 1:
            _, S = simulate_geometric_random_walk(S0=1)
        plt.plot(t, S)
    plt.xlabel('Time (t)')
    plt.ylabel('Stock Price S(t)')
    plt.title(f'Geometric Brownian Motion (n={n_paths} paths)')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    t, S = simulate_geometric_random_walk(S0=1)
    plot_simulation(t, S)