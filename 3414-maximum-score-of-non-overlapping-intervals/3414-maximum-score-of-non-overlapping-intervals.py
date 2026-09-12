class Solution:
    def maximumWeight(self, intervals):
        import bisect

        n = len(intervals)

        # Sort by starting position
        arr = [(l, r, w, i) for i, (l, r, w) in
               enumerate(intervals)]
        arr.sort()

        starts = [x[0] for x in arr]

        # Find the first interval that starts AFTER
        # the current interval ends.
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect.bisect_right(starts, arr[i][1])

        # dp[k][i] = best (score, indices) using at most
        # k intervals from i onward.
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):

                # Don't choose current interval
                skip = dp[k][i + 1]

                # Choose current interval
                l, r, w, idx = arr[i]

                next_score, next_indices = dp[k - 1][nxt[i]]

                take_score = w + next_score
                take_indices = tuple(sorted(
                    (idx,) + next_indices
                ))

                if take_score > skip[0]:
                    dp[k][i] = (take_score, take_indices)

                elif take_score < skip[0]:
                    dp[k][i] = skip

                else:
                    # Same score: choose lexicographically
                    # smaller index array.
                    if take_indices < skip[1]:
                        dp[k][i] = (take_score, take_indices)
                    else:
                        dp[k][i] = skip

        return list(dp[4][0][1])