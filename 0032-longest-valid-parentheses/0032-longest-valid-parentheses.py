class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        ans = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    # New invalid boundary
                    stack.append(i)
                else:
                    # Length of valid substring
                    ans = max(ans, i - stack[-1])

        return ans