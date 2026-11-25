class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Build the final parent relationships.
        new_parent = parent[:]
        last = {}

        def dfs(node):
            ch = s[node]

            if ch in last:
                new_parent[node] = last[ch]

            old = last.get(ch, -1)
            last[ch] = node

            for child in children[node]:
                dfs(child)

            if old == -1:
                del last[ch]
            else:
                last[ch] = old

        dfs(0)

        # Build the final tree.
        final_children = [[] for _ in range(n)]

        for i in range(1, n):
            final_children[new_parent[i]].append(i)

        # Calculate subtree sizes.
        answer = [1] * n

        def calculate(node):
            for child in final_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer