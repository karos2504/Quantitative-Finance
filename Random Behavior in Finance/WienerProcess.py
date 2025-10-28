import numpy as np
import matplotlib.pyplot as plt

def wiener_process(dt=0.1, x0=0, n=1000):
    """
    Simulate a Wiener process (Brownian motion).

    Parameters:
    dt : float - Time step size
    x0 : float - Initial value (W(0))
    n  : int   - Number of steps

    Returns:
    t : numpy array - Time vector
    W : numpy array - Wiener process values
    """
    # Time vector from 0 to n*dt
    t = np.linspace(0, n*dt, n+1)
    
    # Initialize Wiener process
    W = np.zeros(n+1)
    W[0] = x0

    # Generate Gaussian increments
    dW = np.random.normal(0, np.sqrt(dt), n)
    
    # Construct the Wiener process via cumulative sum
    W[1:] = x0 + np.cumsum(dW)

    return t, W

def plot_process(t, W):
    plt.plot(t, W)
    plt.xlabel('Time (t)')
    plt.ylabel('Wiener process W(t)')
    plt.title('Simulated Wiener Process')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    t, W = wiener_process(dt=0.01, n=1000)
    plot_process(t, W)
