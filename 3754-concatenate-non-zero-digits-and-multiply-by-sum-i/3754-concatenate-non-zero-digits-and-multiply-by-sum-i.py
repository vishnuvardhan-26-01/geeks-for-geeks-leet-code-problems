class Solution:
    def sumAndMultiply(self, n):
        s = str(n)
        
        digits = []
        total = 0
        
        for ch in s:
            if ch != '0':
                digits.append(ch)
                total += int(ch)
        
        if not digits:
            return 0
        
        x = int(''.join(digits))
        
        return x * total