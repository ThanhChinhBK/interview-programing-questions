class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        beg, mid, end = 0, 0, len(nums) - 1
        while mid <= end:
            if nums[mid] == 0:
                nums[mid], nums[beg] = nums[beg], nums[mid]
                beg += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
            else:
                mid += 1
