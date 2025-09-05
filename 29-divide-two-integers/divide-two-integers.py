class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == 0:
            return 0
        x = int((dividend / divisor) / abs(dividend / divisor))
        return (abs(dividend) // abs(divisor)) * x
