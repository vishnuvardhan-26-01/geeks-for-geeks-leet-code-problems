class Solution:
    def reverseDegree(self, s):
        ans = 0

        for i, ch in enumerate(s):
            value = 26 - (ord(ch) - ord('a'))
            ans += value * (i + 1)

        return ans