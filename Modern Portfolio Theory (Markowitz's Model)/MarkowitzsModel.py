import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization

# Constants
NUM_TRADING_DAYS = 252  # Average trading days in a year
NUM_PORTFOLIOS = 10000  # Number of random portfolios to generate
STOCKS = ['AAPL', 'WMT', 'TSLA', 'GE', 'AMZN', 'DB']
START_DATE = '2010-01-01'
END_DATE = '2025-01-01'

# -------------------------
# Data Download & Processing
# -------------------------
def download_data():
    stock_data = {}
    for stock in STOCKS:
        ticker = yf.Ticker(stock)
        stock_data[stock] = ticker.history(start=START_DATE, end=END_DATE, auto_adjust=False)['Adj Close']
    return pd.DataFrame(stock_data).dropna()

def show_data(data):
    data.plot(figsize=(10, 5), title="Stock Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()

def calculate_return(data):
    log_return = np.log(data / data.shift(1))
    return log_return[1:]

# -------------------------
# Portfolio Metrics
# -------------------------
def statistics(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility
    return np.array([portfolio_return, portfolio_volatility, sharpe_ratio])

def generate_portfolios(returns):
    portfolio_weights, portfolio_means, portfolio_risks = [], [], []

    for _ in range(NUM_PORTFOLIOS):
        w = np.random.random(len(STOCKS))
        w /= np.sum(w)
        portfolio_weights.append(w)
        portfolio_means.append(np.sum(returns.mean() * w) * NUM_TRADING_DAYS)
        portfolio_risks.append(np.sqrt(np.dot(w.T, np.dot(returns.cov() * NUM_TRADING_DAYS, w))))

    return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_risks)

def show_portfolios(returns, volatilities):
    plt.figure(figsize=(10, 6))
    plt.scatter(volatilities, returns, c=returns / volatilities, marker='o')
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.title('Randomly Generated Portfolios')
    plt.grid(True)
    plt.show()

# -------------------------
# Portfolio Optimization
# -------------------------

# Scipy optimize module can find the minimum of a given function
# The maximum of a f(x) is the minimum of -f(x)
def min_function_sharpe(weights, returns):
    return -statistics(weights, returns)[2] # Maximize Sharpe ratio

# What are the constraints? The sum of weights = 1 !!!
# f(x) = 0 this is the function to minimize
def optimize_portfolio(returns):
    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # Weights sum = 1
    bounds = tuple((0, 1) for _ in range(len(STOCKS)))  # Each weight between 0 and 1
    x0 = np.array([1 / len(STOCKS)] * len(STOCKS))  # Equal weight initial guess

    return optimization.minimize(fun=min_function_sharpe, x0=x0, args=returns, method='SLSQP', bounds=bounds, constraints=constraints)

def print_optimal_portfolio(optimum, returns):
    print("Optimal Portfolio Weights:", optimum['x'].round(3))
    ret, vol, sharpe = statistics(optimum['x'], returns)
    print(f"Expected Return: {ret:.4f}, Volatility: {vol:.4f}, Sharpe Ratio: {sharpe:.4f}")

def show_optimal_portfolio(optimum, returns, portfolio_rets, portfolio_vols):
    plt.figure(figsize=(10, 6))
    plt.scatter(portfolio_vols, portfolio_rets, c=portfolio_rets / portfolio_vols, marker='o')
    plt.scatter(statistics(optimum['x'], returns)[1], statistics(optimum['x'], returns)[0], 
                c='g', marker='*', s=200, label='Optimal Portfolio')
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.title('Portfolio Optimization')
    plt.legend()
    plt.grid(True)
    plt.show()

# -------------------------
# Main Execution
# -------------------------
if __name__ == '__main__':
    dataset = download_data()
    show_data(dataset)

    log_daily_returns = calculate_return(dataset)

    pweights, means, risks = generate_portfolios(log_daily_returns)
    show_portfolios(means, risks)

    optimum = optimize_portfolio(log_daily_returns)
    print_optimal_portfolio(optimum, log_daily_returns)
    show_optimal_portfolio(optimum, log_daily_returns, means, risks)
