class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        
        dp = [0] * 26
        total = 0
        
        for ch in s:
            i = ord(ch) - ord('a')
            
            new = (total + 1) % MOD
            
            total = (total + new - dp[i]) % MOD
            dp[i] = new
        
        return total