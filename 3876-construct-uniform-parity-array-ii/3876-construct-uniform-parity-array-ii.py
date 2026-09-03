class Solution:
    def uniformArray(self, nums1):
        mn = min(nums1)

        # If minimum is odd, we can make every element odd.
        if mn % 2 == 1:
            return True

        # Minimum is even, so every element must be even.
        for x in nums1:
            if x % 2 == 1:
                return False

        return True