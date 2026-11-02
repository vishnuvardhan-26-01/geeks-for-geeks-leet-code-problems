class Solution:
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums) // 2]

        moves = 0
        for num in nums:
            moves += abs(num - median)

        return moves