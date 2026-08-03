class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every value i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            # perform the check here to see if there's remaining rows
            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
# essentially, initialize 4 pointers. Right and bottom should be 1 more than usual. you want to shrink the matrix recursively
# go in a spiral. when you hit the right most value,  and thus complete a row, move the top pointer down.
# when you finish the rightmopst row, move the rightmost pointer down.