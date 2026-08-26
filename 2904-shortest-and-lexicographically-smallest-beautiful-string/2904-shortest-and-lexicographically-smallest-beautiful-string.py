class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        ones = 0
        best = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # We have exactly k ones
            while ones == k:
                # Remove leading zeros to make the substring shorter
                while left <= right and s[left] == '0':
                    left += 1

                candidate = s[left:right + 1]

                if (best == "" or
                    len(candidate) < len(best) or
                    (len(candidate) == len(best) and candidate < best)):
                    best = candidate

                # Move past the first 1
                if s[left] == '1':
                    ones -= 1
                left += 1

        return best