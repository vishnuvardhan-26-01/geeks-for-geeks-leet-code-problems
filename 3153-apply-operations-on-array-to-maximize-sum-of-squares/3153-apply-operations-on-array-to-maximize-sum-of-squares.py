class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bit_count = [0] * 32

        for num in nums:
            for bit in range(32):
                if num & (1 << bit):
                    bit_count[bit] += 1

        ans = 0

        for _ in range(k):
            num = 0

            for bit in range(32):
                if bit_count[bit] > 0:
                    num |= 1 << bit
                    bit_count[bit] -= 1

            ans = (ans + num * num) % MOD

        return ans