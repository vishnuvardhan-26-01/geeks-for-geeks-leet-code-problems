class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            best = float("-inf")
            total = 0

            for k in range(3):
                if i + k < n:
                    total += stoneValue[i + k]
                    best = max(best, total - dp[i + k + 1])

            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"