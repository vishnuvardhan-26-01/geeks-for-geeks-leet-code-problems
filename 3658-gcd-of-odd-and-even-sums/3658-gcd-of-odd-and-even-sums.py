from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n * n
        sumEven = n * (n + 1)
        return gcd(sumOdd, sumEven)