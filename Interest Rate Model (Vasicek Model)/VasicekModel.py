import numpy as np
import matplotlib.pyplot as plt

def vasicek_model(r0, kappa, theta, sigma, T=1, N=1000):
    dt = float(T / N)
    t = np.linspace(0, T, N+1)
    rates = [r0]

    for _ in range(N):
        dr = kappa * (theta - rates[-1]) * dt + sigma * np.random.normal(0, np.sqrt(dt))
        rates.append(rates[-1] + dr)
    return t, rates

def plot_model(t, r):
    plt.plot(t, r)
    plt.xlabel('Time (t)')
    plt.ylabel('Interest rate r(t)')
    plt.title('Vasicek Model Simulation')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    time, rates = vasicek_model(r0=1.3, kappa=0.9, theta=1.5, sigma=0.05)
    plot_model(time, rates)
