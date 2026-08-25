from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums):
        @lru_cache(None)
        def dfs(l, r):
            if l == r:
                return nums[l]

            return max(
                nums[l] - dfs(l + 1, r),
                nums[r] - dfs(l, r - 1)
            )

        return dfs(0, len(nums) - 1) >= 0