class Solution:
    def minOperations(self, s):
        if s == ''.join(sorted(s)):
            return 0

        n = len(s)

        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        if s[0] == mn or s[-1] == mx:
            return 1

        if s[0] == mx and s[-1] == mn:
            if s.count(mx) == 1 and s.count(mn) == 1:
                return 3

        return 2