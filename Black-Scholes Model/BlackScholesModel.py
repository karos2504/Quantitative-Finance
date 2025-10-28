from scipy import stats
import numpy as np

def call_option_price(S, E, T, r, sigma):
    # First calculate d1 and d2 parameters
    d1 = (np.log(S / E) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    print('The d1 and d2 parameters: %s %s' % (d1, d2))
    # Use the N(x) to calculate the price of the option
    call_option = S * stats.norm.cdf(d1) - E * np.exp(-r * T) * stats.norm.cdf(d2)
    return call_option

def put_option_price(S, E, T, r, sigma):
    # First calculate d1 and d2 parameters
    d1 = (np.log(S / E) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    print('The d1 and d2 parameters: %s %s' % (d1, d2))
    # Use the N(x) to calculate the price of the option
    put_option = -S * stats.norm.cdf(-d1) + E * np.exp(-r * T) * stats.norm.cdf(-d2)
    return put_option

if __name__ == '__main__':
    # Underlying stock price at t=0
    S0 = 100
    # Strike price
    E = 100
    # Expiry 1 year = 365 days
    T = 1
    # Risk-free rate
    r = 0.05
    # Volatility of the underlying stock
    sigma = 0.2
    
    print('Call option price according to Black-Scholes model: ', call_option_price(S0, E, T, r, sigma))
    print('Put option price according to Black-Scholes model: ', put_option_price(S0, E, T, r, sigma))
