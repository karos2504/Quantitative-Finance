"""
Zero-Coupon Bond pricing.

Uses continuous compounding via the shared present_value module.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bonds.present_value import present_continuous_value


class ZeroCouponBond:
    """Prices a zero-coupon bond using continuous discounting."""

    def __init__(self, principal: float, maturity: int, interest_rate: float):
        """
        Args:
            principal:     Face value of the bond.
            maturity:      Years to maturity.
            interest_rate: Annual interest rate in percent (e.g. 4 for 4%).
        """
        self.principal = principal
        self.maturity = maturity
        self.interest_rate = interest_rate / 100

    def calculate_price(self) -> float:
        """Return the present value of the bond's principal."""
        return present_continuous_value(self.principal, self.interest_rate, self.maturity)


if __name__ == '__main__':
    bond = ZeroCouponBond(principal=1000, maturity=2, interest_rate=4)
    print(f"Zero-coupon bond price: ${bond.calculate_price():.2f}")
