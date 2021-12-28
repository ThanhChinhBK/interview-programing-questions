class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[1])
        not_overlaps = 1
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= end:
                end = interval[1]
                not_overlaps += 1
        return len(intervals) - not_overlaps
