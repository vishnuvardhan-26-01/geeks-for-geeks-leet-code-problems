class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        # Paths arriving from above each column
        vertical = [0] * n

        for i in range(m):
            left = 0

            for j in range(n):
                from_left = left
                from_up = vertical[j]

                # Starting position
                if i == 0 and j == 0:
                    from_left = 1
                    from_up = 0

                # Destination reached
                if i == m - 1 and j == n - 1:
                    return (from_left + from_up) % MOD

                if grid[i][j] == 1:
                    # Mirror:
                    # Incoming from left -> down
                    # Incoming from above -> right
                    right = from_up
                    down = from_left
                else:
                    # Empty cell: can move right or down
                    total = (from_left + from_up) % MOD
                    right = total
                    down = total

                left = right
                vertical[j] = down

        return 0