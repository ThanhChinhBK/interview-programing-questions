class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0] * n for _ in range(n)]
        points = [((0,0), 1)]
        length = 0
        while points:
            (cur_x, cur_y), distance = points.pop(0)
            if grid[cur_x][cur_y] or visited[cur_x][cur_y]:
                continue
            if cur_x == n-1 and cur_y == n - 1:
                return distance
            visited[cur_x][cur_y] = 1
            next_points = [
                (cur_x-1, cur_y-1), 
                (cur_x-1, cur_y),
                (cur_x-1, cur_y + 1),
                (cur_x, cur_y + 1),
                (cur_x + 1, cur_y + 1),
                (cur_x + 1, cur_y),
                (cur_x + 1, cur_y - 1),
                (cur_x, cur_y - 1)
            ]
            for (next_x, next_y) in next_points:
                if 0 <= next_x < n and 0 <= next_y < n:
                    points.append(((next_x, next_y), distance + 1))
        return -1
