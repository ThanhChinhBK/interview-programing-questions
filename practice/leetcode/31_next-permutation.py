class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        from wiki:
            1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
	    2. Find the largest index l > k such that nums[k] < nums[l].
	    3. Swap nums[k] and nums[l].
	    4. Reverse the sub-array nums[k + 1:].
        """
        k = len(nums) - 2
        while k >= 0:
            if nums[k + 1] > nums[k]:
                break
            k -= 1
        if k == -1:
            nums.reverse()
        else:
            l = len(nums) - 1
            while l > k:
                if nums[l] > nums[k]:
                    break
                l -= 1
            nums[k], nums[l] = nums[l], nums[k]
            nums[k + 1:] = nums[k+1:][::-1]
