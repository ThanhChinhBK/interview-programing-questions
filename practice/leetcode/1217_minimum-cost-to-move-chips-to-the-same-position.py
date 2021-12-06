class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_pos_chips = odd_pos_chips = 0
        for pos in position:
            if pos % 2 == 0:
                even_pos_chips += 1
            else:
                odd_pos_chips += 1
        return min(even_pos_chips, odd_pos_chips)
