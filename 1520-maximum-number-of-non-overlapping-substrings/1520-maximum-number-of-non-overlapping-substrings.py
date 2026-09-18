class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        # Find the smallest valid interval starting from l
        def get_interval(l):
            r = last[ord(s[l]) - ord('a')]
            i = l

            while i <= r:
                c = ord(s[i]) - ord('a')

                # This character appeared before l,
                # so the interval cannot be valid.
                if first[c] < l:
                    return None

                r = max(r, last[c])
                i += 1

            return (l, r)

        intervals = []

        # Only need to try positions that are first occurrences
        for i in range(n):
            c = ord(s[i]) - ord('a')

            if first[c] == i:
                interval = get_interval(i)

                if interval:
                    intervals.append(interval)

        # Choose intervals greedily by earliest ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result