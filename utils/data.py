"""
Shared data download and returns calculation utilities.

Consolidates the repeated download/return logic from CAPM, VaR, Markowitz,
and NormalDistributionOfReturns into a single reusable module.
"""

import numpy as np
import pandas as pd
import yfinance as yf


def download_stock_data(tickers: list[str] | str, start: str, end: str) -> pd.DataFrame:
    """
    Download adjusted close prices for one or more tickers.

    Args:
        tickers: Single ticker string or list of ticker strings.
        start:   Start date in 'YYYY-MM-DD' format.
        end:     End date in 'YYYY-MM-DD' format.

    Returns:
        DataFrame with adjusted close prices, columns = tickers.
    """
    if isinstance(tickers, str):
        tickers = [tickers]

    data = {}
    for ticker in tickers:
        raw = yf.download(ticker, start=start, end=end, auto_adjust=False)
        if isinstance(raw.columns, pd.MultiIndex):
            data[ticker] = raw['Adj Close'].iloc[:, 0]
        else:
            data[ticker] = raw['Adj Close']

    return pd.DataFrame(data).dropna()


def calculate_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate logarithmic returns from price data.

    Args:
        prices: DataFrame of asset prices.

    Returns:
        DataFrame of log returns (first row NaN dropped).
    """
    return np.log(prices / prices.shift(1)).dropna()
