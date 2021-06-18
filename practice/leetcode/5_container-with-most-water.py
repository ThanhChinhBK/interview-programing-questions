class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_s = 0
        ptr_l = 0
        ptr_r = len(height) - 1
        while ptr_l < ptr_r:
            max_s = max(max_s, min(height[ptr_l], height[ptr_r]) * (ptr_r - ptr_l))
            if height[ptr_l] < height[ptr_r]:
                ptr_l += 1
            else:
                ptr_r -= 1
        return max_s
