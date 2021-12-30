from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter()
        sum_ = 0
        res = 0
        counter[0] = 1
        for num in nums:
            sum_ += num
            res += counter[sum_ - k]
            counter[sum_] += 1
        return res
