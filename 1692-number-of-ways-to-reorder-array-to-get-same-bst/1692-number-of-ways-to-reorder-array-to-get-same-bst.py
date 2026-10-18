from typing import List
from functools import lru_cache

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations C[i][j]
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        @lru_cache(None)
        def solve(values):
            if len(values) <= 2:
                return 1

            root = values[0]
            left = tuple(x for x in values[1:] if x < root)
            right = tuple(x for x in values[1:] if x > root)

            ways_left = solve(left)
            ways_right = solve(right)

            interleavings = comb[len(left) + len(right)][len(left)]

            return interleavings * ways_left % MOD * ways_right % MOD

        # Subtract the original ordering itself
        return (solve(tuple(nums)) - 1) % MOD