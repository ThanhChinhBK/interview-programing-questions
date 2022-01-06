class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        change_list = [0] * 1001
        for trip in trips:
            change_list[trip[1]] += trip[0]
            change_list[trip[2]] += -trip[0]
        curr = 0
        for i in range(1000):
            curr += change_list[i]
            if curr > capacity:
                return False
        return True
                
