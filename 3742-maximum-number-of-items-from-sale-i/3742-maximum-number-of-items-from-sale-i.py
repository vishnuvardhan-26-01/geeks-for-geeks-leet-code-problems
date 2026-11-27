class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)

        bonus = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonus[i] += 1

        arr = sorted(
            [(items[i][1], bonus[i] + 1) for i in range(n)],
            reverse=True
        )

        NEG = -10**18
        dp0 = [NEG] * (budget + 1)
        dp0[0] = 0

        ans = 0
        idx = 0

        while idx < n:
            price = arr[idx][0]
            dp1 = [NEG] * (budget + 1)

            while idx < n and arr[idx][0] == price:
                p, value = arr[idx]

                for c in range(budget, p - 1, -1):
                    if dp1[c - p] != NEG:
                        dp1[c] = max(
                            dp1[c],
                            dp1[c - p] + value
                        )

                    if dp0[c - p] != NEG:
                        dp1[c] = max(
                            dp1[c],
                            dp0[c - p] + value
                        )

                idx += 1

            for c in range(budget + 1):
                if dp1[c] != NEG:
                    total = dp1[c] + (budget - c) // price
                    ans = max(ans, total)
                    dp0[c] = max(dp0[c], dp1[c])

        return ans