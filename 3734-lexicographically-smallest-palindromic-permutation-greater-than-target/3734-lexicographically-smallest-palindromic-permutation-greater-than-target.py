class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters in s
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd-frequency character
        odd_count = 0
        middle = ""

        for i in range(26):
            if freq[i] % 2 == 1:
                odd_count += 1
                middle = chr(i + ord('a'))

        if odd_count > 1:
            return ""

        # Build the multiset of characters for the left half
        half = []

        for i in range(26):
            half.extend([chr(i + ord('a'))] * (freq[i] // 2))

        half_len = len(half)

        def make_palindrome(left):
            left = ''.join(left)
            return left + middle + left[::-1]

        # ---------------------------------------------------------
        # Candidate 1:
        # Use exactly target[:half_len] as the left half.
        # This is important because the RIGHT half may make the
        # palindrome greater than target.
        # ---------------------------------------------------------

        best = ""

        rem = freq[:]
        possible = True

        for i in range(half_len):
            c = ord(target[i]) - ord('a')

            if rem[c] < 2:
                possible = False
                break

            rem[c] -= 2

        if possible:
            candidate = make_palindrome(target[:half_len])

            if candidate > target:
                best = candidate

        # ---------------------------------------------------------
        # Candidate 2:
        # Find the smallest left half strictly greater than
        # target[:half_len].
        # ---------------------------------------------------------

        target_half = target[:half_len]

        # Try every possible pivot from right to left.
        for pivot in range(half_len - 1, -1, -1):

            rem = freq[:]
            prefix_possible = True

            # Match target_half[:pivot]
            for i in range(pivot):
                c = ord(target_half[i]) - ord('a')

                if rem[c] < 2:
                    prefix_possible = False
                    break

                rem[c] -= 2

            if not prefix_possible:
                continue

            # At pivot, choose the smallest character greater
            # than target_half[pivot].
            t = ord(target_half[pivot]) - ord('a')

            for c in range(t + 1, 26):

                if rem[c] >= 2:

                    rem[c] -= 2

                    # Fill the rest with the smallest characters
                    suffix = []

                    for x in range(26):
                        suffix.extend(
                            [chr(x + ord('a'))] * (rem[x] // 2)
                        )

                    left = (
                        list(target_half[:pivot])
                        + [chr(c + ord('a'))]
                        + suffix
                    )

                    candidate = make_palindrome(left)

                    # Don't return immediately!
                    # Compare with the equal-left-half candidate.
                    if best == "" or candidate < best:
                        best = candidate

                    rem[c] += 2

        return best