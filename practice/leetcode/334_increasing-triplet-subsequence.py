class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        i, j = float("inf"), float("inf")
        for val in nums:
            if val <= i:
                i = val
            elif val <= j:
                j = val
            else:
                return True
        return False
