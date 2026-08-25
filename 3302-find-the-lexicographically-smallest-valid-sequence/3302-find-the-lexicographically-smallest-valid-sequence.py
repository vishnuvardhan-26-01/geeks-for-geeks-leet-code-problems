class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # suf[i] = number of characters from the END of word2
        # that can be matched exactly using word1[i:].
        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            suf[i] = m - 1 - j

        ans = []
        pos = 0
        changed = False

        for j in range(m):
            while pos < n:

                # Use this index as an exact match
                if word1[pos] == word2[j]:
                    ans.append(pos)
                    pos += 1
                    break

                # Use the one allowed character change
                if not changed:
                    remaining = m - j - 1

                    if suf[pos + 1] >= remaining:
                        ans.append(pos)
                        pos += 1
                        changed = True
                        break

                pos += 1

            else:
                return []

        return ans