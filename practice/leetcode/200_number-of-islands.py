class Solution:
    def check_neighbour(self, grid, i, j, n, m):
        if grid[i][j] == '0':
            return;
        grid[i][j] = '0'
        if i + 1 < n and grid[i+1][j] == '1':
            self.check_neighbour(grid, i + 1, j, n, m)
        if i -1 >= 0 and grid[i-1][j] == '1':
            self.check_neighbour(grid, i - 1, j, n, m)
        if j + 1 < m and grid[i][j + 1] == '1':
            self.check_neighbour(grid, i, j + 1, n, m)
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.check_neighbour(grid, i, j - 1, n, m)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '0':
                    self.check_neighbour(grid, i, j, n, m)
                    res += 1
        return res
