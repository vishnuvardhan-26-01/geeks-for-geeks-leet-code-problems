class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a target-sum subarray
        # completely inside arr[0...i]
        best = [float('inf')] * n

        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Since all numbers are positive, shrink from left
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Previous subarray must end before 'left'
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                # Store the shortest target subarray ending
                # at or before this position
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)
            else:
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == float('inf') else ans