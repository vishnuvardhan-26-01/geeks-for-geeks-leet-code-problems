class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each segment tree node stores:
        # prod = product of the whole segment % k
        # cnt[r] = number of non-empty prefixes whose product % k == r
        size = 4 * n
        prod = [0] * size
        cnt = [[0] * k for _ in range(size)]

        def merge(left, right):
            lp, lc = left
            rp, rc = right

            p = (lp * rp) % k

            c = lc[:]

            # Prefixes that enter the right segment:
            # product(left) * prefix(product of right)
            for r in range(k):
                if rc[r]:
                    nr = (lp * r) % k
                    c[nr] += rc[r]

            return p, c

        def build(node, l, r):
            if l == r:
                p = nums[l] % k
                prod[node] = p
                cnt[node][p] = 1
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            p, c = merge(
                (prod[node * 2], cnt[node * 2]),
                (prod[node * 2 + 1], cnt[node * 2 + 1])
            )

            prod[node] = p
            cnt[node] = c

        def update(node, l, r, idx, value):
            if l == r:
                p = value % k
                prod[node] = p
                cnt[node] = [0] * k
                cnt[node][p] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            p, c = merge(
                (prod[node * 2], cnt[node * 2]),
                (prod[node * 2 + 1], cnt[node * 2 + 1])
            )

            prod[node] = p
            cnt[node] = c

        def query(node, l, r, ql):
            # We only need [ql, n-1]
            if r < ql:
                return None

            if ql <= l:
                return prod[node], cnt[node][:]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql)
            right = query(node * 2 + 1, mid + 1, r, ql)

            if left is None:
                return right
            if right is None:
                return left

            return merge(left, right)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:
            # Persistent update
            nums[index] = value
            update(1, 0, n - 1, index, value)

            # Count prefix products starting at `start`
            _, counts = query(1, 0, n - 1, start)

            result.append(counts[x])

        return result