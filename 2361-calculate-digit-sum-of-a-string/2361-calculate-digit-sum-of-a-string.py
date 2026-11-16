class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            result = []

            for i in range(0, len(s), k):
                group = s[i:i + k]
                total = sum(int(digit) for digit in group)
                result.append(str(total))

            s = ''.join(result)

        return s