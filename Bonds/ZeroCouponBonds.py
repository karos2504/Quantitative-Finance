import numpy as np
class ZeroCouponBonds:
    def __init__(self, principal, maturity, interest_rate):
        self.principal = principal
        self.maturity  = maturity
        self.interest_rate = interest_rate / 100

    # def present_value(self, x, t):
    #     return x / (1 + self.interest_rate)**t
    
    def present_value(self, x, t):
        return x * np.exp(-self.interest_rate*t)

    def calculate_price(self):
        return self.present_value(self.principal, self.maturity)
    
if __name__ == '__main__':
    bond = ZeroCouponBonds(1000, 2, 4)
    print('Price of the bond in dollars: %.2f' % bond.calculate_price())