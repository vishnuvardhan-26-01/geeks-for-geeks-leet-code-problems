class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        max_overlap = 0

        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):

                overlap = 0

                for i in range(n):
                    for j in range(n):

                        ni = i + dr
                        nj = j + dc

                        if 0 <= ni < n and 0 <= nj < n:
                            if img1[i][j] == 1 and img2[ni][nj] == 1:
                                overlap += 1

                max_overlap = max(max_overlap, overlap)

        return max_overlap