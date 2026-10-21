from collections import Counter

class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                target = sorted_nums[start:start + k]

                # The block must contain exactly the required elements.
                if Counter(block) != Counter(target):
                    valid = False
                    break

                # The block must be rotatable into non-decreasing order.
                drops = sum(
                    block[i] > block[(i + 1) % k]
                    for i in range(k)
                )

                if drops > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans