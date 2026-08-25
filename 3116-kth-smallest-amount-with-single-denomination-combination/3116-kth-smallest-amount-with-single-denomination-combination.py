from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                value = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        value = lcm(value, coins[i])

                        if value > x:
                            valid = False
                            break

                if valid:
                    amount = x // value

                    if bits % 2:
                        total += amount
                    else:
                        total -= amount

            return total

        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low