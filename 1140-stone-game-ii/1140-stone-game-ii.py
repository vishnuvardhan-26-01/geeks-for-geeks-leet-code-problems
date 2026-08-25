class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = [[0] * (n + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                if i + 2 * M >= n:
                    dp[i][M] = suffix[i]
                else:
                    for X in range(1, 2 * M + 1):
                        dp[i][M] = max(
                            dp[i][M],
                            suffix[i] - dp[i + X][max(M, X)]
                        )

        return dp[0][1]