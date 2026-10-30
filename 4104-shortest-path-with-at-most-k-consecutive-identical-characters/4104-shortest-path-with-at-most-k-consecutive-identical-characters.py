import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost != dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in adj[u]:
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count <= k:
                    new_cost = cost + w

                    if new_cost < dist[v][new_count]:
                        dist[v][new_count] = new_cost
                        heapq.heappush(
                            pq, (new_cost, v, new_count)
                        )

        return -1