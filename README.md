# Quantitative Finance

A collection of quantitative finance models and simulations implemented in Python.

## Modules

| Package | Description |
|---|---|
| `bonds/` | Zero-coupon & coupon bond pricing, present/future value |
| `options/` | Black-Scholes (analytical & Monte Carlo), stock price simulation |
| `capm/` | Capital Asset Pricing Model, return distribution analysis |
| `portfolio/` | Markowitz mean-variance optimization |
| `risk/` | Value at Risk — analytical and Monte Carlo |
| `interest_rates/` | Vasicek model, Ornstein-Uhlenbeck process, bond pricing |
| `stochastic/` | Wiener process, geometric Brownian motion |
| `utils/` | Shared data download, log returns, and plotting helpers |
| `foundations/` | Python, NumPy, and OOP learning exercises |

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run any module directly
python -m bonds.zero_coupon_bond
python -m options.black_scholes
python -m capm.capm
python -m portfolio.markowitz
python -m risk.var_analytical
python -m interest_rates.vasicek
python -m stochastic.wiener_process
```

## Dependencies

- numpy
- pandas
- matplotlib
- yfinance
- scipy
