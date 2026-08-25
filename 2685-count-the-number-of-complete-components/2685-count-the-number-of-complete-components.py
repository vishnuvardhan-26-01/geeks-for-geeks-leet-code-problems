class Solution:
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        for start in range(n):
            if visited[start]:
                continue

            stack = [start]
            visited[start] = True
            vertices = 0
            edge_count = 0

            while stack:
                node = stack.pop()
                vertices += 1
                edge_count += len(graph[node])

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            # Every edge was counted twice
            edge_count //= 2

            # Complete graph with k vertices has k*(k-1)/2 edges
            if edge_count == vertices * (vertices - 1) // 2:
                answer += 1

        return answer