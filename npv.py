"""Net Present Value (NPV) calculator.

This module provides a simple function to compute the NPV of future cash
flows given a constant discount rate.
"""

from typing import Iterable


def npv(cash_flows: Iterable[float], discount_rate: float) -> float:
    """Return the net present value of ``cash_flows``.

    Parameters
    ----------
    cash_flows:
        Iterable of cash flows where index represents the period starting at 0.
    discount_rate:
        Discount rate per period expressed as a decimal (e.g. 0.1 for 10%).
    """
    return sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(cash_flows))


if __name__ == "__main__":
    # Example usage
    example_flows = [-1000, 200, 300, 400, 500]
    example_rate = 0.1
    print(f"NPV: {npv(example_flows, example_rate):.2f}")
