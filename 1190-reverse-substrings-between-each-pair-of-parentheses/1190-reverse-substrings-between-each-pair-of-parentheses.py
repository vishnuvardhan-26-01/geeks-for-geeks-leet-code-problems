class Solution:
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())

                stack.pop()  # remove '('
                stack.extend(temp)

            else:
                stack.append(ch)

        return ''.join(stack)