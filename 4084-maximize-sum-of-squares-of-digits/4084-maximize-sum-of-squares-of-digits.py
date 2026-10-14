class Solution:
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        result = []

        for _ in range(num):
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit

        return ''.join(result)