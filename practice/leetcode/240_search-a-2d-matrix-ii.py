class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None:
            return -1
        n = len(matrix)
        if n == 0:
            return -1
        m = len(matrix[0])
        row = 0
        col = m - 1
        while col >= 0 and row <= n - 1:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False
