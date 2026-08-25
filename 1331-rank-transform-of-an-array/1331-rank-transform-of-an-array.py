class Solution:
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(set(arr))

        rank = {}

        for i, value in enumerate(sorted_arr):
            rank[value] = i + 1

        return [rank[x] for x in arr]