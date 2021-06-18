class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        count = len(nums1) + len(nums2)
        nums = []
        j = 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums2[j] < nums1[i]:
                nums.append(nums2[j])
                j += 1
            nums.append(nums1[i])
        nums += nums2[j: len(nums2)]
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        return (nums[len(nums) // 2]  + nums[len(nums) // 2 -1]) / 2
