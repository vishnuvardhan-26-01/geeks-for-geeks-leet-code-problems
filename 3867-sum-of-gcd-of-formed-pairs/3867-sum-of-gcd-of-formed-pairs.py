from math import gcd

class Solution:
    def gcdSum(self, nums):
        prefixGcd = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(gcd(x, mx))

        prefixGcd.sort()

        ans = 0
        i = 0
        j = len(prefixGcd) - 1

        while i < j:
            ans += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans