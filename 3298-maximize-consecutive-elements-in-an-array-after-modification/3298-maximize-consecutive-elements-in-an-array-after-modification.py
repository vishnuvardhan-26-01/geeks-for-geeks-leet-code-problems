class Solution:
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = {}
        ans = 0

        for x in nums:
            prev_x = dp.get(x, 0)
            prev_x1 = dp.get(x - 1, 0)

            dp[x] = max(dp.get(x, 0), prev_x1 + 1)
            dp[x + 1] = max(dp.get(x + 1, 0), prev_x + 1)

            ans = max(ans, dp[x], dp[x + 1])

        return ans