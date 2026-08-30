class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        from_front = right + 1
        from_back = n - left
        from_both = (left + 1) + (n - right)

        return min(from_front, from_back, from_both)