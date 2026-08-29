class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Store (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        result = nums[:]

        start = 0

        while start < n:
            end = start

            # Find all values that belong to the same group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Original indices in this group
            indices = [arr[i][1] for i in range(start, end + 1)]
            indices.sort()

            # Values are already sorted
            values = [arr[i][0] for i in range(start, end + 1)]

            # Put smallest values at smallest indices
            for i in range(len(indices)):
                result[indices[i]] = values[i]

            start = end + 1

        return result