class Solution:
    def minOperations(self, nums):
        n = len(nums)
        INF = float('inf')
        ans = INF

        def check(arr):
            pos = arr.index(0)

            for i in range(n):
                if arr[(pos + i) % n] != i:
                    return -1

            return pos

        # Case 1: Original orientation
        k = check(nums)

        if k != -1:
            ans = min(ans, k, n - k + 2)

        # Case 2: Reversed orientation
        rev = nums[::-1]
        k = check(rev)

        if k != -1:
            ans = min(ans, min(k, n - k) + 1)

        return ans if ans != INF else -1