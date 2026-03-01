"""
Coupon Bond pricing.

Uses continuous compounding via the shared present_value module.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bonds.present_value import present_continuous_value


class CouponBond:
    """Prices a coupon-bearing bond using continuous discounting."""

    def __init__(self, principal: float, rate: float, maturity: int, interest_rate: float):
        """
        Args:
            principal:     Face value of the bond.
            rate:          Annual coupon rate in percent (e.g. 10 for 10%).
            maturity:      Years to maturity.
            interest_rate: Annual discount rate in percent (e.g. 4 for 4%).
        """
        self.principal = principal
        self.rate = rate / 100
        self.maturity = maturity
        self.interest_rate = interest_rate / 100

    def calculate_price(self) -> float:
        """Return the sum of discounted coupon payments plus discounted principal."""
        coupon = self.principal * self.rate
        price = sum(
            present_continuous_value(coupon, self.interest_rate, t)
            for t in range(1, self.maturity + 1)
        )
        price += present_continuous_value(self.principal, self.interest_rate, self.maturity)
        return price


if __name__ == '__main__':
    bond = CouponBond(principal=1000, rate=10, maturity=3, interest_rate=4)
    print(f"Coupon bond price: ${bond.calculate_price():.2f}")
