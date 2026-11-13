from array import array

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Find next strictly greater element
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        # Binary lifting tables
        LOG = n.bit_length()

        up = [array('i', nxt)]
        cost = [
            array('q', (
                nums[i] * (nxt[i] - i)
                - (prefix[nxt[i]] - prefix[i])
                for i in range(n)
            ))
        ]

        for j in range(1, LOG):
            prev_up = up[-1]
            prev_cost = cost[-1]

            curr_up = array('i', [n]) * n
            curr_cost = array('q', [0]) * n

            for i in range(n):
                mid = prev_up[i]

                if mid < n:
                    curr_up[i] = prev_up[mid]
                    curr_cost[i] = prev_cost[i] + prev_cost[mid]

            up.append(curr_up)
            cost.append(curr_cost)

        # Calculate minimum cost of nums[l:r+1]
        def get_cost(l, r):
            total = 0
            pos = l

            for j in range(LOG - 1, -1, -1):
                nxt_pos = up[j][pos]

                if nxt_pos <= r:
                    total += cost[j][pos]
                    pos = nxt_pos

            total += (
                nums[pos] * (r - pos + 1)
                - (prefix[r + 1] - prefix[pos])
            )

            return total

        # Sliding window
        ans = 0
        left = 0

        for right in range(n):
            while get_cost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans