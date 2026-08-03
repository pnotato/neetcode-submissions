class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] *n for _ in range(n)]
        l, r = 0, n-1
        top, bottom = 0, n-1

        i = 1
        while l <= r:

            # left first
            for j in range(l, r+1):
                res[top][j] = i
                i += 1
            top += 1

            for k in range(top, bottom+1):
                res[k][r] = i
                i += 1
            r -= 1

            for m in range(r, l-1, -1):
                res[bottom][m] = i
                i += 1
            bottom -= 1

            for n in range(bottom, top -1, -1):
                res[n][l] = i
                i += 1
            l += 1

        return res
            