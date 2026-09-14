class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        x_overlap = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        y_overlap = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])

        return x_overlap and y_overlap