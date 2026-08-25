from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)

        freq = [0] * (m + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (m + 1)

        for g in range(1, m + 1):
            c = 0
            for k in range(g, m + 1, g):
                c += freq[k]
            cnt[g] = c * (c - 1) // 2

        exact = [0] * (m + 1)
        for g in range(m, 0, -1):
            exact[g] = cnt[g]
            for k in range(g * 2, m + 1, g):
                exact[g] -= exact[k]

        pref = []
        vals = []
        s = 0
        for g in range(1, m + 1):
            if exact[g]:
                s += exact[g]
                vals.append(g)
                pref.append(s)

        ans = []
        for q in queries:
            ans.append(vals[bisect_left(pref, q + 1)])
        return ans