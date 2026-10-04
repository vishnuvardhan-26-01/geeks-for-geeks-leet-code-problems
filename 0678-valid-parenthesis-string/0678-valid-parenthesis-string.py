class Solution:
    def checkValidString(self, s):
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # Even the maximum possible balance is negative
            if high < 0:
                return False

            # '*' can act as empty, so minimum can't be negative
            low = max(0, low)

        return low == 0