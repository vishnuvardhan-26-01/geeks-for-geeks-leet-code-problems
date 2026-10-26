from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    stack = [(r, c)]
                    visited[r][c] = True
                    total = 0

                    while stack:
                        x, y = stack.pop()
                        total += grid[x][y]

                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy

                            if (0 <= nx < m and 0 <= ny < n
                                    and grid[nx][ny] > 0
                                    and not visited[nx][ny]):
                                visited[nx][ny] = True
                                stack.append((nx, ny))

                    if total % k == 0:
                        count += 1

        return count