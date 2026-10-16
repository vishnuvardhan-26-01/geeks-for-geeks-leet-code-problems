from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n

        tree_sum = [0] * size
        tree_sq = [0] * size
        lazy = [0] * size

        def apply(node, length, val):
            tree_sq[node] = (tree_sq[node] + 2 * val * tree_sum[node] + length * val * val) % MOD
            tree_sum[node] = (tree_sum[node] + length * val) % MOD
            lazy[node] += val

        def push(node, left, right):
            if lazy[node] and left != right:
                mid = (left + right) // 2
                apply(node * 2, mid - left + 1, lazy[node])
                apply(node * 2 + 1, right - mid, lazy[node])
                lazy[node] = 0

        def update(node, left, right, ql, qr, val):
            if ql <= left and right <= qr:
                apply(node, right - left + 1, val)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr, val)

            tree_sum[node] = (tree_sum[node * 2] + tree_sum[node * 2 + 1]) % MOD
            tree_sq[node] = (tree_sq[node * 2] + tree_sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            # Distinct counts increase by 1 for subarrays starting
            # after the previous occurrence of x.
            update(1, 0, n - 1, prev + 1, i, 1)

            ans = (ans + tree_sq[1]) % MOD
            last[x] = i

        return ans