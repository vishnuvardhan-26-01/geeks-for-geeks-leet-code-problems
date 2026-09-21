class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            x = num % k
            new_dp = [0] * k

            # Subarray containing only this element
            new_dp[x] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r]:
                    nr = (r * x) % k
                    new_dp[nr] += dp[r]

            dp = new_dp

            # Add subarrays ending at this position
            for r in range(k):
                ans[r] += dp[r]

        return ans
        