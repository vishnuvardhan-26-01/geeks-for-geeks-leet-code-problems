from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(x):
            balance = 0

            for ch in x:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            current = queue.popleft()

            if isValid(current):
                result.append(current)
                found = True

            # Once we find valid strings at this level,
            # don't generate strings with more removals.
            if found:
                continue

            for i in range(len(current)):
                # Only remove parentheses, never letters
                if current[i] not in '()':
                    continue

                next_string = current[:i] + current[i + 1:]

                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)

        return result
        