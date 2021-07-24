class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_seq_sum = nums[0]
        cur_seq_sum = nums[0]
        for i in range(1, len(nums)):
            cur_seq_sum = max(cur_seq_sum + nums[i], nums[i])
            max_seq_sum = max(max_seq_sum, cur_seq_sum)
        return max_seq_sum
