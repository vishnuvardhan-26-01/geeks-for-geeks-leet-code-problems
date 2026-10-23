class Solution:
    def sortPermutation(self, nums):
        k = -1

        for i, x in enumerate(nums):
            if x != i:
                k &= x

        return max(k, 0)