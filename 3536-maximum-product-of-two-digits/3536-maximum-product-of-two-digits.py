class Solution:
    def maxProduct(self, n: int) -> int:
        first = second = -1

        while n:
            d = n % 10
            if d >= first:
                second = first
                first = d
            elif d > second:
                second = d
            n //= 10

        return first * second