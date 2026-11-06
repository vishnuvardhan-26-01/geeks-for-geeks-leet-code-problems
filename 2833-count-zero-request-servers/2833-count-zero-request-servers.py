class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        indexed_queries = sorted(
            [(q, i) for i, q in enumerate(queries)]
        )

        ans = [0] * len(queries)
        freq = [0] * (n + 1)

        left = right = active = 0

        for q, idx in indexed_queries:
            start = q - x

            # Add logs within the right boundary
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if freq[server] == 0:
                    active += 1

                freq[server] += 1
                right += 1

            # Remove logs before the left boundary
            while left < right and logs[left][1] < start:
                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans