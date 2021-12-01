class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pi, pj = 1, 1
        res = [1] * len(nums)
        n = len(nums)
        for i in range(n):
            j = -1 - i
            res[i] *= pi
            res[j] *= pj
            pi *= nums[i]
            pj *= nums[j]
        return res
