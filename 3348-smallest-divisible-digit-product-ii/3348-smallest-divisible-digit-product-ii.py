class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def maxPrimeFactor(x):
            d = 2
            mp = 1
            while d * d <= x:
                while x % d == 0:
                    mp = d
                    x //= d
                d += 1
            if x > 1:
                mp = x
            return mp

        if maxPrimeFactor(t) > 7:
            return "-1"

        n = len(num)
        digits = [int(c) for c in num]

        factors = {2: 0, 3: 0, 5: 0, 7: 0}
        tt = t
        for p in [2, 3, 5, 7]:
            while tt % p == 0:
                factors[p] += 1
                tt //= p
        if tt != 1:
            return "-1"

        need2, need3, need5, need7 = factors[2], factors[3], factors[5], factors[7]

        contrib = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        E2, E3 = need2, need3
        minCost23Table = [[0] * (E3 + 1) for _ in range(E2 + 1)]
        for e2 in range(E2 + 1):
            for e3 in range(E3 + 1):
                best = float('inf')
                for x in range(min(e2, e3) + 1):
                    r2 = e2 - x
                    r3 = e3 - x
                    cost = x + -(-r2 // 3) + -(-r3 // 2)
                    if cost < best:
                        best = cost
                minCost23Table[e2][e3] = best

        def minDigits(e2, e3, e5, e7):
            e2c = min(max(e2, 0), E2)
            e3c = min(max(e3, 0), E3)
            e5c = max(e5, 0)
            e7c = max(e7, 0)
            return minCost23Table[e2c][e3c] + e5c + e7c

        def bestSuffixIter(remaining_len, needed):
            n2, n3, n5, n7 = needed
            n2 = max(n2, 0); n3 = max(n3, 0); n5 = max(n5, 0); n7 = max(n7, 0)
            result = []
            for pos in range(remaining_len):
                rl = remaining_len - pos - 1
                found = False
                for d in range(1, 10):
                    c2, c3, c5, c7 = contrib[d]
                    nn2 = max(n2 - c2, 0); nn3 = max(n3 - c3, 0)
                    nn5 = max(n5 - c5, 0); nn7 = max(n7 - c7, 0)
                    if minDigits(nn2, nn3, nn5, nn7) <= rl:
                        result.append(d)
                        n2, n3, n5, n7 = nn2, nn3, nn5, nn7
                        found = True
                        break
                if not found:
                    return None
            if n2 == 0 and n3 == 0 and n5 == 0 and n7 == 0:
                return result
            return None

        # Precompute cumulative prefix exponents: prefix[i] = exponents contributed by digits[0:i]
        prefix2 = [0] * (n + 1)
        prefix3 = [0] * (n + 1)
        prefix5 = [0] * (n + 1)
        prefix7 = [0] * (n + 1)
        hasZeroPrefix = [False] * (n + 1)  # hasZeroPrefix[i] = True if digits[0:i] contains a 0
        for idx in range(n):
            c2, c3, c5, c7 = contrib.get(digits[idx], (0, 0, 0, 0)) if digits[idx] != 0 else (0, 0, 0, 0)
            prefix2[idx + 1] = prefix2[idx] + c2
            prefix3[idx + 1] = prefix3[idx] + c3
            prefix5[idx + 1] = prefix5[idx] + c5
            prefix7[idx + 1] = prefix7[idx] + c7
            hasZeroPrefix[idx + 1] = hasZeroPrefix[idx] or (digits[idx] == 0)

        # Check num itself
        if not hasZeroPrefix[n]:
            n2 = max(need2 - prefix2[n], 0)
            n3 = max(need3 - prefix3[n], 0)
            n5 = max(need5 - prefix5[n], 0)
            n7 = max(need7 - prefix7[n], 0)
            if n2 == 0 and n3 == 0 and n5 == 0 and n7 == 0:
                return num

        for i in range(n - 1, -1, -1):
            if hasZeroPrefix[i]:
                continue
            p2, p3, p5, p7 = prefix2[i], prefix3[i], prefix5[i], prefix7[i]
            startD = max(digits[i] + 1, 1)
            for d in range(startD, 10):
                c2, c3, c5, c7 = contrib[d]
                n2 = max(need2 - p2 - c2, 0)
                n3 = max(need3 - p3 - c3, 0)
                n5 = max(need5 - p5 - c5, 0)
                n7 = max(need7 - p7 - c7, 0)
                rl = n - i - 1
                if minDigits(n2, n3, n5, n7) <= rl:
                    suf = bestSuffixIter(rl, (n2, n3, n5, n7))
                    if suf is not None:
                        return ''.join(map(str, digits[:i] + [d] + suf))

        L0 = minDigits(need2, need3, need5, need7)
        targetLen = max(n + 1, L0)
        suf = bestSuffixIter(targetLen, (need2, need3, need5, need7))
        if suf is not None:
            return ''.join(map(str, suf))
        return "-1"