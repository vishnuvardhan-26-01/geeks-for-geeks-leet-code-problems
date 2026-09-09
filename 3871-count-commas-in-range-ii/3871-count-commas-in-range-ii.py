class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        power = 1000

        while power <= n:
            ans += n - power + 1
            power *= 1000

        return ans