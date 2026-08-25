class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = sorted((nums[i], i) for i in range(n))

        values = [x[0] for x in arr]
        pos = [0] * n

        for i in range(n):
            pos[arr[i][1]] = i

        # Find connected components
        component = [0] * n

        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                component[i] = component[i - 1] + 1
            else:
                component[i] = component[i - 1]

        # next[i] = farthest position reachable from i in one move
        nxt = [0] * n
        r = 0

        for i in range(n):
            if r < i:
                r = i

            while r + 1 < n and values[r + 1] - values[i] <= maxDiff:
                r += 1

            nxt[i] = r

        # Binary lifting
        LOG = n.bit_length()
        jump = [nxt]

        for _ in range(1, LOG):
            prev = jump[-1]
            cur = [0] * n

            for i in range(n):
                cur[i] = prev[prev[i]]

            jump.append(cur)

        answer = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if a == b:
                answer.append(0)
                continue

            if a > b:
                a, b = b, a

            # Different connected components
            if component[a] != component[b]:
                answer.append(-1)
                continue

            # Minimum number of jumps from a to b
            cur = a
            steps = 0

            for p in range(LOG - 1, -1, -1):
                if jump[p][cur] < b:
                    cur = jump[p][cur]
                    steps += 1 << p

            # Final jump
            if nxt[cur] >= b:
                steps += 1
                answer.append(steps)
            else:
                answer.append(-1)

        return answer