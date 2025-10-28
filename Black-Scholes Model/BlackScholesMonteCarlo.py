import numpy as np

class OptionPricing:
    def __init__(self, S0, E, T, rf, sigma, iterations):
        self.S0 = S0
        self.E = E
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.iterations = iterations

    def call_option_simulation(self):
        # Generate random draws
        rand = np.random.normal(0, 1, self.iterations)

        # Simulate end-of-period stock price
        stock_price = self.S0 * np.exp((self.rf - 0.5 * self.sigma**2) * self.T + self.sigma * np.sqrt(self.T) * rand)

        # Calculate payoff for a call option: max(S - E, 0)
        payoff = np.maximum(stock_price - self.E, 0)

        # Discount the expected payoff back to present value
        option_price = np.exp(-self.rf * self.T) * np.mean(payoff)
        return option_price

    def put_option_simulation(self):
        # Generate random draws
        rand = np.random.normal(0, 1, self.iterations)

        # Simulate end-of-period stock price
        stock_price = self.S0 * np.exp((self.rf - 0.5 * self.sigma**2) * self.T + self.sigma * np.sqrt(self.T) * rand)

        # Calculate payoff for a put option: max(E - S, 0)
        payoff = np.maximum(self.E - stock_price, 0)

        # Discount the expected payoff back to present value
        option_price = np.exp(-self.rf * self.T) * np.mean(payoff)
        return option_price


if __name__ == '__main__':
    model = OptionPricing(100, 100, 1, 0.05, 0.2, 100000)
    print('Value of call option is $%.2f' % model.call_option_simulation())
    print('Value of put option is $%.2f' % model.put_option_simulation())
