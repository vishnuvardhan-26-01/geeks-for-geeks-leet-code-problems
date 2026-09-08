class Solution:
    def countCommas(self, n):
        total = 0

        for i in range(1000, n + 1):
            total += len(str(i)) // 4

        return total