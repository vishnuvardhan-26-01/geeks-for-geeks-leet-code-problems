class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_number(date):
            month, day = map(int, date.split('-'))
            return sum(days[:month - 1]) + day

        start = max(day_number(arriveAlice), day_number(arriveBob))
        end = min(day_number(leaveAlice), day_number(leaveBob))

        return max(0, end - start + 1)