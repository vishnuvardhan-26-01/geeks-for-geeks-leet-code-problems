class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        indexed = [(nums[i], i) for i in range(n)]
        indexed.sort()

        group = [0] * n

        current_group = 0
        group[indexed[0][1]] = current_group

        for i in range(1, n):
            if indexed[i][0] - indexed[i - 1][0] > maxDiff:
                current_group += 1

            group[indexed[i][1]] = current_group

        answer = []

        for u, v in queries:
            answer.append(group[u] == group[v])

        return answer