class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        ans = (n - len(rows)) * 2

        for seats in rows.values():
            left = 2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats
            middle = 4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats
            right = 6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans