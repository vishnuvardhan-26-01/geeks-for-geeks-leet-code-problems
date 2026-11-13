class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        both = min(need1, need2)

        # Buy type 3 for the common requirement
        option1 = both * costBoth
        option1 += (need1 - both) * cost1
        option1 += (need2 - both) * cost2

        # Buy type 3 for all requirements (extra contribution is allowed)
        option2 = max(need1, need2) * costBoth

        # Buy everything individually
        option3 = need1 * cost1 + need2 * cost2

        return min(option1, option2, option3)