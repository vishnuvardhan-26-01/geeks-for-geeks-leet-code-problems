class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue

            while stack and stack[-1] > ch and last[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)