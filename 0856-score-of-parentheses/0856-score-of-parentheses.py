class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                inner = stack.pop()

                if inner == 0:
                    value = 1
                else:
                    value = 2 * inner

                stack[-1] += value

        return stack[0]