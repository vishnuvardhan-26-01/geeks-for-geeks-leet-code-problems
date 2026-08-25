class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 1000000007
        n = len(s)

        # Prefix sum of digits
        digit_sum = [0] * (n + 1)

        # Prefix value formed by non-zero digits
        value = [0] * (n + 1)

        # Prefix count of non-zero digits
        count = [0] * (n + 1)

        for i in range(n):
            d = ord(s[i]) - ord('0')

            digit_sum[i + 1] = digit_sum[i] + d
            count[i + 1] = count[i]

            value[i + 1] = value[i]

            if d != 0:
                count[i + 1] += 1
                value[i + 1] = (value[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            # Sum of digits in s[l..r]
            total_sum = digit_sum[r + 1] - digit_sum[l]

            # Number of non-zero digits
            cnt = count[r + 1] - count[l]

            if cnt == 0:
                ans.append(0)
                continue

            # value[r+1] contains all non-zero digits up to r.
            # Remove the non-zero digits before l.
            x = value[r + 1]

            before = value[l]

            # Need 10^cnt to shift away the prefix.
            x = (x - before * pow(10, cnt, MOD)) % MOD

            ans.append(x * total_sum % MOD)

        return ans