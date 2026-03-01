"""
Present Value and Future Value calculations.

Provides both discrete and continuous compounding variants,
extracted from the duplicated logic in bond pricing modules.
"""

import numpy as np


# --- Discrete Compounding ---

def present_discrete_value(x: float, r: float, t: float) -> float:
    """PV using discrete compounding: x / (1 + r)^t."""
    return x / (1 + r) ** t


def future_discrete_value(x: float, r: float, t: float) -> float:
    """FV using discrete compounding: x * (1 + r)^t."""
    return x * (1 + r) ** t


# --- Continuous Compounding ---

def present_continuous_value(x: float, r: float, t: float) -> float:
    """PV using continuous compounding: x * e^(-r*t)."""
    return x * np.exp(-r * t)


def future_continuous_value(x: float, r: float, t: float) -> float:
    """FV using continuous compounding: x * e^(r*t)."""
    return x * np.exp(r * t)


if __name__ == '__main__':
    x, r, t = 100, 0.05, 5

    print(f"Present value (discrete):   ${present_discrete_value(x, r, t):.4f}")
    print(f"Future value  (discrete):   ${future_discrete_value(x, r, t):.4f}")
    print(f"Present value (continuous): ${present_continuous_value(x, r, t):.4f}")
    print(f"Future value  (continuous): ${future_continuous_value(x, r, t):.4f}")
