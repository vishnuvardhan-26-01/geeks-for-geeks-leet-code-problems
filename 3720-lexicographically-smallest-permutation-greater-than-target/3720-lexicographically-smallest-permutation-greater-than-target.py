class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # We will maintain the characters remaining after
        # matching target[:i].
        rem = freq[:]

        # First make sure target can be matched as a prefix.
        valid = [False] * (n + 1)
        valid[0] = True

        prefix_rem = [None] * (n + 1)
        prefix_rem[0] = freq[:]

        for i in range(n):
            idx = ord(target[i]) - ord('a')

            if prefix_rem[i][idx] == 0:
                break

            prefix_rem[i + 1] = prefix_rem[i][:]
            prefix_rem[i + 1][idx] -= 1
            valid[i + 1] = True

        # Try the rightmost position first.
        for i in range(n - 1, -1, -1):

            # target[:i] must be constructible from s
            if not valid[i]:
                continue

            rem = prefix_rem[i][:]

            target_idx = ord(target[i]) - ord('a')

            # Find smallest character greater than target[i]
            for c in range(target_idx + 1, 26):
                if rem[c] > 0:

                    rem[c] -= 1

                    # target[:i] + greater character
                    ans = target[:i] + chr(c + ord('a'))

                    # Put remaining characters in sorted order
                    for x in range(26):
                        ans += chr(x + ord('a')) * rem[x]

                    return ans

        return ""