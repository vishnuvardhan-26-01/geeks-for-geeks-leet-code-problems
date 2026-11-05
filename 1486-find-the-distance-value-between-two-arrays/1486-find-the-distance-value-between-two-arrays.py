class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0

        for num in arr1:
            valid = True

            for x in arr2:
                if abs(num - x) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count