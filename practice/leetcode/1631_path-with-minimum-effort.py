import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        res = 0
        heap = [(0, 0, 0)]
        h, l = len(heights), len(heights[0])
        visited = set()
        while heap:
            d, x, y = heapq.heappop(heap)
            res = max(d, res)
            visited.add((x, y))
            if x == l - 1 and y == h - 1:
                return res
            for dx, dy in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
                if 0 <= dx < l and 0 <= dy < h and (dx, dy) not in visited:
                    heapq.heappush(heap, ((abs(heights[dy][dx] - heights[y][x]), dx, dy)))
        return res
