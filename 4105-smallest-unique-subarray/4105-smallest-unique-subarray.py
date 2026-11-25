class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        if n == 1:
            return 1

        values = {v: i for i, v in enumerate(sorted(set(nums)))}
        arr = [values[x] for x in nums]

        sa = list(range(n))
        rank = arr[:]
        length = 1

        while length < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + length] if i + length < n else -1
            ))

            new_rank = [0] * n

            for i in range(1, n):
                a, b = sa[i - 1], sa[i]

                prev = (
                    rank[a],
                    rank[a + length] if a + length < n else -1
                )
                curr = (
                    rank[b],
                    rank[b + length] if b + length < n else -1
                )

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            length *= 2

        pos = [0] * n
        for i in range(n):
            pos[sa[i]] = i

        lcp = [0] * n
        h = 0

        for i in range(n):
            p = pos[i]

            if p == 0:
                continue

            j = sa[p - 1]

            while (i + h < n and j + h < n
                   and arr[i + h] == arr[j + h]):
                h += 1

            lcp[p] = h

            if h:
                h -= 1

        ans = n

        for i in range(n):
            p = pos[i]
            longest = lcp[p]

            if p + 1 < n:
                longest = max(longest, lcp[p + 1])

            candidate = longest + 1

            if candidate <= n - i:
                ans = min(ans, candidate)

        return ans