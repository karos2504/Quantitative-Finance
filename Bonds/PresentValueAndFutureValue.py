from math import exp

def present_discrete_value(x, r, n):
    return x / (1 + r)**n

def future_discrete_value(x, r, n):
    return x * (1 + r)**n

def present_continuous_value(x, r, t):
    return x / exp(r * t)

def future_continuous_value(x, r, t):
    return x * exp(r * t) 

if __name__ == '__main__':
    # Value of investment on value
    x = 100

    # Define the interest rate (r)
    r = 0.05

    # Duration (years)
    n = 5

    print('Present values (discrete model) of x: %s'% present_discrete_value(x, r, n))
    print('Future values (discrete model) of x: %s'% future_discrete_value(x, r, n))
    print('Present values (continuous model) of x: %s'% present_continuous_value(x, r, n))
    print('Future values (continuous model) of x: %s'% future_continuous_value(x, r, n))