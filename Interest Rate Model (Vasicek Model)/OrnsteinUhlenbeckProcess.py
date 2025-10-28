import numpy as np
import matplotlib.pyplot as plt

def generate_ou_process(dt=0.1, theta=1.2, mu=0.5, sigma=0.3, n=1000):
    x = np.zeros(n+1)
    for t in range(1, n+1):
        x[t] = x[t-1] + theta * (mu - x[t-1]) * dt + sigma * np.random.normal(0, np.sqrt(dt))
    return x

def plot_process(x, dt=0.1):
    t = np.linspace(0, dt*len(x), len(x))
    plt.plot(t, x)
    plt.xlabel('Time t')
    plt.ylabel('x(t)')
    plt.title('Ornstein-Uhlenbeck Process')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    data = generate_ou_process()
    plot_process(data)
