class Solution:
    def canAliceWin(self, n):
        stones = 10
        alice = True

        while n >= stones:
            n -= stones
            stones -= 1
            alice = not alice

        return not alice