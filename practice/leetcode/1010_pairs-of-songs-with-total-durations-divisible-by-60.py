class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        nums = [0] * 60
        res = 0
        for song in time:
            res += nums[- (song % 60)]
            nums[song % 60] += 1
        return res
