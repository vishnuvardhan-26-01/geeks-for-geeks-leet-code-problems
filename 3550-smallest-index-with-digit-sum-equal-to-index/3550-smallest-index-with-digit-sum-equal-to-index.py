class Solution:
    def smallestIndex(self, nums):
        for i, num in enumerate(nums):
            digit_sum = sum(map(int, str(num)))
            if digit_sum == i:
                return i
        return -1