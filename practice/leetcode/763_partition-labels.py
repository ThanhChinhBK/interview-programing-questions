class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_dict = {c:i for i, c in enumerate(s)}
        j = 0
        anchor = 0
        res = []
        for i, c in enumerate(s):
            j = max(j, last_dict[c])
            if i == j:
                res.append(i + 1 - anchor)
                anchor = i + 1
        return res
