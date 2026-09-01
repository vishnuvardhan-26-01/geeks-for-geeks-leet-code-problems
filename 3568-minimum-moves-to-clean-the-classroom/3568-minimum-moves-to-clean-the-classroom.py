from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find S and assign an index to every L
        start = None
        litter = {}

        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)

                elif classroom[i][j] == 'L':
                    litter[(i, j)] = count
                    count += 1

        # No litter to collect
        if count == 0:
            return 0

        all_mask = (1 << count) - 1

        # BFS state:
        # row, col, remaining energy, collected-litter mask, moves
        queue = deque()
        queue.append((start[0], start[1], energy, 0, 0))

        # visited[row][col][energy][mask]
        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c, e, mask, moves = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Can't move with zero energy
                if e == 0:
                    continue

                new_energy = e - 1
                new_mask = mask

                # Collect litter
                if (nr, nc) in litter:
                    index = litter[(nr, nc)]
                    new_mask |= (1 << index)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                new_moves = moves + 1

                # All litter collected
                if new_mask == all_mask:
                    return new_moves

                state = (nr, nc, new_energy, new_mask)

                if state not in visited:
                    visited.add(state)
                    queue.append(
                        (nr, nc, new_energy, new_mask, new_moves)
                    )

        return -1