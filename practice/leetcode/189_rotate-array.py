class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_inplace(_list, from_ind, to_ind):
            """Reverse a list in place."""
            if from_ind >= len(_list):
                return
            if to_ind >= len(_list):
                to_ind = len(_list) - 1 
            for i in range(0, (to_ind-from_ind) // 2 + 1):
                _list[i + from_ind], _list[to_ind - i] = _list[to_ind - i], _list[from_ind + i]
    
        n = len(nums)
        k = k % n
        reverse_inplace(nums, 0, n - 1)
        reverse_inplace(nums, 0, k - 1)
        reverse_inplace(nums, k, n - 1)    
        
