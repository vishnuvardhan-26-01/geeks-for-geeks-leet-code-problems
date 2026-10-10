class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2
            needed = sum(max(0, d - mid) for d in diffs)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        limit = left
        remaining = k - sum(max(0, d - limit) for d in diffs)

        # Reduce all differences to at most limit.
        ans = sum(min(d, limit) ** 2 for d in diffs)

        # Use remaining operations to reduce some limit-sized differences by 1.
        ans -= remaining * (2 * limit - 1)

        return ans