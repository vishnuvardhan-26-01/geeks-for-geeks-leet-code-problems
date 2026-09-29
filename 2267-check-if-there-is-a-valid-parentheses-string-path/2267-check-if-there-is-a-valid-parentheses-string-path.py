class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # Start must be '('
        if grid[0][0] == ')':
            return False

        # dp[j] = set of possible balances at current cell
        dp = [set() for _ in range(n)]
        dp[0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                current = set()

                # From top
                if i > 0:
                    current.update(dp[j])

                # From left
                if j > 0:
                    current.update(dp[j - 1])

                if grid[i][j] == '(':
                    current = {balance + 1 for balance in current}
                else:
                    current = {balance - 1 for balance in current}

                # A valid prefix can never have negative balance
                current = {balance for balance in current if balance >= 0}

                dp[j] = current

        return 0 in dp[n - 1]